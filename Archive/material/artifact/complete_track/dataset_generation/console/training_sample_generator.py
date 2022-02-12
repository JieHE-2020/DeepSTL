from translation.level_1.scheduling.SP_scheduler import SPScheduler
from translation.level_2.TP_atom.scheduling.TP_atom_sheduler import TPAtomScheduler
from translation.level_3.eventually_always.normal.eventually_always_atom_handler import EventuallyAlwaysAtomHandler
from translation.level_3.always_eventually.normal.always_eventually_atom_handler import AlwaysEventuallyAtomHandler
from translation.medium.eventually.normal.eventually_SP_handler import EventuallySPHandler
from translation.medium.always.normal.always_SP_handler import AlwaysSPHandler
from public import parameters
from corpus import conjunction
from corpus import sig_mode_name_generate
from corpus import number_generate
import copy
import random
import math
import global_variables_id
import global_variables_num
import time


class TrainingSampleGenerator:

    def __init__(self, limit_num_formula, limit_num_clause):
        global_variables_id._init()
        global_variables_num._init()
        global_variables_id.set_value('ID_COUNTER', 0)
        global_variables_num.set_value('NUM_COUNTER', 0)

        # number of different translations for a single formula
        self.limit_num_formula = limit_num_formula
        # number of different translations for a single clause
        self.limit_num_clause = limit_num_clause

        self.formula_type = self.formula_type_select()
        self.formula_expression = ''
        self.formula_translation_list = []
        self.generation_dict = dict()

        if self.formula_type == 'invariance_reachability':
            self.group1_processing()
        elif self.formula_type == 'immediate_response':
            self.group2_processing()
        elif self.formula_type == 'temporal_response':
            self.group3_processing()
        else:  # self.formula_type == 'stabilization_recurrence'
            self.group4_processing()

    @staticmethod
    def formula_type_select():
        # probabilities taken from empirical study
        selector = random.randint(1, 1000)
        # print(selector)
        if 1 <= selector < 300:
            formula_type = 'invariance_reachability'  # group 1 - G_I (SP) / F_I (SP)
        elif 300 <= selector < 300 + 208:
            formula_type = 'immediate_response'  # group 2 - G (SP -> SP)
        elif 300 + 208 <= selector < 300 + 208 + 254:
            formula_type = 'temporal_response'  # group 3 - G (P -> TP)
        else:
            formula_type = 'stabilization_recurrence'  # group 4 - G (P -> NTP)

        # formula_type = 'invariance_reachability'
        # formula_type = 'immediate_response'
        # formula_type = 'temporal_response'
        # formula_type = 'stabilization_recurrence'
        return formula_type

    def group1_processing(self):
        """
        invariance/reachability: : G_I (SP) / F_I (SP)
        """
        try_num = 0
        while True:
            # 1. preparation - set unchanged parameters
            position = 'after_imply'
            # for NTP
            nest_info_dict = {
                'whetherNest': False,
                'nestLayer': 1,
                'whetherBottom': True,
                'hasParallelSuccessor': False,
                'tense': 'present'
            }

            clause_type = 'TP'
            point = random.randint(0, 1)
            if point == 0:  # F_I (SP)
                tp_sp_handler = EventuallySPHandler(position, nest_info_dict, self.limit_num_clause)
                tp_sp_translation = tp_sp_handler.eventually_sp_translator.random_selected_translations
            else:  # G_I (SP)
                tp_sp_handler = AlwaysSPHandler(position, nest_info_dict, self.limit_num_clause)
                tp_sp_translation = tp_sp_handler.always_sp_translator.random_selected_translations

            clause_info_dict = {
                'type': clause_type,
                # 'signal_name_set': set(ntp_atom_handler.ntp_info_dict['ingredient'][0]['ingredient'][0]),
                'expr': tp_sp_handler.tp_info_dict['expression'],
                'eng_list': tp_sp_translation
            }

            # check whether it is repetitive with existing formulas in the data set
            candidate_formula = clause_info_dict['expr']
            flag = self.formula_check(candidate_formula)
            try_num = try_num + 1

            if not flag or try_num > parameters.max_try_times:
                break

        self.finalize_assemble_without_response(clause_info_dict, candidate_formula)

    def group2_processing(self):
        """
        immediate response: G (SP -> SP)
        """
        try_num = 0
        while True:
            clause1_info_dict = self.SP_clause1_processing()
            clause2_info_dict = self.SP_clause2_processing()

            # check whether the candidate formula is repetitive with existing formulas in the data set
            clause1_expr = clause1_info_dict['expr']
            clause2_expr = clause2_info_dict['expr']
            candidate_formula = 'always ' + '( ' + clause1_expr + ' -> ' + clause2_expr + ' )'
            flag = self.formula_check(candidate_formula)
            try_num = try_num + 1
            if not flag or try_num > parameters.max_try_times:
                break

        self.finalize_assemble_with_response(clause1_info_dict, clause2_info_dict, candidate_formula)

    def group3_processing(self):
        """
        temporal response: G (P -> TP)
        P := SP | TP
        """
        try_num = 0
        while True:
            clause1_info_dict = self.P_clause1_processing()
            clause2_info_dict = self.TP_clause2_processing()

            # check whether the candidate formula is repetitive with existing formulas in the data set
            clause1_expr = clause1_info_dict['expr']
            clause2_expr = clause2_info_dict['expr']
            candidate_formula = 'always ' + '( ' + clause1_expr + ' -> ' + clause2_expr + ' )'
            flag = self.formula_check(candidate_formula)
            try_num = try_num + 1
            if not flag or try_num > parameters.max_try_times:
                break

        self.finalize_assemble_with_response(clause1_info_dict, clause2_info_dict, candidate_formula)

    def group4_processing(self):
        """
        stabilization_recurrence: G (P -> NTP)
        """
        try_num = 0
        while True:
            clause1_info_dict = self.P_clause1_processing()
            clause2_info_dict = self.NTP_clause2_processing()

            # check whether the candidate formula is repetitive with existing formulas in the data set
            clause1_expr = clause1_info_dict['expr']
            clause2_expr = clause2_info_dict['expr']
            candidate_formula = 'always ' + '( ' + clause1_expr + ' -> ' + clause2_expr + ' )'
            flag = self.formula_check(candidate_formula)
            try_num = try_num + 1
            if not flag or try_num > parameters.max_try_times:
                break

        self.finalize_assemble_with_response(clause1_info_dict, clause2_info_dict, candidate_formula)

    def SP_clause1_processing(self):
        # 1. preparation - set unchanged parameters
        position = 'before_imply'
        # type_preference is for ATOM
        # - default: assign equal probability for SE and ERE regardless of position
        # - positional: for clause1, the prob for SE to select is 0.2, while the prob for ERE to select is 0.8
        #               for clause2, the prob for SE to select is 0.9, while the prob for ERE to select is 0.1
        # - SE: only select SE
        # - ERE: only select ERE
        type_preference = 'positional'
        # atom_type is for BC_ATOM
        # - random: to assemble boolean combination,
        #           the prob for SE to select is 0.8, while the prob for ERE to select is 0.2
        # - SE: only select SE
        atom_type = 'random'

        clause1_type = 'SP'
        sp_scheduler = SPScheduler(position, type_preference, atom_type, self.limit_num_clause)

        expr_type_list = sp_scheduler.expr_type_list
        if 'ERE' not in expr_type_list:
            clause1_conj_list = copy.deepcopy(conjunction.conj_clause1_special)
        else:
            clause1_conj_list = copy.deepcopy(conjunction.conj_clause1_general)

        clause1_info_dict = {
            'type': clause1_type,
            # 'signal_name_set': set(sp_scheduler.signal_name_list),
            'expr': sp_scheduler.sp_expression,
            'eng_list': sp_scheduler.sp_translation,
            'conj_list': clause1_conj_list
        }

        return clause1_info_dict

    def SP_clause2_processing(self):
        # 1. preparation - set unchanged parameters
        position = 'after_imply'
        # type_preference is for ATOM
        # - default: assign equal probability for SE and ERE regardless of position
        # - positional: for clause1, the prob for SE to select is 0.2, while the prob for ERE to select is 0.8
        #               for clause2, the prob for SE to select is 0.9, while the prob for ERE to select is 0.1
        # - SE: only select SE
        # - ERE: only select ERE
        type_preference = 'positional'
        # atom_type is for BC_ATOM
        # - random: to assemble boolean combination,
        #           the prob for SE to select is 0.8, while the prob for ERE to select is 0.2
        # - SE: only select SE
        atom_type = 'random'

        clause_type = 'SP'
        sp_scheduler = SPScheduler(position, type_preference, atom_type, self.limit_num_clause)
        clause2_conj_list = copy.deepcopy(conjunction.conj_clause2_general)

        clause2_info_dict = {
            'type': clause_type,
            # 'signal_name_set': set(sp_scheduler.signal_name_list),
            'expr': sp_scheduler.sp_expression,
            'eng_list': sp_scheduler.sp_translation,
            'conj_list': clause2_conj_list
        }

        return clause2_info_dict

    def P_clause1_processing(self):
        """
        P := SP | TP
        the prob to select SP is 0.8, while the prob to select TP is 0.2
        """
        # 1. preparation - set unchanged parameters
        position = 'before_imply'
        # for SP
        type_preference = 'positional'
        atom_type = 'random'
        # for TP
        nest_info_dict = {
            'whetherNest': False,
            'nestLayer': 1,
            'whetherBottom': True,
            'hasParallelSuccessor': False,
            'tense': 'present'
        }

        # 2. select clause type and start processing
        point = random.randint(1, 10)
        # point = 0  #  only select SP
        if point <= 8:
            clause1_type = 'SP'
            sp_scheduler = SPScheduler(position, type_preference, atom_type, self.limit_num_clause)

            expr_type_list = sp_scheduler.expr_type_list
            if 'ERE' not in expr_type_list:
                clause1_conj_list = copy.deepcopy(conjunction.conj_clause1_special)
            else:
                clause1_conj_list = copy.deepcopy(conjunction.conj_clause1_general)

            clause1_info_dict = {
                'type': clause1_type,
                # 'signal_name_set': set(sp_scheduler.signal_name_list),
                'expr': sp_scheduler.sp_expression,
                'eng_list': sp_scheduler.sp_translation,
                'conj_list': clause1_conj_list
            }

        else:
            clause_type = 'TP'
            tp_atom_scheduler = TPAtomScheduler(position, nest_info_dict, self.limit_num_clause)
            clause1_conj_list = copy.deepcopy(conjunction.conj_clause1_general)

            clause1_info_dict = {
                'type': clause_type,
                # 'signal_name_set': set(tp_atom_scheduler.signal_name_list),
                'expr': tp_atom_scheduler.tp_atom_expression,
                'eng_list': tp_atom_scheduler.tp_atom_translation,
                'conj_list': clause1_conj_list
            }

        return clause1_info_dict

    def TP_clause2_processing(self):
        # 1. preparation - set unchanged parameters
        position = 'after_imply'
        # for TP
        nest_info_dict = {
            'whetherNest': False,
            'nestLayer': 1,
            'whetherBottom': True,
            'hasParallelSuccessor': False,
            'tense': 'present'
        }

        clause_type = 'TP'
        tp_atom_scheduler = TPAtomScheduler(position, nest_info_dict, self.limit_num_clause)

        if tp_atom_scheduler.layer_selected == 1:
            clause2_conj_list = conjunction.conj_clause2_general
        else:
            clause2_conj_list = conjunction.conj_clause2_special

        clause2_info_dict = {
            'type': clause_type,
            # 'signal_name_set': set(tp_atom_scheduler.signal_name_list),
            'expr': tp_atom_scheduler.tp_atom_expression,
            'eng_list': tp_atom_scheduler.tp_atom_translation,
            'conj_list': clause2_conj_list
        }

        return clause2_info_dict

    def NTP_clause2_processing(self):
        # 1. preparation - set unchanged parameters
        position = 'after_imply'
        # for NTP
        nest_info_dict = {
            'whetherNest': True,
            'nestLayer': 2,
            'whetherBottom': True,
            'hasParallelSuccessor': False,
            'tense': 'future'
        }

        clause_type = 'NTP'
        point = random.randint(0, 1)
        if point == 0:  # eventually always
            ntp_atom_handler = EventuallyAlwaysAtomHandler(position, nest_info_dict, self.limit_num_clause)
            ntp_atom_translation = ntp_atom_handler.eventually_always_atom_translator.random_selected_translations
        else:  # always eventually
            ntp_atom_handler = AlwaysEventuallyAtomHandler(position, nest_info_dict, self.limit_num_clause)
            ntp_atom_translation = ntp_atom_handler.always_eventually_atom_translator.random_selected_translations

        clause2_conj_list = conjunction.conj_clause2_general

        clause2_info_dict = {
            'type': clause_type,
            # 'signal_name_set': set(ntp_atom_handler.ntp_info_dict['ingredient'][0]['ingredient'][0]),
            'expr': ntp_atom_handler.ntp_info_dict['expression'],
            'eng_list': ntp_atom_translation,
            'conj_list': clause2_conj_list
        }

        return clause2_info_dict

    def finalize_assemble_without_response(self, clause_info_dict, candidate_formula):
        # 1. write the candidate formula into the formula data set
        self.formula_expression = candidate_formula
        self.formula_write(self.formula_expression)

        # 2. assemble translations
        formula_eng_list = clause_info_dict['eng_list']
        if len(formula_eng_list) > self.limit_num_formula:
            formula_eng_list = random.sample(formula_eng_list, self.limit_num_formula)

        def period_add(sentence):
            return sentence + '.'

        self.formula_translation_list = list(map(period_add, formula_eng_list))
        self.generation_dict = self.identifier_num_process()

        # 3. write the formula and its translations into the .csv file
        self.csv_file_write()

    def finalize_assemble_with_response(self, clause1_info_dict, clause2_info_dict, candidate_formula):
        # 1. write the candidate formula into the formula data set
        self.formula_expression = candidate_formula
        self.formula_write(self.formula_expression)

        # 2. assemble translations
        clause1_eng_list = clause1_info_dict['eng_list']
        clause1_conj_list = clause1_info_dict['conj_list']
        clause2_eng_list = clause2_info_dict['eng_list']
        clause2_conj_list = clause2_info_dict['conj_list']
        formula_eng_list = []
        if (len(clause1_eng_list) * len(clause2_eng_list) <=
                1 / parameters.union_operation_threshold_probability * self.limit_num_formula):
            # use for loop
            for c1_eng in clause1_eng_list:
                for c2_eng in clause2_eng_list:
                    conj_c1 = random.choice(clause1_conj_list)
                    conj_c2 = random.choice(clause2_conj_list)
                    if 'then' in c1_eng and 'then' in conj_c2:
                        point = random.randint(1, 10)
                        if point <= 8:  # set 0.8 prob to drop
                            continue
                    formula_eng = conj_c1 + c1_eng + conj_c2 + c2_eng + '.'
                    formula_eng_list.append(formula_eng)
        else:
            # use union operation
            formula_eng_set = set()
            while len(formula_eng_set) < math.ceil(self.limit_num_formula):
                conj_c1 = random.choice(clause1_conj_list)
                c1_eng = random.choice(clause1_eng_list)
                c2_eng = random.choice(clause2_eng_list)
                conj_c2 = random.choice(clause2_conj_list)
                if 'then' in c1_eng and 'then' in conj_c2:
                    point = random.randint(1, 10)
                    if point <= 8:  # set 0.8 prob to drop
                        continue
                formula_eng = conj_c1 + c1_eng + conj_c2 + c2_eng + '.'
                formula_eng_set.add(formula_eng)
            formula_eng_list = sorted(formula_eng_set)

        self.formula_translation_list = self.random_select_translation(formula_eng_list, self.limit_num_formula)
        self.generation_dict = self.identifier_num_process()

        # 3. write the formula and its translations into the .csv file
        self.csv_file_write()

        # # 4. write the formula and its translations together into the .txt file
        # self.txt_file_write(self.formula_expression, self.formula_translation_list)

    def identifier_num_process(self):
        formula_expression_list = []
        for i in range(len(self.formula_translation_list)):
            formula_expression_list.append(self.formula_expression)
        id_num = global_variables_id.get_value('ID_COUNTER')
        constant_num = global_variables_num.get_value('NUM_COUNTER')

        formula_list_id_num = []
        translation_list_id_num = []
        formula_list_no_split = []
        translation_list_no_split = []
        formula_list_split = []
        translation_list_split = []

        for i in range(len(self.formula_translation_list)):
            formula = formula_expression_list[i]
            eng = self.formula_translation_list[i]
            formula_list_id_num.append(formula)
            translation_list_id_num.append(eng)

            formula_no_split = copy.deepcopy(formula)
            eng_no_split = copy.deepcopy(eng)
            formula_split = copy.deepcopy(formula)
            eng_split = copy.deepcopy(eng)
            # process numbers
            for k in range(constant_num):
                if 'num'+str(k+1)+'value#' in formula:
                    value = number_generate.atom_value_substitute()
                    formula_no_split = formula_no_split.replace('num'+str(k+1)+'value#', value)
                    eng_no_split = eng_no_split.replace('num'+str(k+1)+'value#', value)
                    formula_split = formula_split.replace('num'+str(k+1)+'value#', value)
                    eng_split = eng_split.replace('num'+str(k+1)+'value#', value)

                if 'num'+str(k+1)+'valuea#' in formula and 'num'+str(k+1)+'valueb#' in formula:
                    [value_a, value_b] = number_generate.atom_value_range_substitute()
                    formula_no_split = formula_no_split.replace('num'+str(k+1)+'valuea#', value_a)
                    formula_no_split = formula_no_split.replace('num'+str(k+1)+'valueb#', value_b)
                    eng_no_split = eng_no_split.replace('num'+str(k+1)+'valuea#', value_a)
                    eng_no_split = eng_no_split.replace('num'+str(k+1)+'valueb#', value_b)
                    formula_split = formula_split.replace('num'+str(k+1)+'valuea#', value_a)
                    formula_split = formula_split.replace('num'+str(k+1)+'valueb#', value_b)
                    eng_split = eng_split.replace('num'+str(k+1)+'valuea#', value_a)
                    eng_split = eng_split.replace('num'+str(k+1)+'valueb#', value_b)

                if 'num'+str(k+1)+'temporal#' in formula:
                    t_value = number_generate.t_value_substitute()
                    formula_no_split = formula_no_split.replace('num'+str(k+1)+'temporal#', t_value)
                    eng_no_split = eng_no_split.replace('num'+str(k+1)+'temporal#', t_value)
                    formula_split = formula_split.replace('num'+str(k+1)+'temporal#', t_value)
                    eng_split = eng_split.replace('num'+str(k+1)+'temporal#', t_value)

                if 'num' + str(k+1) + 'temporala#' in formula and 'num' + str(k+1) + 'temporalb#' in formula:
                    [t_value_a, t_value_b] = number_generate.t_value_range_substitute()
                    formula_no_split = formula_no_split.replace('num'+str(k+1)+'temporala#', t_value_a)
                    formula_no_split = formula_no_split.replace('num'+str(k+1)+'temporalb#', t_value_b)
                    eng_no_split = eng_no_split.replace('num'+str(k+1)+'temporala#', t_value_a)
                    eng_no_split = eng_no_split.replace('num'+str(k+1)+'temporalb#', t_value_b)
                    formula_split = formula_split.replace('num'+str(k+1)+'temporala#', t_value_a)
                    formula_split = formula_split.replace('num'+str(k+1)+'temporalb#', t_value_b)
                    eng_split = eng_split.replace('num'+str(k+1)+'temporala#', t_value_a)
                    eng_split = eng_split.replace('num'+str(k+1)+'temporalb#', t_value_b)

            # process identifiers
            random_id_no_split = ''
            random_id_set = set()
            for j in range(id_num):
                # within one formula, generate non-repetitive identifiers
                flag = True
                while flag:
                    random_id_no_split = sig_mode_name_generate.random_identifier_substitute()
                    old_len = len(random_id_set)
                    random_id_set.add(random_id_no_split)
                    if len(random_id_set) == old_len + 1:
                        flag = False
                formula_no_split = formula_no_split.replace('id'+str(j+1), random_id_no_split)
                if j == 0 and 'Id1' in eng_no_split:
                    eng_no_split = eng_no_split.replace('Id' + str(j + 1), random_id_no_split)
                else:
                    eng_no_split = eng_no_split.replace('id'+str(j+1), random_id_no_split)
                # split identifier
                id_str_list = list(random_id_no_split)
                random_id_split = ' '.join(id_str_list)
                formula_split = formula_split.replace('id'+str(j+1), random_id_split)
                if j == 0 and 'Id1' in eng_split:
                    eng_split = eng_split.replace('Id'+str(j+1), random_id_split)
                else:
                    eng_split = eng_split.replace('id'+str(j+1), random_id_split)

            formula_list_no_split.append(formula_no_split)
            translation_list_no_split.append(eng_no_split)
            formula_list_split.append(formula_split)
            translation_list_split.append(eng_split)

        # only difference is the name of identifiers
        generation_dict = {
            'formula_list_id_num': formula_list_id_num,
            'translation_list_id_num': translation_list_id_num,
            'formula_list_no_split': formula_list_no_split,
            'translation_list_no_split': translation_list_no_split,
            'formula_list_split': formula_list_split,
            'translation_list_split': translation_list_split,
        }

        return generation_dict

    @staticmethod
    def random_select_translation(eng_list, limit_num):
        if len(eng_list) > limit_num:
            random_eng_list = random.sample(eng_list, limit_num)
        else:
            random_eng_list = eng_list

        return random_eng_list

    @staticmethod
    def formula_check(candidate_formula):
        # check whether the candidate formula is repetitive with formulas that have been already generated
        flag = False
        with open('./data/STL_formulas.txt', 'r') as f:
            formula_set = set(f.readline())
            candidate_formula = candidate_formula + '\n'
            if candidate_formula in formula_set:
                flag = True

        return flag

    @staticmethod
    def formula_write(formula_added):
        with open('./data/STL_formulas.txt', 'a') as f:
            f.write(formula_added + '\n')

    def csv_file_write(self):
        formula_list_id_num = self.generation_dict['formula_list_id_num']
        translation_list_id_num = self.generation_dict['translation_list_id_num']
        with open('./data/corpus_id.csv', 'a') as outfile:
            for i in range(len(formula_list_id_num)):
                raw_string = \
                    '"{}","{}","{}"'.format(formula_list_id_num[i], translation_list_id_num[i], self.formula_type)
                outfile.write(raw_string)
                outfile.write('\n')

        formula_list_no_split = self.generation_dict['formula_list_no_split']
        translation_list_no_split = self.generation_dict['translation_list_no_split']
        with open('./data/corpus_no_split.csv', 'a') as outfile:
            for i in range(len(formula_list_no_split)):
                raw_string = \
                    '"{}","{}","{}"'.format(formula_list_no_split[i], translation_list_no_split[i], self.formula_type)
                outfile.write(raw_string)
                outfile.write('\n')

        formula_list_split = self.generation_dict['formula_list_split']
        translation_list_split = self.generation_dict['translation_list_split']
        with open('./data/corpus_split.csv', 'a') as outfile:
            for i in range(len(formula_list_split)):
                raw_string = \
                    '"{}","{}","{}"'.format(formula_list_split[i], translation_list_split[i], self.formula_type)
                outfile.write(raw_string)
                outfile.write('\n')

    # @staticmethod
    # def txt_file_write(formula_added, eng_list):
    #     with open('./data/tokenization_dataset.txt', 'a') as f:
    #         for eng in eng_list:
    #             f.write(eng + '\n')
    #         f.write(formula_added + '\n')
