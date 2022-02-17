from selection.level_3.NTP_atom.original_NTP_atom_selector import OriginalNTPAtomSelector
from translation.level_3.eventually_always.normal.eventually_always_atom_translator \
    import EventuallyAlwaysAtomTranslator
from public import parameters


class EventuallyAlwaysAtomHandler:

    def __init__(self, position, nest_info_dict, limit_num):
        self.position = position
        self.nest_info_dict = nest_info_dict
        # the number of randomly selected translations
        self.limit_num = limit_num

        # prepare materials for translation
        self.instruction_dict = self.instruction_assemble()
        self.ntp_info_dict = self.ntp_select()

        self.eventually_always_atom_translator = self.translate_process()

    def instruction_assemble(self):
        instruction_dict = {'position': self.position,
                            'adverbial_query_main_type1': 'adverbialEnabled',
                            'adverbial_query_main_type2_main_part': 'adverbialDisabled',
                            'nest_info_dict': self.nest_info_dict
                            }

        return instruction_dict

    @staticmethod
    def ntp_select():
        ntp_type = 'eventually_always'
        ntp_selector = OriginalNTPAtomSelector(ntp_type)
        ntp_info_dict = ntp_selector.ntp_info_dict

        return ntp_info_dict

    def translate_process(self):
        translate_guide = [self.instruction_dict, self.ntp_info_dict]
        eventually_always_atom_translator = EventuallyAlwaysAtomTranslator(translate_guide, self.limit_num)

        return eventually_always_atom_translator


# # information of position: two options
# # 1 - 'before_imply'
# # 2 - 'after_imply'
# position = 'after_imply'
#
# # information of nesting
# nest_info_dict = {
#     'whetherNest': True,
#     'nestLayer': 2,
#     'whetherBottom': True,
#     'hasParallelSuccessor': False,
#     'tense': 'future'
# }
#
# limit_num = parameters.limit_num_tp_atom_normal
# eventually_always_atom_handler = EventuallyAlwaysAtomHandler(position, nest_info_dict, limit_num)
# print(eventually_always_atom_handler.ntp_info_dict)
# print(eventually_always_atom_handler.ntp_info_dict['expression'])
# print('\n')
# eventually_always_atom_handler.eventually_always_atom_translator.display_random_translation()
