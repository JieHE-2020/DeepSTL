from translation.level_2.TP_atom.original_TP_atom.since.simplest.simplest_since_atom_translator \
    import SimplestSinceAtomTranslator
import copy
from public import parameters


class SimplestSinceAtomHandler:

    def __init__(self, material, limit_num):
        # extract information from material
        position = copy.deepcopy(material['position'])
        nest_info_dict = copy.deepcopy(material['nest_info_dict'])
        tp_info_dict = copy.deepcopy(material['tp_info_dict'])

        # the number of randomly selected translations
        self.limit_num = limit_num
        # the number of randomly selected translations from all simplest translations for 'once' operator
        self.once_limit_num = parameters.limit_num_tp_atom_until_since_second
        # the number of randomly selected translations from all simplest translations for 'historically' operator
        self.historically_limit_num = parameters.limit_num_tp_atom_until_since_first

        # define embedded variables for temporary use
        embedded_position = 'before_imply'
        embedded_nest_info_dict = copy.deepcopy(nest_info_dict)
        # modify key 'tense' of embedded_nest_info_dict
        embedded_nest_info_dict['tense'] = 'present'

        # self.mode has two options: 1. 'embedded'; 2. 'parametric'
        self.mode = 'embedded'
        if self.mode == 'embedded':
            self.position = embedded_position
            self.nest_info_dict = embedded_nest_info_dict
        else:  # self.mode == 'parametric':
            self.position = position
            self.nest_info_dict = nest_info_dict

        # prepare translation instructions for different types of translating strategies
        self.instruction_dict = self.instruction_assemble()
        # get information of 'since' operator, 'historically' operator and 'once' operator from class parameter
        self.tp_info_dict = copy.deepcopy(tp_info_dict)
        # the number of selected translations
        self.limit_num = limit_num

        # execute translation procedure
        self.simplest_since_atom_translator = self.simplest_since_atom_translate_process()

    def instruction_assemble(self):
        # instruction for 'historically' operator
        historically_instruction_dict = {
            'position': self.position,
            'adverbial_query_main_type1': 'adverbialEnabled',
            'adverbial_query_main_type2_main_part': 'adverbialDisabled',
            'nest_info_dict': self.nest_info_dict
        }

        # instruction for 'once' operator
        once_instruction_dict = {
            'position': 'before_imply',
            'adverbial_query': 'adverbialEnabled',
            'nest_info_dict': self.nest_info_dict
        }

        instruction_dict = {
            'historically': historically_instruction_dict,
            'once': once_instruction_dict
        }

        return instruction_dict

    def simplest_since_atom_translate_process(self):
        translate_guide = {
            'historically_tp_info': self.tp_info_dict['historically'],
            'once_tp_info': self.tp_info_dict['once'],
            'historically_instruction': self.instruction_dict['historically'],
            'once_instruction': self.instruction_dict['once']
        }

        limit_num_dict = {
            'total': self.limit_num,
            'once': self.once_limit_num,
            'historically': self.historically_limit_num
        }

        simplest_since_atom_translator = SimplestSinceAtomTranslator(translate_guide, limit_num_dict)

        return simplest_since_atom_translator
