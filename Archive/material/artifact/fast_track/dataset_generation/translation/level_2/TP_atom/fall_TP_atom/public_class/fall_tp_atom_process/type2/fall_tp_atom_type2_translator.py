from translation.level_2.TP_atom.fall_TP_atom.public_class.fall_tp_atom_process.type1.fall_tp_atom_type1_translator \
    import FallTPAtomType1Translator
from translation.level_2.TP_atom.fall_TP_atom.public_class.fall_tp_atom_process.type2.fall_tp_atom_type2_refiner_assembler \
    import FallTPAtomType2RefinerAssembler
import copy


class FallTPAtomType2Translator(FallTPAtomType1Translator):
    """
    functions:
    1. refine the translation template of main sentence and assemble it into English expressions
    2. get the normal translation version for the temporal operator
    """

    def main_sentence_process(self):
        new_template = dict()
        # subject
        new_template['subject'] = copy.deepcopy(self.template['event_related']['subject_without_appositive'])
        # predicate
        new_template['predicate'] = copy.deepcopy(self.template['event_related']['predicate'])
        # object
        new_template['object'] = copy.deepcopy(self.template['event_related']['object_fall_related'])

        predicate_cmd_dict = copy.deepcopy(self.predicate_cmd_dict)
        adverbial_list = copy.deepcopy(self.adverbial_dict['adv_general_list'])
        type2_refiner_assembler = FallTPAtomType2RefinerAssembler(new_template, predicate_cmd_dict,
                                                                  adverbial_list, self.translate_guide)
        eng_main_sentence_type_2 = type2_refiner_assembler.eng_list

        return eng_main_sentence_type_2
