from grammar.level_2.TP_atom_BC_atom import original_TP_SP_rules
from selection.level_2.TP_atom.original_TP_atom_selector import OriginalTPAtomSelector
from selection.level_1.atom.atom_selector import AtomSelector
from selection.level_1.BC_atom.BC_atom_selector import BCAtomSelector
import random
import copy


class OriginalTPBCAtomSelector(OriginalTPAtomSelector):
    # This function overrides function tp_select in class OriginalTPAtomSelector
    def tp_select(self):
        # select category
        if self.tp_type == 'eventually':
            category = 0
        elif self.tp_type == 'always':
            category = 1
        elif self.tp_type == 'once':
            category = 2
        elif self.tp_type == 'historically':
            category = 3
        elif self.tp_type == 'until':
            category = 4
        elif self.tp_type == 'since':
            category = 5
        else:
            # randomly choose the category of TP
            category = random.randint(0, len(original_TP_SP_rules.TP) - 1)

        # randomly choose the sub_category of the chosen category (in a weighted manner)
        sum_list = []
        sum = 0.0

        for i in range(len(original_TP_SP_rules.TP[category])):
            sum = sum + original_TP_SP_rules.TP[category][i]['probability']
            sum_list.append(sum)

        # take category = 0 for example
        # sum_list = [0.2, 0.6, 1]
        # 0 <= point < sum_list[0]            =>  sub_category == 0
        # sum_list[0] <= point < sum_list[1]  =>  sub_category == 1
        # sum_list[1] <= point < sum_list[2]  =>  sub_category == 2
        point = random.random()
        sub_category = 0
        if 0 <= point < sum_list[0]:
            sub_category = 0
        else:
            for i in range(len(sum_list) - 1):
                # len(sum_list) - 1 = 3 - 1 = 2 => i = 0, 1
                if sum_list[i] <= point < sum_list[i + 1]:
                    sub_category = i + 1

        # extract grammar template of TP
        tp_info_dict = copy.deepcopy(original_TP_SP_rules.TP[category][sub_category])
        del tp_info_dict['probability']
        tp_info_dict['type'][0] = tp_info_dict['type'][0] + '_BC_Atom'

        self.tp_filling(tp_info_dict, category, sub_category)

    def tp_filling(self, tp_info_dict, category, sub_category):
        """
        the following part selects SP expressions
        # category == 0 => eventually
        # category == 1 => always
        # category == 2 => once
        # category == 3 => historically
        # category == 4 => until
        # category == 5 => since
        """
        if category == 0 or category == 2:  # for 'eventually' and 'once'
            bc_atom_selector = BCAtomSelector('random')
            bc_atom_info_dict = bc_atom_selector.bc_atom_info_dict
            self.tp_replacement_1(sub_category, tp_info_dict, bc_atom_info_dict)

        if category == 1 or category == 3:  # for 'always' and 'historically'
            bc_atom_selector = BCAtomSelector('SE')
            bc_atom_info_dict = bc_atom_selector.bc_atom_info_dict
            self.tp_replacement_1(sub_category, tp_info_dict, bc_atom_info_dict)

        if category == 4 or category == 5:  # for 'until' and 'since'
            # for clause 1
            select_clause1_type = random.randint(0, 1)
            if select_clause1_type == 0:  # select one single atomic proposition
                atom_type = 'SE'
                atom_selector_1 = AtomSelector(atom_type)
                sp_info_dict_1 = atom_selector_1.info_dict
            else:   # select boolean combination of atomic propositions
                bc_atom_selector_1 = BCAtomSelector('SE')
                sp_info_dict_1 = bc_atom_selector_1.bc_atom_info_dict

            # for clause 2
            if select_clause1_type == 0:
                # clause 1 has selected one single atomic proposition, then
                # clause 2 must choose boolean combination of atomic propositions
                bc_atom_selector_2 = BCAtomSelector('random')
                sp_info_dict_2 = bc_atom_selector_2.bc_atom_info_dict
            else:
                select_clause2_type = random.randint(0, 1)
                if select_clause2_type == 0:  # select one single atomic proposition
                    select_cmd = random.randint(0, 1)
                    if select_cmd == 0:
                        atom_type = 'SE'
                    else:
                        atom_type = 'ERE'
                    atom_selector_2 = AtomSelector(atom_type)
                    sp_info_dict_2 = atom_selector_2.info_dict
                else:  # select boolean combination of atomic propositions
                    bc_atom_selector_2 = BCAtomSelector('random')
                    sp_info_dict_2 = bc_atom_selector_2.bc_atom_info_dict

            self.tp_replacement_2(sub_category, tp_info_dict, sp_info_dict_1, sp_info_dict_2)


# for i in range(1000):
#     original_tp_bc_atom_selector = OriginalTPBCAtomSelector('random')
#     tp_bc_atom_info_dict = original_tp_bc_atom_selector.tp_info_dict
#     print(tp_bc_atom_info_dict)
#     print(i)

# original_tp_bc_atom_selector = OriginalTPBCAtomSelector('always')
# tp_bc_atom_info_dict = original_tp_bc_atom_selector.tp_info_dict
# print(tp_bc_atom_info_dict)
# print(tp_bc_atom_info_dict['expression'])
# print(tp_bc_atom_info_dict['ingredient'][0])
# print(tp_bc_atom_info_dict['ingredient'][0]['ingredient'][0])
# print(tp_bc_atom_info_dict['ingredient'][0]['ingredient'][1])