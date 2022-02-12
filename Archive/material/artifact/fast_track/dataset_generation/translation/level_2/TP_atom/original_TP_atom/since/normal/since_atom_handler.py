from selection.level_2.TP_atom.original_TP_atom_selector import OriginalTPAtomSelector
from selection.level_2.TP_atom.TP_atom_until_since_separator import TPAtomUntilSinceSeparator
from translation.level_2.TP_atom.original_TP_atom.since.normal.since_atom_translator import SinceAtomTranslator
from public import parameters


class SinceAtomHandler:

    def __init__(self, position, nest_info_dict, limit_num):
        self.position = position
        self.nest_info_dict = nest_info_dict
        # the number of randomly selected translations
        self.limit_num = limit_num
        # the number of randomly selected translations for each translating type of 'once' operator
        self.once_limit_num = parameters.limit_num_tp_atom_until_since_second
        # for each kind of translations for 'once' operator, the number of randomly selected translations
        # from all possible translations of 'historically' operator
        self.historically_limit_num = parameters.limit_num_tp_atom_until_since_first

        # prepare translation instructions for different types of translating strategies
        self.instruction_dict = self.instruction_assemble()
        # get information of 'since' operator, from which information of
        # 'historically' operator and 'once' operator is extracted respectively
        self.tp_info_dict = self.tp_select()

        # execute translation procedure
        self.since_atom_translator = self.since_atom_translate_process()

    def instruction_assemble(self):
        # instruction for 'historically' operator
        historically_instruction_dict = {'position': self.position,
                                         'adverbial_query_main_type1': 'adverbialEnabled',
                                         'adverbial_query_main_type2_main_part': 'adverbialDisabled',
                                         'nest_info_dict': self.nest_info_dict
                                         }

        # instruction for 'once' operator
        once_dict_type1 = {
            'position': 'before_imply',
            'adverbial_query': 'adverbialEnabled',
            'nest_info_dict': self.nest_info_dict
        }

        once_dict_type2 = {
            'position_main': 'before_imply',
            'position_attributive_clause': self.position,
            'adverbial_query': 'adverbialEnabled',
            'nest_info_dict': self.nest_info_dict
        }

        once_dict_type3 = {
            'position': self.position,
            'adverbial_query': 'adverbialEnabled',
            'nest_info_dict': self.nest_info_dict
        }

        once_instruction_dict = {
            'once_type1': once_dict_type1,
            'once_type2': once_dict_type2,
            'once_type3': once_dict_type3
        }

        instruction_dict = {
            'historically': historically_instruction_dict,
            'once': once_instruction_dict
        }

        return instruction_dict

    @staticmethod
    def tp_select():
        tp_type = 'since'
        tp_selector = OriginalTPAtomSelector(tp_type)
        since_info_dict = tp_selector.tp_info_dict
        since_separator = TPAtomUntilSinceSeparator(since_info_dict)
        # separate the information dictionary of 'since' operator into
        # information dictionary of 'historically' operator and 'once' operator respectively
        historically_info_dict = since_separator.historically_info_dict
        once_info_dict = since_separator.once_info_dict

        tp_info_dict = {
            'since': since_info_dict,
            'historically': historically_info_dict,
            'once': once_info_dict
        }

        return tp_info_dict

    def since_atom_translate_process(self):
        translate_guide = {
            'since_tp_info': self.tp_info_dict['since'],
            'historically_tp_info': self.tp_info_dict['historically'],
            'once_tp_info': self.tp_info_dict['once'],
            'historically_instruction': self.instruction_dict['historically'],
            'once_instruction': self.instruction_dict['once']
        }

        limit_num_dict = {
            'total': self.limit_num,
            'once_each_type': self.once_limit_num,
            'historically_overall': self.historically_limit_num
        }

        since_atom_translator = SinceAtomTranslator(translate_guide, limit_num_dict)

        return since_atom_translator


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
#
# since_atom_handler = SinceAtomHandler(position, nest_info_dict, limit_num)
# print(since_atom_handler.tp_info_dict['since'])
# print(since_atom_handler.tp_info_dict['since']['expression'])
# print('\n')
# print(since_atom_handler.tp_info_dict['historically'])
# print(since_atom_handler.tp_info_dict['historically']['expression'])
# print('\n')
# print(since_atom_handler.tp_info_dict['once'])
# print(since_atom_handler.tp_info_dict['once']['expression'])
# print('\n')
# since_atom_handler.since_atom_translator.display_random_translation()
