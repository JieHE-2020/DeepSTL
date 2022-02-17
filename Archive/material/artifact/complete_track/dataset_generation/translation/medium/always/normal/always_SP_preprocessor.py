from template import TP_template
from commands.command_always import PreCmdAlways
from translation.level_2.TP_atom.original_TP_atom.always.normal.SP.always_atom_template_refiner \
    import AlwaysAtomTemplateRefiner
from translation.level_2.TP_atom.original_TP_atom.always.normal.SP.always_atom_assembler \
    import AlwaysAtomAssembler
from public import parameters
import math
import copy
import random


class AlwaysSPPreprocessor:
    """
    functions:
    1. process the temporal information of 'always' operator in the form of phrase
       and assemble them into English expressions
    2. process main sentences of type 1:
       refine the templates of SP and assemble them into English expressions
    """

    def __init__(self, translate_guide, limit_num, whether_from_not_eventually=False):
        self.instruction_dict = copy.deepcopy(translate_guide[0])
        self.tp_info_dict = copy.deepcopy(translate_guide[1])
        self.whether_from_not_eventually = whether_from_not_eventually

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

        # process the temporal information for 'always' (in the form of phrase)
        # and assemble them into English expressions
        self.eng_temporal_phrase = self.temporal_phrase_process()

        if self.instruction_dict['nest_info_dict']['whetherBottom']:
            # process main sentences of type 1
            # refine the templates of SP and assemble them into English expressions
            self.eng_main_sentence_type1 = self.main_sentence_type1_process(limit_num)

        # print('preprocess done')

    def adverbial_prepare(self):
        adv_refine_dict = copy.deepcopy(copy.deepcopy(self.template['adverb_refine']))

        adv_list = copy.deepcopy(self.template['adverb_assemble']['adverb'])
        adv_phrase_list = copy.deepcopy(self.template['adverbial_phrase_assemble']['adverbial_phrase'])
        adv_assemble_list = [adv_list, adv_phrase_list]

        adverbial_dict = {
            'refine_dict': adv_refine_dict,
            'assemble_list': adv_assemble_list
        }

        return adverbial_dict

    def command_process(self):
        adverb_dict = copy.deepcopy(self.adverbial_dict['refine_dict'])
        pre_cmd = PreCmdAlways(adverb_dict)

        position = self.instruction_dict['position']
        tense = self.instruction_dict['nest_info_dict']['tense']

        if tense == 'present':
            if position == 'before_imply':
                main_type1_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_before_imply_main_type1_cmd_dict)
                main_type1_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_before_imply_main_type1_appositive_cmd_dict)

                main_type2_main_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_before_imply_main_type2_main_part_cmd_dict)
                main_type2_main_part_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_before_imply_main_type2_main_part_appositive_cmd_dict)

                main_type2_clause_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_before_imply_main_type2_clause_part_cmd_dict)

            else:  # position == 'after_imply'
                main_type1_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_after_imply_main_type1_cmd_dict)
                main_type1_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_after_imply_main_type1_appositive_cmd_dict)

                main_type2_main_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_after_imply_main_type2_main_part_cmd_dict)
                main_type2_main_part_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_after_imply_main_type2_main_part_appositive_cmd_dict)

                main_type2_clause_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_after_imply_main_type2_clause_part_cmd_dict)

        elif tense == 'future':
            if position == 'before_imply':
                main_type1_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_before_imply_main_type1_cmd_dict)
                main_type1_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_before_imply_main_type1_appositive_cmd_dict)

                main_type2_main_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_before_imply_main_type2_main_part_cmd_dict)
                main_type2_main_part_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_before_imply_main_type2_main_part_appositive_cmd_dict)

                main_type2_clause_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_before_imply_main_type2_clause_part_cmd_dict)

            else:  # position == 'after_imply'
                main_type1_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_after_imply_main_type1_cmd_dict)
                main_type1_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_after_imply_main_type1_appositive_cmd_dict)

                main_type2_main_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_after_imply_main_type2_main_part_cmd_dict)
                main_type2_main_part_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_after_imply_main_type2_main_part_appositive_cmd_dict)

                main_type2_clause_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_after_imply_main_type2_clause_part_cmd_dict)

        else:  # tense == 'past'
            if position == 'before_imply':
                main_type1_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_before_imply_main_type1_cmd_dict)
                main_type1_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_before_imply_main_type1_appositive_cmd_dict)

                main_type2_main_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_before_imply_main_type2_main_part_cmd_dict)
                main_type2_main_part_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_before_imply_main_type2_main_part_appositive_cmd_dict)

                main_type2_clause_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_before_imply_main_type2_clause_part_cmd_dict)

            else:  # position == 'after_imply'
                main_type1_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_after_imply_main_type1_cmd_dict)
                main_type1_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_after_imply_main_type1_appositive_cmd_dict)

                main_type2_main_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_after_imply_main_type2_main_part_cmd_dict)
                main_type2_main_part_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_after_imply_main_type2_main_part_appositive_cmd_dict)

                main_type2_clause_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_after_imply_main_type2_clause_part_cmd_dict)

        main_type1 = {
            'main': main_type1_cmd_dict,
            'appositive': main_type1_appositive_cmd_dict
        }

        main_type2_main_part = {
            'main': main_type2_main_part_cmd_dict,
            'appositive': main_type2_main_part_appositive_cmd_dict
        }

        predicate_cmd_dict = {
            'main_type1': main_type1,
            'main_type2_main_part': main_type2_main_part,
            'main_type2_clause_part': main_type2_clause_part_cmd_dict
        }

        return predicate_cmd_dict

    def temporal_phrase_process(self):
        temporal_info_source = copy.deepcopy(self.template['temporal_phrase'])
        temporal_info_raw = []
        eng_temporal_phrase = []
        nest_info_dict = self.instruction_dict['nest_info_dict']

        banned_words = ['next', 'following', 'subsequent', 'coming']
        for phrase in temporal_info_source:
            flag = 1
            for word in banned_words:
                if word in phrase:
                    flag = 0
            if flag == 1:
                temporal_info_raw.append(phrase)

        if self.tp_index == [1, 0]:  # always
            eng_temporal_phrase = temporal_info_raw

        elif self.tp_index == [1, 1]:  # always [0:t] (0 < t)
            t_value = self.tp_info_dict['ingredient'][1]
            for phrase in temporal_info_raw:

                if nest_info_dict['whetherNest'] and nest_info_dict['nestLayer'] > 1:
                    if 'first' in phrase:
                        continue
                phrase_modified = phrase.replace('t_value', t_value)
                eng_temporal_phrase.append(phrase_modified)

        else:  # always [a:b] (0 < a < b)
            t_value_a = self.tp_info_dict['ingredient'][1]
            t_value_b = self.tp_info_dict['ingredient'][2]
            for phrase in temporal_info_raw:
                if nest_info_dict['whetherNest'] and nest_info_dict['nestLayer'] > 1:
                    if 'first' in phrase:
                        continue
                phrase_modified = phrase.replace('t_value_a', t_value_a)
                phrase_modified = phrase_modified.replace('t_value_b', t_value_b)
                eng_temporal_phrase.append(phrase_modified)

        return eng_temporal_phrase

    def main_sentence_type1_process(self, limit_num):
        predicate_cmd_dict = self.predicate_cmd_dict['main_type1']
        positive_predicate_version = 'alwaysUseDuration'
        adverbial_query = self.instruction_dict['adverbial_query_main_type1']
        adverbial_para = copy.deepcopy(self.adverbial_dict['assemble_list'])
        if self.tp_info_dict['type'][0] == 'original_TP_Atom':
            main_sentence_refiner = AlwaysAtomTemplateRefiner(self.sp_info_dict, predicate_cmd_dict,
                                                              positive_predicate_version)
            main_sentence_assembler = AlwaysAtomAssembler(adverbial_query, main_sentence_refiner.assemble_guide,
                                                          adverbial_para)
            eng_main_sentence = main_sentence_assembler.eng_list
        else:  # self.tp_info_dict['type'][0] == 'original_TP_BC_Atom':
            pkg_list = []
            # process atomic proposition A
            # print('eng_main_sentence_1 begin')
            sp_info_dict_1 = self.tp_info_dict['ingredient'][0]['ingredient'][0]
            main_sentence_refiner = AlwaysAtomTemplateRefiner(sp_info_dict_1, predicate_cmd_dict,
                                                              positive_predicate_version)
            main_sentence_assembler = AlwaysAtomAssembler(adverbial_query, main_sentence_refiner.assemble_guide,
                                                          adverbial_para)
            eng_main_sentence_1 = main_sentence_assembler.eng_list
            pkg_list.append(eng_main_sentence_1)
            # process atomic proposition B
            # print('eng_main_sentence_2 begin')
            sp_info_dict_2 = self.tp_info_dict['ingredient'][0]['ingredient'][1]
            main_sentence_refiner = AlwaysAtomTemplateRefiner(sp_info_dict_2, predicate_cmd_dict,
                                                              positive_predicate_version)
            main_sentence_assembler = AlwaysAtomAssembler(adverbial_query, main_sentence_refiner.assemble_guide,
                                                          adverbial_para)
            eng_main_sentence_2 = main_sentence_assembler.eng_list
            pkg_list.append(eng_main_sentence_2)
            # print('eng_main_sentence_2 done')

            eng_main_sentence = self.bc_atom_organize(pkg_list, limit_num)

        return eng_main_sentence

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
        for eng in self.eng_main_sentence_type1:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

    def pack_key_list(self):
        return [self.eng_temporal_phrase,
                self.eng_main_sentence_type1]
