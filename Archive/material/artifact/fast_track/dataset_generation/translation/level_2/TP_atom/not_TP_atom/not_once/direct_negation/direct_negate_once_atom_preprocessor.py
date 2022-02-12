from template import TP_template
from commands.command_historically import PreCmdHistorically
from commands.command_once import PreCmdOnce
from translation.level_2.TP_atom.not_TP_atom.not_once.direct_negation.SP. \
    direct_negate_once_atom_type1_atom_template_refiner import DirectNegateOnceAtomType1AtomTemplateRefiner
from translation.level_2.TP_atom.not_TP_atom.not_once.direct_negation.SP. \
    direct_negate_once_atom_type1_atom_assembler import DirectNegateOnceAtomType1AtomAssembler
from translation.level_2.TP_atom.not_TP_atom.not_once.direct_negation. \
    direct_negate_once_atom_quick_refiner_assembler import DirectNegateOnceAtomQuickRefinerAssembler
from translation.level_2.TP_atom.original_TP_atom.once.normal.SP.once_atom_template_refiner \
    import OnceAtomTemplateRefiner
from translation.level_2.TP_atom.original_TP_atom.once.normal.SP.once_atom_assembler \
    import OnceAtomAssembler
import copy
import random


class DirectNegateOnceAtomPreprocessor:
    """
    functions:
    Take translating 'not once [0:2] (x>1)' as an example
    1. Negation on original translation 1 (main sentence guided) for 'once' operator:
    Method: Use type 1 translating style of 'historically' operator but use temporal information of 'once' operator
            plus meaning of 'at/for anytime'
    a. Deal with main sentence:
    · Use 'historically_not_info_dict' of historically [0:2] (not (x>1))
    · Use 'historically' command to assemble main sentence with only negative mood.
      The position is equal to self.instruction_dict['position'].
    · No other adverbs or adverbial phrases
    b. Deal with temporal information:
    · Temporal information should start with phrase group with meaning of 'at/for anytime', which needs to use
      template of restored 'once_info_dict' of once [0:2] (x>1)

    2. Negation on original translation 2 ('there be' structure guided) for 'once' operator:
    Method: Use translating style of 'once' operator and use temporal information of 'once' operator
            plus meaning of 'at/for anytime'
    a. Deal with English expressions:
    · Use restored 'once_info_dict' of once [0:2] (x>1)
    · Use 'once' command to assemble ‘there be’ structure with negative mood.
      The position is equal to self.instruction_dict['position'].
    · Use 'once' command to assemble main sentence.
      However, the position should be deliberately set as 'before_imply'.
    · No other adverbs or adverbial phrases
    b. Deal with temporal information:
    · Temporal information should start with phrase group with meaning of ‘at/for anytime’, which needs to use
      template of restored once_info_dict of once [0:2] (x>1)
    """

    def __init__(self, translate_guide):
        self.instruction_dict = copy.deepcopy(translate_guide['instruction_dict'])
        self.historically_not_info_dict = copy.deepcopy(translate_guide['historically_not_info_dict'])
        self.once_info_dict = copy.deepcopy(translate_guide['once_info_dict'])

        # extract information for the restored 'once' operator
        self.tp_index = self.once_info_dict['index']
        category = self.tp_index[0]
        sub_category = self.tp_index[1]
        self.template = copy.deepcopy(TP_template.Eng_TP[category][sub_category])

        # extract information for simple phrase
        self.once_sp_info_dict = self.once_info_dict['ingredient'][0]
        self.historically_not_sp_info_dict = self.historically_not_info_dict['ingredient'][0]

        # Start Preprocessing

        # prepare adverbial modifiers and commands for later use
        self.adverbial_dict = self.adverbial_prepare()  # keep the value of every key empty
        self.historically_not_predicate_cmd_dict = self.historically_not_command_process()
        self.once_there_be_predicate_cmd_dict = self.once_there_be_command_process()
        self.once_main_predicate_cmd_dict = self.once_main_command_process()

        # process the temporal information for 'once' in the form of phrase
        # and assemble them into English expressions
        # note that this temporal information should start with phrase group with meaning of 'at/for anytime'
        [self.temporal_info_refined, self.eng_temporal_phrase] = self.temporal_phrase_process()

        # Negation on original translation 1 - deal with main sentence
        self.eng_main_sentence_type_1 = self.main_sentence_type_1_process()

        # Negation on original translation 2 - deal with English expressions
        # process 'there be' structure
        self.eng_temporal_clause = self.temporal_clause_process()
        # process main sentence
        self.eng_main_sentence_type_2 = self.main_sentence_type_2_process()

    @staticmethod
    def adverbial_prepare():
        adv_refine_dict = {}

        adv_list = []
        adv_phrase_list = []
        adv_assemble_list = [adv_list, adv_phrase_list]

        adverbial_dict = {
            'refine_dict': adv_refine_dict,
            'assemble_list': adv_assemble_list,
            'adv_general_list': adv_list
        }

        return adverbial_dict

    def historically_not_command_process(self):
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

    def once_there_be_command_process(self):
        adverb_dict = copy.deepcopy(self.adverbial_dict['refine_dict'])
        pre_cmd = PreCmdOnce(adverb_dict)

        position = self.instruction_dict['position']
        tense = self.instruction_dict['nest_info_dict']['tense']

        if tense == 'present':
            flag = random.randint(1, 10)
            # from the perspective of present time
            if flag <= 2:  # choose with 20% probability
                if position == 'before_imply':
                    main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_before_imply_present_version)
                else:  # position == 'after_imply'
                    main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_after_imply_present_version)
                appositive_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_appositive_present_version)

            # from the perspective of past time
            else:  # choose with 80% probability
                if position == 'before_imply':
                    main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_before_imply_past_version)
                else:  # position == 'after_imply'
                    main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_after_imply_past_version)
                appositive_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_appositive_past_version)

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

    def once_main_command_process(self):
        adverb_dict = copy.deepcopy(self.adverbial_dict['refine_dict'])
        pre_cmd = PreCmdOnce(adverb_dict)

        # position should be deliberately set as 'before_imply'
        position = 'before_imply'
        tense = self.instruction_dict['nest_info_dict']['tense']

        if tense == 'present':
            flag = random.randint(1, 10)
            # from the perspective of present time
            if flag <= 2:  # choose with 20% probability
                if position == 'before_imply':
                    main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_before_imply_present_version)
                else:  # position == 'after_imply'
                    main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_after_imply_present_version)
                appositive_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_appositive_present_version)

            # from the perspective of past time
            else:  # choose with 80% probability
                if position == 'before_imply':
                    main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_before_imply_past_version)
                else:  # position == 'after_imply'
                    main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_after_imply_past_version)
                appositive_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_appositive_past_version)

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
        temporal_info_raw = copy.deepcopy(self.template['temporal_phrase'])
        temporal_info_refined = []

        if self.tp_index == [2, 0]:  # once
            temporal_info_refined = temporal_info_raw

        elif self.tp_index == [2, 1]:  # once [0:t] (0 < t)
            t_value = self.once_info_dict['ingredient'][1]
            for phrase in temporal_info_raw:
                phrase_modified = phrase.replace('t_value', t_value)
                temporal_info_refined.append(phrase_modified)

        else:  # once [a:b] (0 < a < b)
            t_value_a = self.once_info_dict['ingredient'][1]
            t_value_b = self.once_info_dict['ingredient'][2]
            for phrase in temporal_info_raw:
                phrase_modified = phrase.replace('t_value_a', t_value_a)
                phrase_modified = phrase_modified.replace('t_value_b', t_value_b)
                temporal_info_refined.append(phrase_modified)

        eng_temporal_phrase = self.random_temporal_phrase_assemble(temporal_info_refined)

        return [temporal_info_refined, eng_temporal_phrase]

    def random_temporal_phrase_assemble(self, temporal_info_refined):
        eng_temporal_phrase = []

        semantics_anytime = copy.deepcopy(self.template['semantics_anytime'])
        nest_info_dict = self.instruction_dict['nest_info_dict']

        for phrase_anytime in semantics_anytime:
            for phrase_temporal in temporal_info_refined:

                if nest_info_dict['whetherNest'] and nest_info_dict['nestLayer'] > 1:
                    if 'first' in phrase_temporal:
                        continue

                phrase_at_anytime = 'at ' + phrase_anytime
                eng = phrase_at_anytime + ' ' + phrase_temporal
                eng_temporal_phrase.append(eng)

                phrase_for_anytime = 'for ' + phrase_anytime
                eng = phrase_for_anytime + ' ' + phrase_temporal
                eng_temporal_phrase.append(eng)

        return eng_temporal_phrase

    def main_sentence_type_1_process(self):
        predicate_cmd_dict = self.historically_not_predicate_cmd_dict['main_type1']
        # only used for clause whose mood is 'negative'
        main_sentence_refiner = \
            DirectNegateOnceAtomType1AtomTemplateRefiner(self.historically_not_sp_info_dict, predicate_cmd_dict)

        adverbial_query = 'adverbialDisabled'
        adverbial_para = copy.deepcopy(self.adverbial_dict['assemble_list'])
        main_sentence_assembler = \
            DirectNegateOnceAtomType1AtomAssembler(adverbial_query, main_sentence_refiner.assemble_guide,
                                                   adverbial_para)

        return main_sentence_assembler.eng_list

    def temporal_clause_process(self):
        new_template = dict()
        # subject
        new_template['subject'] = copy.deepcopy(self.template['clause']['subject'])
        # predicate
        new_template['predicate'] = copy.deepcopy(self.template['clause']['predicate'])
        # object
        # note that do not use self.template['clause']['object'] because it has the semantics of 'sometime'
        object_ingredient = copy.deepcopy(self.template['semantics_anytime'])
        clause_object = []
        for ingredient in object_ingredient:
            for phrase in self.temporal_info_refined:
                obj = ingredient + ' ' + phrase
                clause_object.append(obj)
        new_template['object'] = clause_object
        # conjunction to link the following clause
        new_template['conjunction'] = ', at which'

        predicate_cmd_dict = copy.deepcopy(self.once_there_be_predicate_cmd_dict['main'])
        adverbial_list = copy.deepcopy(self.adverbial_dict['adv_general_list'])
        quick_refiner_assembler \
            = DirectNegateOnceAtomQuickRefinerAssembler(new_template, predicate_cmd_dict, adverbial_list)
        self.eng_temporal_clause = quick_refiner_assembler.eng_list

        return self.eng_temporal_clause

    def main_sentence_type_2_process(self):
        main_sentence_refiner = \
            OnceAtomTemplateRefiner(self.once_sp_info_dict, self.once_main_predicate_cmd_dict)

        adverbial_query = 'adverbialDisabled'
        adverbial_para = copy.deepcopy(self.adverbial_dict['assemble_list'])
        main_sentence_assembler = OnceAtomAssembler(adverbial_query, main_sentence_refiner.assemble_guide,
                                                    adverbial_para)

        return main_sentence_assembler.eng_list

    def display_key_list(self):
        count = 1
        for eng in self.eng_temporal_phrase:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

        count = 1
        for eng in self.eng_main_sentence_type_1:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

        count = 1
        for eng in self.eng_temporal_clause:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

        count = 1
        for eng in self.eng_main_sentence_type_2:
            print('%d: %s' % (count, eng))
            count = count + 1

    def pack_key_list(self):
        return [self.eng_temporal_phrase,
                self.eng_main_sentence_type_1,
                self.eng_temporal_clause,
                self.eng_main_sentence_type_2]
