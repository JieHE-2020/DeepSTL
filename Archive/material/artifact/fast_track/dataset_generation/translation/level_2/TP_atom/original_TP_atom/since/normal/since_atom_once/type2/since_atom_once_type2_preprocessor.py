from template import TP_template
from commands.command_once import PreCmdOnce
from commands.command_since import PreCmdSince
from translation.level_2.TP_atom.original_TP_atom.since.normal.since_atom_once.type2.\
    since_atom_once_type2_quick_refiner_assembler import SinceAtomOnceType2QuickRefinerAssembler
from translation.level_2.TP_atom.original_TP_atom.since.normal.since_atom_once.type2.SP.\
    since_atom_once_type2_atom_template_refiner import SinceAtomOnceType2AtomTemplateRefiner
from translation.level_2.TP_atom.original_TP_atom.since.normal.since_atom_once.type2.SP.\
    since_atom_once_type2_atom_assembler import SinceAtomOnceType2AtomAssembler
import copy
import random


class SinceAtomOnceType2Preprocessor:
    """
    functions:
    1. process the temporal information of 'once' operator in the form of phrase, which will be
       added to a non-restrictive attributive clause during organization
    2. refine the templates of Atom expressions and assemble them into English translations
    3. process a non-restrictive attributive clause, which is used to express the temporal information
       of 'once' operator
    """

    def __init__(self, translate_guide):
        self.instruction_dict = copy.deepcopy(translate_guide[0])
        self.tp_info_dict = copy.deepcopy(translate_guide[1])

        # extract information for temporal operator
        self.tp_index = self.tp_info_dict['index']
        category = self.tp_index[0]
        sub_category = self.tp_index[1]
        self.once_template = copy.deepcopy(TP_template.Eng_TP[category][sub_category])
        self.since_template = copy.deepcopy(TP_template.Eng_TP[5][sub_category])

        # extract information for simple phrase
        self.sp_info_dict = self.tp_info_dict['ingredient'][0]

        # Start Preprocessing

        # prepare adverbial modifiers and commands for later use
        self.adverbial_dict = self.adverbial_prepare()
        self.predicate_cmd_dict_main = self.command_process_main()
        self.predicate_cmd_dict_clause = self.command_process_clause()

        # process temporal information
        self.temporal_info_refined = self.temporal_info_process()

        if self.instruction_dict['nest_info_dict']['whetherBottom']:
            # refine the templates of SP and assemble them into English expressions
            self.eng_main_sentence = self.main_sentence_process()

            # process a non-restrictive attributive clause, which is used to express
            # the temporal information of 'once' operator
            self.eng_attributive_clause = self.temporal_attributive_clause_process()

    def adverbial_prepare(self):
        adv_refine_dict = copy.deepcopy(self.once_template['adverb'])

        adv_list = copy.deepcopy(self.once_template['adverb']['adverb'])
        adv_phrase_list = []  # only assemble adverbs, do not assemble phrases
        adv_assemble_list = [adv_list, adv_phrase_list]

        adverbial_dict = {
            'refine_dict': adv_refine_dict,
            'assemble_list': adv_assemble_list,
            'adv_general_list': adv_list
        }

        return adverbial_dict

    def command_process_main(self):
        adverb_dict = copy.deepcopy(self.adverbial_dict['refine_dict'])
        pre_cmd = PreCmdOnce(adverb_dict)
        pre_cmd_since = PreCmdSince(adverb_dict)

        position = self.instruction_dict['position_main']
        tense = self.instruction_dict['nest_info_dict']['tense']

        if tense == 'present':
            flag = random.randint(1, 10)
            # from the perspective of present time
            if flag <= 2:  # choose with 20% probability
                if position == 'before_imply':
                    # without future tense
                    main_cmd_dict = copy.deepcopy(pre_cmd_since.once_present_cmd_dic_before_imply_present_version)
                else:  # position == 'after_imply'
                    main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_after_imply_present_version)
                appositive_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_appositive_present_version)

            # from the perspective of past time
            else:  # choose with 80% probability
                if position == 'before_imply':
                    # without future tense
                    main_cmd_dict = copy.deepcopy(pre_cmd_since.once_present_cmd_dic_before_imply_past_version)
                else:  # position == 'after_imply'
                    main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_after_imply_past_version)
                appositive_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_appositive_past_version)

        elif tense == 'future':
            if position == 'before_imply':
                # without future tense
                main_cmd_dict = copy.deepcopy(pre_cmd_since.once_future_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_after_imply)
            appositive_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_appositive)

        else:  # tense == 'past'
            if position == 'before_imply':
                # without future tense
                main_cmd_dict = copy.deepcopy(pre_cmd_since.once_past_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_after_imply)
            appositive_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_appositive)

        predicate_cmd_dict = {
            'main': main_cmd_dict,
            'appositive': appositive_cmd_dict
        }

        return predicate_cmd_dict

    def command_process_clause(self):
        adverb_dict = copy.deepcopy(self.adverbial_dict['refine_dict'])
        pre_cmd = PreCmdOnce(adverb_dict)

        position = self.instruction_dict['position_attributive_clause']
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

    def temporal_info_process(self):
        temporal_info_raw = copy.deepcopy(self.once_template['temporal_phrase'])
        temporal_info_refined = []

        if self.tp_index == [2, 0]:  # once
            temporal_info_refined = temporal_info_raw

        elif self.tp_index == [2, 1]:  # once [0:t] (0 < t)
            t_value = self.tp_info_dict['ingredient'][1]
            for phrase in temporal_info_raw:
                phrase_modified = phrase.replace('t_value', t_value)
                temporal_info_refined.append(phrase_modified)

        else:  # once [a:b] (0 < a < b)
            t_value_a = self.tp_info_dict['ingredient'][1]
            t_value_b = self.tp_info_dict['ingredient'][2]
            for phrase in temporal_info_raw:
                phrase_modified = phrase.replace('t_value_a', t_value_a)
                phrase_modified = phrase_modified.replace('t_value_b', t_value_b)
                temporal_info_refined.append(phrase_modified)

        return temporal_info_refined

    def main_sentence_process(self):
        main_sentence_refiner = SinceAtomOnceType2AtomTemplateRefiner(self.sp_info_dict, self.predicate_cmd_dict_main)

        adverbial_query = self.instruction_dict['adverbial_query']
        adverbial_para = copy.deepcopy(self.adverbial_dict['assemble_list'])
        main_sentence_assembler = \
            SinceAtomOnceType2AtomAssembler(adverbial_query, main_sentence_refiner.assemble_guide, adverbial_para)

        eng_main_sentence = main_sentence_assembler.eng_list

        return eng_main_sentence

    def temporal_attributive_clause_process(self):
        new_template = dict()
        # subject
        new_template['subject'] = copy.deepcopy(self.since_template['attributive_clause']['subject'])
        # predicate
        if self.sp_info_dict['type'] == 'SE':
            new_template['predicate'] = copy.deepcopy(self.since_template['attributive_clause']['predicate_se'])
        else:  # self.sp_info_dict['type'] == 'ERE'
            new_template['predicate'] = copy.deepcopy(self.since_template['attributive_clause']['predicate_ere'])
        # temporal adverbial
        temporal_adverbial_part_1 =\
            copy.deepcopy(self.since_template['attributive_clause']['temporal_adverbial_part_1'])
        temporal_adverbial = []
        for item in temporal_adverbial_part_1:
            for phrase in self.temporal_info_refined:
                adverbial = item + ' ' + phrase
                temporal_adverbial.append(adverbial)
        new_template['temporal_adverbial'] = temporal_adverbial

        predicate_cmd_dict = copy.deepcopy(self.predicate_cmd_dict_clause['main'])
        adverbial_list = copy.deepcopy(self.adverbial_dict['adv_general_list'])
        quick_refiner_assembler = \
            SinceAtomOnceType2QuickRefinerAssembler(new_template, predicate_cmd_dict, adverbial_list)

        eng_attributive_clause = quick_refiner_assembler.eng_list

        return eng_attributive_clause

    def display_key_list(self):
        count = 1
        for eng in self.eng_main_sentence:
            print('%d: %s' % (count, eng))
            count = count + 1

        count = 1
        for eng in self.eng_attributive_clause:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

    def pack_key_list(self):
        return [self.eng_main_sentence, self.eng_attributive_clause]
