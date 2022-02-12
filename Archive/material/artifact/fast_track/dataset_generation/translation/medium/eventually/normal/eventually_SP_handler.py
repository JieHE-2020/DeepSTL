from selection.level_2.TP_atom.original_TP_atom_selector import OriginalTPAtomSelector
from selection.level_2.TP_BC_atom.original_TP_BC_atom_selector import OriginalTPBCAtomSelector
from translation.medium.eventually.normal.eventually_SP_translator \
    import EventuallySPTranslator
from public import parameters
import random


class EventuallySPHandler:

    def __init__(self, position, nest_info_dict, limit_num):
        self.position = position
        self.nest_info_dict = nest_info_dict
        # the number of randomly selected translations
        self.limit_num = limit_num

        # prepare materials for translation
        self.instruction_dict = self.instruction_assemble()
        self.tp_info_dict = self.tp_select()

        self.eventually_sp_translator = self.translate_process()

    def instruction_assemble(self):
        instruction_dict = {'position': self.position,
                            'adverbial_query': 'adverbialEnabled',
                            'nest_info_dict': self.nest_info_dict
                            }

        return instruction_dict

    @staticmethod
    def tp_select():
        tp_type = 'eventually'
        sp_type = random.randint(0, 1)
        if sp_type == 0:  # one atomic proposition
            tp_selector = OriginalTPAtomSelector(tp_type)
        else:  # boolean combination
            tp_selector = OriginalTPBCAtomSelector(tp_type)

        tp_info_dict = tp_selector.tp_info_dict

        return tp_info_dict

    def translate_process(self):
        translate_guide = [self.instruction_dict, self.tp_info_dict]
        eventually_sp_translator = EventuallySPTranslator(translate_guide, self.limit_num)

        return eventually_sp_translator


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
# limit_num = parameters.limit_num_tp_atom_normal
# eventually_atom_handler = EventuallySPHandler(position, nest_info_dict, limit_num)
# print(eventually_atom_handler.tp_info_dict)
# print(eventually_atom_handler.tp_info_dict['expression'])
# print('\n')
# eventually_atom_handler.eventually_sp_translator.display_random_translation()
