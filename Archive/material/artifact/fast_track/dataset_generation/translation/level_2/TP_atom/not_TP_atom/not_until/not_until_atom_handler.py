from selection.level_2.TP_atom.not_TP_atom_selector import NotTPAtomSelector
from selection.level_2.TP_atom.TP_atom_restorer import TPAtomRestorer
from selection.level_2.TP_atom.TP_atom_until_since_separator import TPAtomUntilSinceSeparator
from translation.level_2.TP_atom.not_TP_atom.public_class.not_tp_atom_process.not_tp_atom_translator \
    import NotTPAtomTranslator
from public import parameters


class NotUntilAtomHandler:

    def __init__(self, position, nest_info_dict, limit_num):
        self.position = position
        self.nest_info_dict = nest_info_dict
        # the number of randomly selected translations
        self.limit_num = limit_num
        # the number of randomly selected translations for 'until' operator
        # currently the number for simplest version and normal version is the same
        self.until_limit_num = parameters.limit_num_tp_atom_simplest_normal

        # prepare materials for translation
        self.not_tp_info_dict = self.not_tp_select()
        self.tp_info_dict = self.tp_restore()
        self.instruction_dict = self.instruction_assemble()

        self.not_until_atom_translator = self.translate_process()

    @staticmethod
    def not_tp_select():
        not_tp_type = 'until'
        not_tp_selector = NotTPAtomSelector(not_tp_type)
        not_tp_info_dict = not_tp_selector.not_tp_info_dict

        return not_tp_info_dict

    def tp_restore(self):
        tp_restorer = TPAtomRestorer(self.not_tp_info_dict)
        until_info_dict = tp_restorer.tp_info_dict
        until_separator = TPAtomUntilSinceSeparator(until_info_dict)
        # separate the information dictionary of 'until' operator into
        # information dictionary of 'always' operator and 'eventually' operator respectively
        always_info_dict = until_separator.always_info_dict
        eventually_info_dict = until_separator.eventually_info_dict

        tp_info_dict = {
            'until': until_info_dict,
            'always': always_info_dict,
            'eventually': eventually_info_dict
        }

        return tp_info_dict

    def instruction_assemble(self):
        # 1. instruction for main sentence of both type 1 and type 2
        main_instruction_dict = {
            'position': self.position,
            'nest_info_dict': self.nest_info_dict
        }

        # 2. instruction for the simplest/normal translation version of 'until' operator
        until_instruction_dict = {
            'position': self.position,
            'nest_info_dict': self.nest_info_dict,
            'tp_info_dict': self.tp_info_dict
        }

        instruction_dict = {
            'main': main_instruction_dict,
            'until': until_instruction_dict
        }

        return instruction_dict

    def translate_process(self):
        translate_guide = {
            'tp_operator_type': 'until',
            'tp_operator_limit_num': self.until_limit_num,
            'tp_info_dict': self.tp_info_dict,
            'main_instruction': self.instruction_dict['main'],
            'original_tp_instruction': self.instruction_dict['until']
        }
        not_until_atom_translator = NotTPAtomTranslator(translate_guide, self.limit_num)

        return not_until_atom_translator


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
# not_until_atom_handler = NotUntilAtomHandler(position, nest_info_dict, limit_num)
# print(not_until_atom_handler.not_tp_info_dict)
# print(not_until_atom_handler.not_tp_info_dict['expression'])
# print(not_until_atom_handler.tp_info_dict['until']['expression'])
# print('\n')
# not_until_atom_handler.not_until_atom_translator.display_random_translation()
