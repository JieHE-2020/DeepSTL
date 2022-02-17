from translation.level_2.TP_atom.original_TP_atom.once.simplest.simplest_once_atom_translator \
    import SimplestOnceAtomTranslator
import copy


class SimplestOnceAtomHandler:

    def __init__(self, material, limit_num):
        # extract information from material
        position = copy.deepcopy(material['position'])
        nest_info_dict = copy.deepcopy(material['nest_info_dict'])
        tp_info_dict = copy.deepcopy(material['tp_info_dict'])

        # the number of randomly selected translations
        self.limit_num = limit_num

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
        # get information of 'once' operator from class parameter
        self.tp_info_dict = copy.deepcopy(tp_info_dict)
        # the number of randomly selected translationWs
        self.limit_num = limit_num

        # execute translation procedure
        self.simplest_once_atom_translator = self.simplest_once_atom_translate_process()

    def instruction_assemble(self):
        # instruction for 'once' operator
        instruction_dict = {'position': self.position,
                            'adverbial_query': 'adverbialEnabled',
                            'nest_info_dict': self.nest_info_dict
                            }

        return instruction_dict

    def simplest_once_atom_translate_process(self):
        translate_guide = [self.instruction_dict, self.tp_info_dict]
        simplest_once_atom_translator = SimplestOnceAtomTranslator(translate_guide, self.limit_num)

        return simplest_once_atom_translator
