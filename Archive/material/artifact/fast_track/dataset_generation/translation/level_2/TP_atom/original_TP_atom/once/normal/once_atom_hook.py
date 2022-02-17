from translation.level_2.TP_atom.original_TP_atom.once.normal.once_atom_handler import OnceAtomHandler
import copy


class OnceAtomHook(OnceAtomHandler):

    def __init__(self, material, limit_num):
        # extract information from material
        tp_info_dict = copy.deepcopy(material['tp_info_dict'])
        position = copy.deepcopy(material['position'])
        nest_info_dict = copy.deepcopy(material['nest_info_dict'])

        # define embedded variables for temporary use
        embedded_position = 'before_imply'
        embedded_nest_info_dict = copy.deepcopy(nest_info_dict)
        # modify key 'tense' of self.embedded_nest_info_dict
        embedded_nest_info_dict['tense'] = 'present'

        # self.mode has two options: 1. 'embedded'; 2. 'parametric'
        self.mode = 'embedded'
        if self.mode == 'embedded':
            self.position = embedded_position
            self.nest_info_dict = embedded_nest_info_dict
        else:  # self.mode == 'parametric':
            self.position = position
            self.nest_info_dict = nest_info_dict

        self.tp_info_dict_adopted = tp_info_dict
        super().__init__(self.position, self.nest_info_dict, limit_num)

    def tp_select(self):
        return self.tp_info_dict_adopted
