from selection.level_3.NTP_atom.original_NTP_atom_selector import OriginalNTPAtomSelector
from translation.level_3.always_eventually.normal.always_eventually_atom_translator \
    import AlwaysEventuallyAtomTranslator
from public import parameters


class AlwaysEventuallyAtomHandler:

    def __init__(self, position, nest_info_dict, limit_num):
        self.position = position
        self.nest_info_dict = nest_info_dict
        # the number of randomly selected translations
        self.limit_num = limit_num

        # prepare materials for translation
        self.instruction_dict = self.instruction_assemble()
        self.ntp_info_dict = self.ntp_select()

        self.always_eventually_atom_translator = self.translate_process()

    def instruction_assemble(self):
        instruction_dict = {'position': self.position,
                            'adverbial_query': 'adverbialEnabled',
                            'nest_info_dict': self.nest_info_dict
                            }

        return instruction_dict

    @staticmethod
    def ntp_select():
        ntp_type = 'always_eventually'
        ntp_selector = OriginalNTPAtomSelector(ntp_type)
        ntp_info_dict = ntp_selector.ntp_info_dict

        return ntp_info_dict

    def translate_process(self):
        translate_guide = [self.instruction_dict, self.ntp_info_dict]
        always_eventually_atom_translator = AlwaysEventuallyAtomTranslator(translate_guide, self.limit_num)

        return always_eventually_atom_translator


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
# limit_num = parameters.limit_num_tp_atom_normal
# always_eventually_atom_handler = AlwaysEventuallyAtomHandler(position, nest_info_dict, limit_num)
# print(always_eventually_atom_handler.ntp_info_dict)
# print(always_eventually_atom_handler.ntp_info_dict['expression'])
# print('\n')
# always_eventually_atom_handler.always_eventually_atom_translator.display_random_translation()
