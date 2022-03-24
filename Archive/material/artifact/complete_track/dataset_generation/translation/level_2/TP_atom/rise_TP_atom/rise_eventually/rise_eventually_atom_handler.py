from selection.level_2.TP_atom.rise_TP_atom_selector import RiseTPAtomSelector
from selection.level_2.TP_atom.TP_atom_restorer import TPAtomRestorer
from translation.level_2.TP_atom.rise_TP_atom.public_class.rise_tp_atom_process.rise_tp_atom_translator \
    import RiseTPAtomTranslator


class RiseEventuallyAtomHandler:

    def __init__(self, position, nest_info_dict, limit_num=1000):
        self.position = position
        self.nest_info_dict = nest_info_dict
        # the number of randomly selected translations
        self.limit_num = limit_num
        # the number of randomly selected translations for 'eventually' operator
        # currently the number for simplest version and normal version is the same
        self.eventually_limit_num = 2000

        # prepare materials for translation
        self.rise_tp_info_dict = self.rise_tp_select()
        self.tp_info_dict = self.tp_restore()
        self.instruction_dict = self.instruction_assemble()

        self.rise_eventually_atom_translator = self.translate_process()

    @staticmethod
    def rise_tp_select():
        rise_tp_type = 'eventually'
        rise_tp_selector = RiseTPAtomSelector(rise_tp_type)
        rise_tp_info_dict = rise_tp_selector.rise_tp_info_dict

        return rise_tp_info_dict

    def tp_restore(self):
        tp_restorer = TPAtomRestorer(self.rise_tp_info_dict)
        tp_info_dict = tp_restorer.tp_info_dict

        return tp_info_dict

    def instruction_assemble(self):
        # 1. instruction for main sentence of both type 1 and type 2
        main_instruction_dict = {
            'position': self.position,
            'nest_info_dict': self.nest_info_dict
        }

        # 2. instruction for the simplest/normal translation version of 'eventually' operator
        eventually_instruction_dict = {
            'position': self.position,
            'nest_info_dict': self.nest_info_dict,
            'tp_info_dict': self.tp_info_dict
        }

        instruction_dict = {
            'main': main_instruction_dict,
            'eventually': eventually_instruction_dict
        }

        return instruction_dict

    def translate_process(self):
        translate_guide = {
            'tp_operator_type': 'eventually',
            'tp_operator_limit_num': self.eventually_limit_num,
            'tp_info_dict': self.tp_info_dict,
            'main_instruction': self.instruction_dict['main'],
            'original_tp_instruction': self.instruction_dict['eventually']
        }
        rise_eventually_atom_translator = RiseTPAtomTranslator(translate_guide, self.limit_num)

        return rise_eventually_atom_translator


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
# rise_eventually_atom_handler = RiseEventuallyAtomHandler(position, nest_info_dict)
# print(rise_eventually_atom_handler.rise_tp_info_dict)
# print(rise_eventually_atom_handler.rise_tp_info_dict['expression'])
# print(rise_eventually_atom_handler.tp_info_dict['expression'])
# print('\n')
# rise_eventually_atom_handler.rise_eventually_atom_translator.display_random_translation()
