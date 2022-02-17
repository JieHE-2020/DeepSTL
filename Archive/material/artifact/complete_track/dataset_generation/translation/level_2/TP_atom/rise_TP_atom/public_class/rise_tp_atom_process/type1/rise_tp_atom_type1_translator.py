from template import TP_template
from commands.command_templateTP import PreCmdTemplateTP
from translation.level_2.TP_atom.rise_TP_atom.public_class.rise_tp_atom_process. \
    type1.rise_tp_atom_type1_refiner_assembler import RiseTPAtomType1RefinerAssembler
import copy


class RiseTPAtomType1Translator:
    """
    functions:
    1. refine the translation template of main sentence and assemble it into English expressions
    2. get the simplest translation version for the temporal operator
    """

    def __init__(self, translate_guide):
        self.translate_guide = copy.deepcopy(translate_guide)
        self.main_instruction_dict = copy.deepcopy(translate_guide['main_instruction'])

        tp_operator_type = self.translate_guide['tp_operator_type']
        # extract information for 'eventually', 'always', 'once' or 'historically' operator
        if tp_operator_type == 'eventually' or tp_operator_type == 'always' or \
                tp_operator_type == 'once' or tp_operator_type == 'historically':
            tp_operator_info_dict = copy.deepcopy(self.translate_guide['tp_info_dict'])
            tp_operator_index = tp_operator_info_dict['index']
            category = tp_operator_index[0]
            sub_category = tp_operator_index[1]
            self.template = copy.deepcopy(TP_template.Eng_TP[category][sub_category])
        else:  # extract information for 'until' or 'since' operator
            tp_operator_info_dict = copy.deepcopy(self.translate_guide['tp_info_dict'][tp_operator_type])
            tp_operator_index = tp_operator_info_dict['index']
            category = tp_operator_index[0]
            sub_category = tp_operator_index[1]
            self.template = copy.deepcopy(TP_template.Eng_TP[category][sub_category])

        # Start Preprocessing

        # prepare adverbial modifiers and commands for later use
        self.adverbial_dict = self.adverbial_prepare()
        # commands used to operate predicates of the main sentence
        self.predicate_cmd_dict = self.command_process()

        # process main sentence
        self.eng_main_sentence = self.main_sentence_process()

    @staticmethod
    def adverbial_prepare():
        # temporally put all these data structures empty
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

    def command_process(self):
        adverb_dict = copy.deepcopy(self.adverbial_dict['refine_dict'])
        pre_cmd = PreCmdTemplateTP(adverb_dict)

        position = self.main_instruction_dict['position']
        tense = self.main_instruction_dict['nest_info_dict']['tense']

        if tense == 'present':
            if position == 'before_imply':
                main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_after_imply)

        elif tense == 'future':
            if position == 'before_imply':
                main_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_after_imply)

        else:  # tense == 'past'
            if position == 'before_imply':
                main_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_after_imply)

        predicate_cmd_dict = main_cmd_dict

        return predicate_cmd_dict

    def main_sentence_process(self):
        new_template = dict()
        # subject
        new_template['subject'] = copy.deepcopy(self.template['event_related']['subject_with_appositive'])
        # predicate
        new_template['predicate'] = copy.deepcopy(self.template['event_related']['predicate'])
        # object
        new_template['object'] = copy.deepcopy(self.template['event_related']['object_rise_related'])

        predicate_cmd_dict = copy.deepcopy(self.predicate_cmd_dict)
        adverbial_list = copy.deepcopy(self.adverbial_dict['adv_general_list'])
        type1_refiner_assembler = RiseTPAtomType1RefinerAssembler(new_template, predicate_cmd_dict,
                                                                  adverbial_list, self.translate_guide)
        eng_main_sentence_type_1 = type1_refiner_assembler.eng_list

        return eng_main_sentence_type_1
