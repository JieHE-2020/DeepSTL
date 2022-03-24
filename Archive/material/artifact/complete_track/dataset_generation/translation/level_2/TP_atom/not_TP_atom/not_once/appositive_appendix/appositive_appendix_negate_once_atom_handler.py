from translation.level_2.TP_atom.not_TP_atom.public_class.not_tp_atom_process.not_tp_atom_translator \
    import NotTPAtomTranslator
import copy
from public import parameters


class AppositiveAppendixNegateOnceAtomHandler:

    def __init__(self, translate_guide, limit_num):
        self.translate_guide = copy.deepcopy(translate_guide)
        # the number of randomly selected translations
        self.limit_num = limit_num
        # the number of randomly selected translations for 'once' operator
        # currently the number for simplest version and normal version is the same
        self.once_limit_num = self.limit_num * parameters.tp_atom_factor_simplest_normal

        self.instruction_dict = self.instruction_assemble()

        self.appositive_appendix_negate_once_atom_translator = self.translate_process()

    def instruction_assemble(self):
        # 1. instruction for main sentence of both type 1 and type 2
        main_instruction_dict = self.translate_guide['instruction_dict']

        # 2. instruction for the simplest/normal translation version of 'once' operator
        once_instruction_dict = {
            'position': self.translate_guide['instruction_dict']['position'],
            'nest_info_dict': self.translate_guide['instruction_dict']['nest_info_dict'],
            'tp_info_dict': self.translate_guide['once_info_dict']
        }

        instruction_dict = {
            'main': main_instruction_dict,
            'once': once_instruction_dict
        }

        return instruction_dict

    def translate_process(self):
        guide = {
            'tp_operator_type': 'once',
            'tp_operator_limit_num': self.once_limit_num,
            'tp_info_dict': self.translate_guide['once_info_dict'],
            'main_instruction': self.instruction_dict['main'],
            'original_tp_instruction': self.instruction_dict['once']
        }
        appositive_appendix_negate_once_atom_translator = NotTPAtomTranslator(guide, self.limit_num)

        return appositive_appendix_negate_once_atom_translator

