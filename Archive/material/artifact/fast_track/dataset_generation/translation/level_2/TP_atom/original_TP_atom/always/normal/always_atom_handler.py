from selection.level_2.TP_atom.original_TP_atom_selector import OriginalTPAtomSelector
from translation.level_2.TP_atom.original_TP_atom.always.normal.always_atom_translator import AlwaysAtomTranslator
from public import parameters


class AlwaysAtomHandler:

    def __init__(self, position, nest_info_dict, limit_num):
        self.position = position
        self.nest_info_dict = nest_info_dict
        # the number of randomly selected translations
        self.limit_num = limit_num

        # prepare materials for translation
        self.instruction_dict = self.instruction_assemble()
        self.tp_info_dict = self.tp_select()

        self.always_atom_translator = self.translate_process()

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
        tp_selector = OriginalTPAtomSelector(tp_type)
        tp_info_dict = tp_selector.tp_info_dict

        return tp_info_dict

    def translate_process(self):
        translate_guide = [self.instruction_dict, self.tp_info_dict]
        always_atom_translator = AlwaysAtomTranslator(translate_guide, self.limit_num)

        return always_atom_translator


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
# always_atom_handler = AlwaysAtomHandler(position, nest_info_dict, limit_num)
# print(always_atom_handler.tp_info_dict['expression'])
# print('\n')
# always_atom_handler.always_atom_translator.display_random_translation()
