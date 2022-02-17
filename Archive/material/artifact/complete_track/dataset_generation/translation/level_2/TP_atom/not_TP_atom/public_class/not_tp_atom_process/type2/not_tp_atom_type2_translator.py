from translation.level_2.TP_atom.not_TP_atom.public_class.not_tp_atom_process.type1.not_tp_atom_type1_translator \
    import NotTPAtomType1Translator
from translation.level_2.TP_atom.not_TP_atom.public_class.not_tp_atom_process.type2.not_tp_atom_type2_refiner_assembler \
    import NotTPAtomType2RefinerAssembler
import copy


class NotTPAtomType2Translator(NotTPAtomType1Translator):
    """
    functions:
    1. refine the translation template of main sentence and assemble it into English expressions
    2. get the normal translation version for the temporal operator
    """

    def main_sentence_process(self):
        new_template = dict()
        # subject
        new_template['subject'] = copy.deepcopy(self.template['negation']['subject_without_appositive'])
        # predicate
        new_template['predicate'] = copy.deepcopy(self.template['negation']['predicate'])
        # object
        new_template['object'] = copy.deepcopy(self.template['negation']['object'])

        predicate_cmd_dict = copy.deepcopy(self.predicate_cmd_dict)
        adverbial_list = copy.deepcopy(self.adverbial_dict['adv_general_list'])
        type2_refiner_assembler = NotTPAtomType2RefinerAssembler(new_template, predicate_cmd_dict,
                                                                 adverbial_list, self.translate_guide)
        eng_main_sentence_type_2 = type2_refiner_assembler.eng_list

        return eng_main_sentence_type_2
