from template import TP_template
from commands.command_historically import PreCmdHistorically
from translation.level_2.TP_atom.original_TP_atom.historically.simplest.SP.simplest_historically_atom_template_refiner\
    import SimplestHistoricallyAtomTemplateRefiner
from translation.level_2.TP_atom.original_TP_atom.historically.normal.SP.historically_atom_assembler \
    import HistoricallyAtomAssembler
import copy


class SimplestHistoricallyAtomPreprocessor:
    """
    functions:
    1. process the temporal information for 'historically' in the form of phrase
       and assemble them into English expressions
    2. process main sentences of type 1:
       refine the templates of SP and assemble them into English expressions
    """

    def __init__(self, translate_guide, whether_from_not_once=False):
        self.instruction_dict = copy.deepcopy(translate_guide[0])
        self.tp_info_dict = copy.deepcopy(translate_guide[1])
        self.whether_from_not_once = whether_from_not_once

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

        # process the temporal information for 'historically' (in the form of phrase)
        # and assemble them into English expressions
        self.eng_temporal_phrase = self.temporal_phrase_process()

        # refine the templates of SP and assemble them into English expressions
        self.eng_main_sentence_type1 = self.main_sentence_type1_process()

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
        pre_cmd = PreCmdHistorically(adverb_dict)

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
        temporal_info_raw = copy.deepcopy(self.template['temporal_phrase'])
        eng_temporal_phrase = []
        nest_info_dict = self.instruction_dict['nest_info_dict']

        if self.tp_index == [3, 0]:  # historically
            eng_temporal_phrase = temporal_info_raw

        elif self.tp_index == [3, 1]:  # historically [0:t] (0 < t)
            t_value = self.tp_info_dict['ingredient'][1]
            for phrase in temporal_info_raw:
                if nest_info_dict['whetherNest'] and nest_info_dict['nestLayer'] > 1:
                    if 'first' in phrase:
                        continue
                phrase_modified = phrase.replace('t_value', t_value)
                eng_temporal_phrase.append(phrase_modified)

        else:  # historically [a:b] (0 < a < b)
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

    def main_sentence_type1_process(self):
        predicate_cmd_dict = self.predicate_cmd_dict['main_type1']
        positive_predicate_version = 'alwaysUseDuration'
        main_sentence_refiner = SimplestHistoricallyAtomTemplateRefiner(self.sp_info_dict, predicate_cmd_dict,
                                                                        positive_predicate_version,
                                                                        self.whether_from_not_once)

        adverbial_query = self.instruction_dict['adverbial_query_main_type1']
        adverbial_para = copy.deepcopy(self.adverbial_dict['assemble_list'])
        main_sentence_assembler = HistoricallyAtomAssembler(adverbial_query, main_sentence_refiner.assemble_guide,
                                                            adverbial_para)

        return main_sentence_assembler.eng_list

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
