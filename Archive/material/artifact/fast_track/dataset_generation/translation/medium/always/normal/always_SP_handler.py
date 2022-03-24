from selection.level_2.TP_atom.original_TP_atom_selector import OriginalTPAtomSelector
from selection.level_2.TP_BC_atom.original_TP_BC_atom_selector import OriginalTPBCAtomSelector
from translation.medium.always.normal.always_SP_translator import AlwaysSPTranslator
from public import parameters
import random


class AlwaysSPHandler:

    def __init__(self, position, nest_info_dict, limit_num):
        self.position = position
        self.nest_info_dict = nest_info_dict
        # the number of randomly selected translations
        self.limit_num = limit_num

        # prepare materials for translation
        self.instruction_dict = self.instruction_assemble()
        self.tp_info_dict = self.tp_select()
        # print(self.tp_info_dict)

        self.always_sp_translator = self.translate_process()

    def instruction_assemble(self):
        instruction_dict = {'position': self.position,
                            'adverbial_query_main_type1': 'adverbialEnabled',
                            'adverbial_query_main_type2_main_part': 'adverbialDisabled',
                            'nest_info_dict': self.nest_info_dict
                            }

        return instruction_dict

    @staticmethod
    def tp_select():
        tp_type = 'always'
        sp_type = random.randint(0, 1)
        if sp_type == 0:  # one atomic proposition
            tp_selector = OriginalTPAtomSelector(tp_type)
        else:  # boolean combination
            tp_selector = OriginalTPBCAtomSelector(tp_type)
        tp_info_dict = tp_selector.tp_info_dict

        # tp_info_dict = {'type': ['original_TP_BC_Atom', 'always'], 'index': [1, 2], 'ingredient': [{'type': ['BC_Atom', 'A or B'], 'index': 1, 'ingredient': [{'type': 'SE', 'index': [3, 2], 'ingredient': ['r x Z K', '9954.6', '9971.123'], 'expression': 'r x Z K >= 9954.6 and r x Z K < 9971.123'}, {'type': 'SE', 'index': [3, 8], 'ingredient': ['Q _ b J x E f I h p', '7392', '8229'], 'expression': 'not rise (Q _ b J x E f I h p >= 7392 and Q _ b J x E f I h p <= 8229)'}], 'expression': '(r x Z K >= 9954.6 and r x Z K < 9971.123) or not rise (Q _ b J x E f I h p >= 7392 and Q _ b J x E f I h p <= 8229)'}, '4845', '7416'], 'expression': 'always [4845:7416] ((r x Z K >= 9954.6 and r x Z K < 9971.123) or not rise (Q _ b J x E f I h p >= 7392 and Q _ b J x E f I h p <= 8229))'}

        return tp_info_dict

    def translate_process(self):
        translate_guide = [self.instruction_dict, self.tp_info_dict]
        always_sp_translator = AlwaysSPTranslator(translate_guide, self.limit_num)

        return always_sp_translator


# # information of position: two options
# # 1 - 'before_imply'
# # 2 - 'after_imply'
# position = 'after_imply'
#
# # information of nesting
# nest_info_dict = {
#     'whetherNest': False,
#     'nestLayer': 1,
#     'whetherBottom': True,
#     'hasParallelSuccessor': False,
#     'tense': 'present'
# }
#
# limit_num = parameters.limit_num_tp_atom_normal
# always_sp_handler = AlwaysSPHandler(position, nest_info_dict, limit_num)
# print(always_sp_handler.tp_info_dict)
# print(always_sp_handler.tp_info_dict['expression'])
# print('\n')
# always_sp_handler.always_sp_translator.display_random_translation()
