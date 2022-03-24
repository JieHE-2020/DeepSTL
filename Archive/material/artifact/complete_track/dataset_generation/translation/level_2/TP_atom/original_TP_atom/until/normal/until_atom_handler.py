from selection.level_2.TP_atom.original_TP_atom_selector import OriginalTPAtomSelector
from selection.level_2.TP_atom.TP_atom_until_since_separator import TPAtomUntilSinceSeparator
from translation.level_2.TP_atom.original_TP_atom.until.normal.until_atom_translator import UntilAtomTranslator
from public import parameters


class UntilAtomHandler:

    def __init__(self, position, nest_info_dict, limit_num):
        self.position = position
        self.nest_info_dict = nest_info_dict
        # the number of randomly selected translations
        self.limit_num = limit_num
        # the number of randomly selected translations for each translating type of 'eventually' operator
        self.eventually_limit_num = parameters.limit_num_tp_atom_until_since_second
        # for each kind of translations for 'eventually' operator, the number of randomly selected translations
        # from all possible translations of 'always' operator
        self.always_limit_num = parameters.limit_num_tp_atom_until_since_first

        # prepare translation instructions for different types of translating strategies
        self.instruction_dict = self.instruction_assemble()
        # get information of 'until' operator, from which information of
        # 'always' operator and 'eventually' operator is extracted respectively
        self.tp_info_dict = self.tp_select()

        # execute translation procedure
        self.until_atom_translator = self.until_atom_translate_process()

    def instruction_assemble(self):
        # instruction for 'always' operator
        always_instruction_dict = {
            'position': self.position,
            'adverbial_query_main_type1': 'adverbialEnabled',
            'adverbial_query_main_type2_main_part': 'adverbialDisabled',
            'nest_info_dict': self.nest_info_dict
        }

        # instruction for 'eventually' operator
        eventually_dict_type1 = {
            'position': 'before_imply',
            'adverbial_query': 'adverbialEnabled',
            'nest_info_dict': self.nest_info_dict
        }

        eventually_dict_type2 = {
            'position_main': 'before_imply',
            'position_attributive_clause': self.position,
            'adverbial_query': 'adverbialEnabled',
            'nest_info_dict': self.nest_info_dict
        }

        eventually_dict_type3 = {
            'position': self.position,
            'adverbial_query': 'adverbialEnabled',
            'nest_info_dict': self.nest_info_dict
        }

        eventually_instruction_dict = {
            'eventually_type1': eventually_dict_type1,
            'eventually_type2': eventually_dict_type2,
            'eventually_type3': eventually_dict_type3
        }

        instruction_dict = {
            'always': always_instruction_dict,
            'eventually': eventually_instruction_dict
        }

        return instruction_dict

    @staticmethod
    def tp_select():
        tp_type = 'until'
        tp_selector = OriginalTPAtomSelector(tp_type)
        until_info_dict = tp_selector.tp_info_dict
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

    def until_atom_translate_process(self):
        translate_guide = {
            'until_tp_info': self.tp_info_dict['until'],
            'always_tp_info': self.tp_info_dict['always'],
            'eventually_tp_info': self.tp_info_dict['eventually'],
            'always_instruction': self.instruction_dict['always'],
            'eventually_instruction': self.instruction_dict['eventually']
        }

        limit_num_dict = {
            'total': self.limit_num,
            'eventually_each_type': self.eventually_limit_num,
            'always_overall': self.always_limit_num
        }

        until_atom_translator = UntilAtomTranslator(translate_guide, limit_num_dict)

        return until_atom_translator


# information of position: two options
# 1 - 'before_imply'
# 2 - 'after_imply'
position = 'after_imply'

# information of nesting
nest_info_dict = {
    'whetherNest': False,
    'nestLayer': 1,
    'whetherBottom': True,
    'hasParallelSuccessor': False,
    'tense': 'present'
}
limit_num = parameters.limit_num_tp_atom_normal

# import time
# tic = time.time()
#
# for i in range(20):
#     until_atom_handler = UntilAtomHandler(position, nest_info_dict, limit_num)
#     print(until_atom_handler.tp_info_dict['until'])
#     print(until_atom_handler.tp_info_dict['until']['expression'])
#     print('\n')
#     print(until_atom_handler.tp_info_dict['always'])
#     print(until_atom_handler.tp_info_dict['always']['expression'])
#     print('\n')
#     print(until_atom_handler.tp_info_dict['eventually'])
#     print(until_atom_handler.tp_info_dict['eventually']['expression'])
#     print('\n')
#     until_atom_handler.until_atom_translator.display_random_translation()
#     print(i)
# toc = time.time()
# print(str((toc - tic)) + 's')
