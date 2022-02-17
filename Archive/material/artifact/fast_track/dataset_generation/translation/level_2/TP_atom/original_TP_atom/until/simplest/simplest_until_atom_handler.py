from translation.level_2.TP_atom.original_TP_atom.until.simplest.simplest_until_atom_translator \
    import SimplestUntilAtomTranslator
import copy
from public import parameters


class SimplestUntilAtomHandler:

    def __init__(self, material, limit_num):
        # extract information from material
        position = copy.deepcopy(material['position'])
        nest_info_dict = copy.deepcopy(material['nest_info_dict'])
        tp_info_dict = copy.deepcopy(material['tp_info_dict'])

        # the number of randomly selected translations
        self.limit_num = limit_num
        # the number of randomly selected translations from all simplest translations for 'eventually' operator
        self.eventually_limit_num = parameters.limit_num_tp_atom_until_since_second
        # the number of randomly selected translations from all simplest translations for 'always' operator
        self.always_limit_num = parameters.limit_num_tp_atom_until_since_first

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
        # get information of 'until' operator, 'always' operator and 'eventually' operator from class parameter
        self.tp_info_dict = copy.deepcopy(tp_info_dict)

        # execute translation procedure
        self.simplest_until_atom_translator = self.simplest_until_atom_translate_process()

    def instruction_assemble(self):
        # instruction for 'always' operator
        always_instruction_dict = {
            'position': self.position,
            'adverbial_query_main_type1': 'adverbialEnabled',
            'adverbial_query_main_type2_main_part': 'adverbialDisabled',
            'nest_info_dict': self.nest_info_dict
        }

        # instruction for 'eventually' operator
        eventually_instruction_dict = {
            'position': 'before_imply',
            'adverbial_query': 'adverbialEnabled',
            'nest_info_dict': self.nest_info_dict
        }

        instruction_dict = {
            'always': always_instruction_dict,
            'eventually': eventually_instruction_dict
        }

        return instruction_dict

    def simplest_until_atom_translate_process(self):
        translate_guide = {
            'always_tp_info': self.tp_info_dict['always'],
            'eventually_tp_info': self.tp_info_dict['eventually'],
            'always_instruction': self.instruction_dict['always'],
            'eventually_instruction': self.instruction_dict['eventually']
        }

        limit_num_dict = {
            'total': self.limit_num,
            'eventually': self.eventually_limit_num,
            'always': self.always_limit_num
        }

        simplest_until_atom_translator = SimplestUntilAtomTranslator(translate_guide, limit_num_dict)

        return simplest_until_atom_translator
