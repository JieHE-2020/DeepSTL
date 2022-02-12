from translation.level_2.TP_atom.not_TP_atom.public_class.not_continuation_atom_process.\
    not_continuation_atom_translator import NotContinuationAtomTranslator
import copy


class DirectNegateAlwaysAtomHandler:

    def __init__(self, translate_guide, limit_num):
        self.translate_guide = copy.deepcopy(translate_guide)
        # extract information for 'always' operator
        self.tp_info_dict = copy.deepcopy(self.translate_guide['always_info_dict'])
        # the number of randomly selected translations
        self.limit_num = limit_num

        # prepare translation instructions
        self.instruction_dict = self.instruction_assemble()
        # execute translation procedure
        self.not_continuation_atom_translator = self.not_continuation_translate_process()

    def instruction_assemble(self):
        # instruction for 'always' operator
        instruction_dict = {'position': self.translate_guide['instruction_dict']['position'],
                            'adverbial_query_main_type1': 'adverbialEnabled',
                            'adverbial_query_main_type2_main_part': 'adverbialDisabled',
                            'nest_info_dict': self.translate_guide['instruction_dict']['nest_info_dict']
                            }

        return instruction_dict

    def not_continuation_translate_process(self):
        guide = [self.instruction_dict, self.tp_info_dict]
        not_continuation_atom_translator = NotContinuationAtomTranslator(guide, self.limit_num)

        return not_continuation_atom_translator
