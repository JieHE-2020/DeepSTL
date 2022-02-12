from selection.level_2.TP_atom.original_TP_atom_selector import OriginalTPAtomSelector
from translation.level_2.TP_atom.original_TP_atom.historically.normal.historically_atom_translator \
    import HistoricallyAtomTranslator
from public import parameters


class HistoricallyAtomHandler:

    def __init__(self, position, nest_info_dict, limit_num):
        self.position = position
        self.nest_info_dict = nest_info_dict
        # the number of randomly selected translations
        self.limit_num = limit_num

        # prepare materials for translation
        self.instruction_dict = self.instruction_assemble()
        self.tp_info_dict = self.tp_select()
        # the following two are for testing
        # self.tp_info_dict = {'type': ['original_TP_Atom', 'historically'], 'index': [3, 2], 'ingredient': [{'type': 'SE', 'index': [2, 7], 'ingredient': ['V_DEN', '25.3'], 'expression': 'not fall (V_DEN < 25.3)'}, '3', '9'], 'expression': 'historically [3:9] (not fall (V_DEN < 25.3))'}
        # self.tp_info_dict = {'type': ['original_TP_Atom', 'historically'], 'index': [3, 1], 'ingredient': [{'type': 'SE', 'index': [2, 4], 'ingredient': ['V_Sply', '36'], 'expression': 'not rise (V_Sply <= 36)'}, '3'], 'expression': 'historically [0:3] (not rise (V_Sply <= 36))'}

        self.historically_atom_translator = self.translate_process()

    def instruction_assemble(self):
        instruction_dict = {'position': self.position,
                            'adverbial_query_main_type1': 'adverbialEnabled',
                            'adverbial_query_main_type2_main_part': 'adverbialDisabled',
                            'nest_info_dict': self.nest_info_dict
                            }

        return instruction_dict

    @staticmethod
    def tp_select():
        tp_type = 'historically'
        tp_selector = OriginalTPAtomSelector(tp_type)
        tp_info_dict = tp_selector.tp_info_dict

        return tp_info_dict

    def translate_process(self):
        translate_guide = [self.instruction_dict, self.tp_info_dict]
        historically_atom_translator = HistoricallyAtomTranslator(translate_guide, self.limit_num)

        return historically_atom_translator


# for i in range(100):
#     # information of position: two options
#     # 1 - 'before_imply'
#     # 2 - 'after_imply'
#     position = 'after_imply'
#
#     # information of nesting
#     nest_info_dict = {
#         'whetherNest': False,
#         'nestLayer': 1,
#         'whetherBottom': True,
#         'hasParallelSuccessor': False,
#         'tense': 'present'
#     }
#     limit_num = parameters.limit_num_tp_atom_normal
#     historically_atom_handler = HistoricallyAtomHandler(position, nest_info_dict, limit_num)
#     print(historically_atom_handler.tp_info_dict)
#     print(historically_atom_handler.tp_info_dict['expression'])
#     print('\n')
#     historically_atom_handler.historically_atom_translator.display_random_translation()
#     print(i)
