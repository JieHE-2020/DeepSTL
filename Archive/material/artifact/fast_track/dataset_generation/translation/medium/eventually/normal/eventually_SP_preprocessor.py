from template import TP_template
from commands.command_eventually import PreCmdEventually
from translation.level_2.TP_atom.original_TP_atom.eventually.normal.eventually_atom_quick_refiner_assembler \
    import EventuallyAtomQuickRefinerAssembler
from translation.level_2.TP_atom.original_TP_atom.eventually.normal.SP.eventually_atom_template_refiner \
    import EventuallyAtomTemplateRefiner
from translation.level_2.TP_atom.original_TP_atom.eventually.normal.SP.eventually_atom_assembler \
    import EventuallyAtomAssembler
from public import parameters
import copy
import random
import math


class EventuallySPPreprocessor:
    """
    functions:
    1. process the temporal information of 'eventually' operator in the form of phrase
       and assemble the ingredients into English expressions
    2. process the temporal information of 'eventually' operator in the form of clause
       and assemble the ingredients into English expressions
    3. refine the templates of Atom expressions and assemble them into English translations
    """

    def __init__(self, translate_guide, limit_num):
        self.instruction_dict = copy.deepcopy(translate_guide[0])
        self.tp_info_dict = copy.deepcopy(translate_guide[1])

        # extract information for temporal operator
        self.tp_index = self.tp_info_dict['index']
        category = self.tp_index[0]
        sub_category = self.tp_index[1]
        self.template = copy.deepcopy(TP_template.Eng_TP[category][sub_category])

        # extract information for simple phrase
        self.sp_info_dict = self.tp_info_dict['ingredient'][0]

        # Start Preprocessing

        # prepare adverbial modifiers and commands for later use
        self.adverbial_dict = self.adverbial_prepare()
        self.predicate_cmd_dict = self.command_process()

        # process the temporal information for 'eventually' in the form of phrase
        # and assemble them into English expressions
        [self.temporal_info_refined, self.eng_temporal_phrase] = self.temporal_phrase_process()

        # process the temporal information for 'eventually' in the form of clause
        # and assemble them into English expressions
        self.eng_temporal_clause = self.temporal_clause_process()

        if self.instruction_dict['nest_info_dict']['whetherBottom']:
            # refine the templates of Atom expressions and assemble them into English translations
            self.eng_main_sentence = self.main_sentence_process(limit_num)

    def adverbial_prepare(self):
        adv_refine_dict = copy.deepcopy(self.template['adverb'])

        adv_list = copy.deepcopy(self.template['adverb']['adverb'])
        adv_phrase_list = []  # only assemble adverbs, do not assemble phrases
        adv_assemble_list = [adv_list, adv_phrase_list]

        adverbial_dict = {
            'refine_dict': adv_refine_dict,
            'assemble_list': adv_assemble_list,
            'adv_general_list': adv_list
        }

        return adverbial_dict

    def command_process(self):
        adverb_dict = copy.deepcopy(self.adverbial_dict['refine_dict'])
        pre_cmd = PreCmdEventually(adverb_dict)

        position = self.instruction_dict['position']
        tense = self.instruction_dict['nest_info_dict']['tense']

        if tense == 'present':
            if position == 'before_imply':
                main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_after_imply)
            appositive_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_appositive)

        elif tense == 'future':
            if position == 'before_imply':
                main_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_after_imply)
            appositive_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_appositive)

        else:  # tense == 'past'
            if position == 'before_imply':
                main_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_after_imply)
            appositive_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_appositive)

        predicate_cmd_dict = {
            'main': main_cmd_dict,
            'appositive': appositive_cmd_dict
        }

        return predicate_cmd_dict

    def temporal_phrase_process(self):
        temporal_info_source = copy.deepcopy(self.template['temporal_phrase'])
        temporal_info_raw = []
        temporal_info_refined = []

        banned_words = ['next', 'following', 'subsequent', 'coming']
        for phrase in temporal_info_source:
            flag = 1
            for word in banned_words:
                if word in phrase:
                    flag = 0
            if flag == 1:
                temporal_info_raw.append(phrase)

        if self.tp_index == [0, 0]:  # eventually
            temporal_info_refined = temporal_info_raw

        elif self.tp_index == [0, 1]:  # eventually [0:t] (0 < t)
            t_value = self.tp_info_dict['ingredient'][1]
            for phrase in temporal_info_raw:
                phrase_modified = phrase.replace('t_value', t_value)
                temporal_info_refined.append(phrase_modified)

        else:  # eventually [a:b] (0 < a < b)
            t_value_a = self.tp_info_dict['ingredient'][1]
            t_value_b = self.tp_info_dict['ingredient'][2]
            for phrase in temporal_info_raw:
                phrase_modified = phrase.replace('t_value_a', t_value_a)
                phrase_modified = phrase_modified.replace('t_value_b', t_value_b)
                temporal_info_refined.append(phrase_modified)

        eng_temporal_phrase = self.random_temporal_phrase_assemble(temporal_info_refined)

        return [temporal_info_refined, eng_temporal_phrase]

    def random_temporal_phrase_assemble(self, temporal_info_refined):
        eng_temporal_phrase = []

        adv_list = copy.deepcopy(self.adverbial_dict['adv_general_list'])
        semantics_sometime = copy.deepcopy(self.template['semantics_sometime'])
        nest_info_dict = self.instruction_dict['nest_info_dict']

        for phrase_sometime in semantics_sometime:
            for phrase_temporal in temporal_info_refined:

                if nest_info_dict['whetherNest'] and nest_info_dict['nestLayer'] > 1:
                    if 'first' in phrase_temporal:
                        continue

                flag = random.randint(0, 1)
                if flag == 0:  # do not add adverb
                    phrase_at_sometime = 'at ' + phrase_sometime
                    eng = phrase_at_sometime + ' ' + phrase_temporal
                else:  # add adverb
                    adverb = random.choice(adv_list)
                    phrase_at_sometime = 'at ' + phrase_sometime
                    eng = adverb + ' ' + phrase_at_sometime + ' ' + phrase_temporal
                eng_temporal_phrase.append(eng)

        return eng_temporal_phrase

    def temporal_clause_process(self):
        new_template = dict()
        # subject
        new_template['subject'] = copy.deepcopy(self.template['clause']['subject'])
        # predicate
        new_template['predicate'] = copy.deepcopy(self.template['clause']['predicate'])
        # object
        object_ingredient = copy.deepcopy(self.template['clause']['object'])
        clause_object = []
        for ingredient in object_ingredient:
            for phrase in self.temporal_info_refined:
                obj = ingredient + ' ' + phrase
                clause_object.append(obj)
        new_template['object'] = clause_object
        # conjunction to link the following clause
        new_template['conjunction'] = ', at which'

        predicate_cmd_dict = copy.deepcopy(self.predicate_cmd_dict['main'])
        adverbial_list = copy.deepcopy(self.adverbial_dict['adv_general_list'])
        quick_refiner_assembler = EventuallyAtomQuickRefinerAssembler(new_template, predicate_cmd_dict, adverbial_list)
        # quick_refiner_assembler.display_assemble_guide()
        # quick_refiner_assembler.display_translation()
        self.eng_temporal_clause = quick_refiner_assembler.eng_list

        return self.eng_temporal_clause

    def main_sentence_process(self, limit_num):
        adverbial_query = self.instruction_dict['adverbial_query']
        adverbial_para = copy.deepcopy(self.adverbial_dict['assemble_list'])

        if self.tp_info_dict['type'][0] == 'original_TP_Atom':
            main_sentence_refiner = EventuallyAtomTemplateRefiner(self.sp_info_dict, self.predicate_cmd_dict)
            main_sentence_assembler = EventuallyAtomAssembler(adverbial_query, main_sentence_refiner.assemble_guide,
                                                              adverbial_para)
            # main_sentence_assembler.display_translation()
            self.eng_main_sentence = main_sentence_assembler.eng_list
        else:  # self.tp_info_dict['type'][0] == 'original_TP_BC_Atom':
            pkg_list = []
            # process atomic proposition A
            sp_info_dict_1 = self.tp_info_dict['ingredient'][0]['ingredient'][0]
            main_sentence_refiner = EventuallyAtomTemplateRefiner(sp_info_dict_1, self.predicate_cmd_dict)
            main_sentence_assembler = EventuallyAtomAssembler(adverbial_query, main_sentence_refiner.assemble_guide,
                                                              adverbial_para)
            eng_main_sentence_1 = main_sentence_assembler.eng_list
            pkg_list.append(eng_main_sentence_1)
            # process atomic proposition B
            sp_info_dict_2 = self.tp_info_dict['ingredient'][0]['ingredient'][1]
            main_sentence_refiner = EventuallyAtomTemplateRefiner(sp_info_dict_2, self.predicate_cmd_dict)
            main_sentence_assembler = EventuallyAtomAssembler(adverbial_query, main_sentence_refiner.assemble_guide,
                                                              adverbial_para)
            eng_main_sentence_2 = main_sentence_assembler.eng_list
            pkg_list.append(eng_main_sentence_2)

            self.eng_main_sentence = self.bc_atom_organize(pkg_list, limit_num)

        return self.eng_main_sentence

    def bc_atom_organize(self, pkg_list, limit_num):
        index = self.tp_info_dict['ingredient'][0]['index']
        eng_list = []

        if index == 0:   # 'A and B'
            if (len(pkg_list[0]) * len(pkg_list[1])) <= \
                    1 / parameters.union_operation_threshold_probability * limit_num:
                # use for loop
                for eng_a in pkg_list[0]:
                    for eng_b in pkg_list[1]:
                        point = random.randint(0, 1)
                        if point == 0:
                            eng = eng_a + ' and ' + eng_b
                        else:
                            eng = eng_a + ', and ' + eng_b
                        eng_list.append(eng)
            else:
                # use union operation
                eng_set = set()
                while len(eng_set) < math.ceil(limit_num):
                    eng_a = random.choice(pkg_list[0])
                    eng_b = random.choice(pkg_list[1])
                    point = random.randint(0, 1)
                    if point == 0:
                        eng = eng_a + ' and ' + eng_b
                    else:
                        eng = eng_a + ', and ' + eng_b
                    eng_set.add(eng)
                eng_list = sorted(eng_set)

        else:  # 'A or B'
            if (len(pkg_list[0]) * len(pkg_list[1])) <= \
                    1 / parameters.union_operation_threshold_probability * limit_num:
                # use for loop
                for eng_a in pkg_list[0]:
                    for eng_b in pkg_list[1]:
                        point = random.randint(0, 1)
                        if point == 0:
                            eng = eng_a + ' or ' + eng_b
                        else:
                            eng = eng_a + ', or ' + eng_b
                        eng_list.append(eng)
            else:
                # use union operation
                eng_set = set()
                while len(eng_set) < math.ceil(limit_num):
                    eng_a = random.choice(pkg_list[0])
                    eng_b = random.choice(pkg_list[1])
                    point = random.randint(0, 1)
                    if point == 0:
                        eng = eng_a + ' or ' + eng_b
                    else:
                        eng = eng_a + ', or ' + eng_b
                    eng_set.add(eng)
                eng_list = sorted(eng_set)

        random_eng_list = self.random_select_translation(eng_list, limit_num)

        return random_eng_list

    @staticmethod
    def random_select_translation(eng_list, limit_num):
        if len(eng_list) > limit_num:
            random_eng_list = random.sample(eng_list, limit_num)
        else:
            random_eng_list = eng_list

        return random_eng_list

    def display_key_list(self):
        count = 1
        for eng in self.eng_temporal_phrase:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

        count = 1
        for eng in self.eng_temporal_clause:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

        count = 1
        for eng in self.eng_main_sentence:
            print('%d: %s' % (count, eng))
            count = count + 1

    def pack_key_list(self):
        return [self.eng_temporal_phrase, self.eng_temporal_clause, self.eng_main_sentence]
