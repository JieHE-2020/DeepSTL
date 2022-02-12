from grammar.level_2.TP_atom_BC_atom import rise_TP_SP_rules
from selection.level_2.TP_atom.original_TP_atom_selector import OriginalTPAtomSelector
import random
import copy


class RiseTPAtomSelector(OriginalTPAtomSelector):
    def __init__(self, tp_type='random'):
        super().__init__(tp_type)
        self.rise_tp_info_dict = self.tp_info_dict

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
            category = random.randint(0, len(rise_TP_SP_rules.rise_TP) - 1)

        # randomly choose the sub_category of the chosen category (in a weighted manner)
        sum_list = []
        sum = 0.0

        for i in range(len(rise_TP_SP_rules.rise_TP[category])):
            sum = sum + rise_TP_SP_rules.rise_TP[category][i]['probability']
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
        tp_info_dict = copy.deepcopy(rise_TP_SP_rules.rise_TP[category][sub_category])
        del tp_info_dict['probability']
        tp_info_dict['type'][0] = tp_info_dict['type'][0] + '_Atom'

        self.tp_filling(tp_info_dict, category, sub_category)


# rise_tp_atom_selector = RiseTPAtomSelector('random')
# print(rise_tp_atom_selector.rise_tp_info_dict)
