from translation.level_1.atom.atom_handler import AtomHandler
from translation.level_1.BC_atom.BC_atom_handler import BCAtomHandler
import random


class SPScheduler:

    def __init__(self, position, type_preference, atom_type, limit_num):
        self.position = position
        # for ATOM
        self.type_preference = type_preference
        # for BC_ATOM
        self.atom_type = atom_type

        self.limit_num = limit_num

        # select type of simple phrase
        self.type_selected = self.type_select()

        # start generating simple phrase and its translations
        self.sp_expression = str()
        self.sp_translation = []
        self.signal_name_list = []
        self.expr_type_list = []
        self.sp_atom_distribute()

    @staticmethod
    def type_select():
        point = random.randint(1, 100)
        # point = 0  # only select 'ATOM'
        if point <= 75:
            type_selected = 'ATOM'
        else:
            type_selected = 'BC_ATOM'

        return type_selected

    def sp_atom_distribute(self):
        if self.type_selected == 'ATOM':
            self.atom_process()
        else:   # self.type_selected == 'BC_ATOM'
            self.bc_atom_process()

    def atom_process(self):
        atom_handler = AtomHandler(self.position, self.type_preference, self.limit_num)
        self.sp_expression = atom_handler.atom_info_dict['expression']
        self.sp_translation = atom_handler.atom_translator.random_selected_translations
        self.signal_name_list.\
            append(atom_handler.atom_info_dict['ingredient'][0])
        self.expr_type_list.\
            append(atom_handler.atom_info_dict['type'])

    def bc_atom_process(self):
        bc_atom_handler = BCAtomHandler(self.position, self.atom_type, self.limit_num)
        self.sp_expression = bc_atom_handler.bc_atom_info_dict['expression']
        self.sp_translation = bc_atom_handler.bc_atom_translator.random_selected_translations
        if bc_atom_handler.bc_atom_info_dict['index'] == 0 or bc_atom_handler.bc_atom_info_dict['index'] == 1:
            # 2 signals
            self.signal_name_list. \
                append(bc_atom_handler.bc_atom_info_dict['ingredient'][0]['ingredient'][0])
            self.expr_type_list. \
                append(bc_atom_handler.bc_atom_info_dict['ingredient'][0]['type'])
            self.signal_name_list. \
                append(bc_atom_handler.bc_atom_info_dict['ingredient'][1]['ingredient'][0])
            self.expr_type_list. \
                append(bc_atom_handler.bc_atom_info_dict['ingredient'][1]['type'])
        else:
            # 3 signals
            self.signal_name_list. \
                append(bc_atom_handler.bc_atom_info_dict['ingredient'][0]['ingredient'][0])
            self.expr_type_list. \
                append(bc_atom_handler.bc_atom_info_dict['ingredient'][0]['type'])
            self.signal_name_list. \
                append(bc_atom_handler.bc_atom_info_dict['ingredient'][1]['ingredient'][0])
            self.expr_type_list. \
                append(bc_atom_handler.bc_atom_info_dict['ingredient'][1]['type'])
            self.signal_name_list. \
                append(bc_atom_handler.bc_atom_info_dict['ingredient'][2]['ingredient'][0])
            self.expr_type_list. \
                append(bc_atom_handler.bc_atom_info_dict['ingredient'][2]['type'])
