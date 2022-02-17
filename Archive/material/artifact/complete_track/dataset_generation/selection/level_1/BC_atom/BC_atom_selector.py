from grammar.level_1.BC_atom import BC_atom_rules
from selection.level_1.atom.atom_selector import AtomSelector
import random
import copy


class BCAtomSelector:
    def __init__(self, atom_type='random'):
        # only two options for atom_type: 'random', 'SE'
        self.atom_type = atom_type
        self.bc_atom_info_dict = dict()
        self.boolean_combination = True
        self.bc_atom_select()

    def bc_atom_select(self):
        # randomly choose the category of BC_Atom (in a weighted manner)
        sum_list = []
        sum = 0.0
        for i in range(len(BC_atom_rules.BC_Atom)):
            sum = sum + BC_atom_rules.BC_Atom[i]['probability']
            sum_list.append(sum)
        point = random.random()
        category = 0
        if 0 <= point < sum_list[0]:
            category = 0
        else:
            for i in range(len(sum_list) - 1):
                if sum_list[i] <= point < sum_list[i + 1]:
                    category = i + 1

        bc_atom_info_dict = copy.deepcopy(BC_atom_rules.BC_Atom[category])
        del bc_atom_info_dict['probability']

        sp_info_dict_list = []
        sig_name_list = []
        selection_finished = False
        if category == 0 or category == 1:  # needs 2 sp_info_dict

            while not selection_finished:
                if self.atom_type == 'random':
                    select_cmd = random.randint(1, 10)
                    if select_cmd <= 8:  # with 80% probability
                        atom_type_chosen = 'SE'
                    else:
                        atom_type_chosen = 'ERE'
                else:  # self.atom_type == 'SE'
                    atom_type_chosen = 'SE'

                atom_selector = AtomSelector(atom_type_chosen, self.boolean_combination)
                new_atom_info_dict = atom_selector.info_dict

                if new_atom_info_dict['ingredient'][0] not in sig_name_list:
                    sig_name_list.append(new_atom_info_dict['ingredient'][0])
                    sp_info_dict_list.append(new_atom_info_dict)

                if len(sp_info_dict_list) == 2:
                    selection_finished = True

            self.bc_atom_replacement(bc_atom_info_dict, sp_info_dict_list, 2)

        else:  # category == 2 or category == 3, needs 3 sp_info_dict

            while not selection_finished:
                if self.atom_type == 'random':
                    select_cmd = random.randint(0, 4)
                    if select_cmd <= 3:
                        atom_type_chosen = 'SE'
                    else:
                        atom_type_chosen = 'ERE'
                else:  # self.atom_type == 'SE'
                    atom_type_chosen = 'SE'

                atom_selector = AtomSelector(atom_type_chosen, self.boolean_combination)
                new_atom_info_dict = atom_selector.info_dict

                if new_atom_info_dict['ingredient'][0] not in sig_name_list:
                    sig_name_list.append(new_atom_info_dict['ingredient'][0])
                    sp_info_dict_list.append(new_atom_info_dict)

                if len(sp_info_dict_list) == 3:
                    selection_finished = True

            self.bc_atom_replacement(bc_atom_info_dict, sp_info_dict_list, 3)

    def bc_atom_replacement(self, bc_atom_info_dict, sp_info_dict_list, expr_num):
        for i in range(expr_num):
            # key 'ingredient'
            bc_atom_info_dict['ingredient'][i] = sp_info_dict_list[i]
            # key 'expression'
            num_str = str(i+1)
            string_replaced = 'SP_expr_' + num_str
            if sp_info_dict_list[i]['type'] == 'SE' and sp_info_dict_list[i]['index'][0] == 3 and \
                    sp_info_dict_list[i]['index'][1] <= 3:  # 'sig >=/> value1 and sig <=/< value2
                bc_atom_info_dict['expression'] = \
                    bc_atom_info_dict['expression'].replace(string_replaced, '('+sp_info_dict_list[i]['expression']+')')
            else:
                bc_atom_info_dict['expression'] = \
                    bc_atom_info_dict['expression'].replace(string_replaced, sp_info_dict_list[i]['expression'])

        self.bc_atom_info_dict = bc_atom_info_dict


# for i in range(1000):
#     bc_atom_selector = BCAtomSelector('random')
#     bc_atom_info_dict = bc_atom_selector.bc_atom_info_dict
#     print(bc_atom_info_dict)
#     print(i)
