from grammar.level_2.TP_atom_BC_atom import original_TP_SP_rules
from selection.level_1.atom.atom_selector import AtomSelector
from corpus import number_generate
import random
import copy


class OriginalTPAtomSelector:
    def __init__(self, tp_type='random'):
        self.tp_info_dict = dict()
        self.tp_type = tp_type
        self.tp_select()

    # This function uses class AtomSelector
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
        tp_info_dict['type'][0] = tp_info_dict['type'][0] + '_Atom'

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
            select_cmd = random.randint(1, 100)
            if select_cmd <= 75:
                atom_type = 'SE'
            else:
                atom_type = 'ERE'
            atom_selector = AtomSelector(atom_type)
            sp_info_dict = atom_selector.info_dict
            self.tp_replacement_1(sub_category, tp_info_dict, sp_info_dict)

        if category == 1 or category == 3:  # for 'always' and 'historically'
            atom_type = 'SE'
            atom_selector = AtomSelector(atom_type)
            sp_info_dict = atom_selector.info_dict
            self.tp_replacement_1(sub_category, tp_info_dict, sp_info_dict)

        if category == 4 or category == 5:  # for 'until' and 'since'
            atom_type = 'SE'
            atom_selector_1 = AtomSelector(atom_type)
            sp_info_dict_1 = atom_selector_1.info_dict

            select_cmd = random.randint(1, 100)
            if select_cmd <= 75:
                atom_type = 'SE'
            else:
                atom_type = 'ERE'
            atom_selector_2 = AtomSelector(atom_type)
            sp_info_dict_2 = atom_selector_2.info_dict
            self.tp_replacement_2(sub_category, tp_info_dict, sp_info_dict_1, sp_info_dict_2)

    def tp_replacement_1(self, sub_category, tp_info_dict, sp_info_dict):
        tp_info_dict['ingredient'][0] = sp_info_dict
        sp_expr = sp_info_dict['expression']
        if sub_category == 0:
            tp_info_dict['expression'] = tp_info_dict['expression'].replace('SP_expr', sp_expr)
        if sub_category == 1:
            t_value = self.t_value_find()
            tp_info_dict['ingredient'][1] = str(t_value)
            tp_info_dict['expression'] = tp_info_dict['expression'].replace('t_value', tp_info_dict['ingredient'][1])
            tp_info_dict['expression'] = tp_info_dict['expression'].replace('SP_expr', sp_expr)
        if sub_category == 2:
            [t_value_a, t_value_b] = self.t_value_range_find()
            tp_info_dict['ingredient'][1] = str(t_value_a)
            tp_info_dict['ingredient'][2] = str(t_value_b)
            tp_info_dict['expression'] = tp_info_dict['expression'].replace('t_value_a', tp_info_dict['ingredient'][1])
            tp_info_dict['expression'] = tp_info_dict['expression'].replace('t_value_b', tp_info_dict['ingredient'][2])
            tp_info_dict['expression'] = tp_info_dict['expression'].replace('SP_expr', sp_expr)

        self.tp_info_dict = tp_info_dict

    def tp_replacement_2(self, sub_category, tp_info_dict, sp_info_dict_1, sp_info_dict_2):
        tp_info_dict['ingredient'][0] = sp_info_dict_1
        tp_info_dict['ingredient'][1] = sp_info_dict_2

        sp_expr_1 = sp_info_dict_1['expression']
        sp_expr_2 = sp_info_dict_2['expression']

        if sub_category == 0:
            tp_info_dict['expression'] = tp_info_dict['expression'].replace('SP_expr_1', sp_expr_1)
            tp_info_dict['expression'] = tp_info_dict['expression'].replace('SP_expr_2', sp_expr_2)
        if sub_category == 1:
            t_value = self.t_value_find()
            tp_info_dict['ingredient'][2] = str(t_value)
            tp_info_dict['expression'] = tp_info_dict['expression'].replace('t_value', tp_info_dict['ingredient'][2])
            tp_info_dict['expression'] = tp_info_dict['expression'].replace('SP_expr_1', sp_expr_1)
            tp_info_dict['expression'] = tp_info_dict['expression'].replace('SP_expr_2', sp_expr_2)
        if sub_category == 2:
            [t_value_a, t_value_b] = self.t_value_range_find()
            tp_info_dict['ingredient'][2] = str(t_value_a)
            tp_info_dict['ingredient'][3] = str(t_value_b)
            tp_info_dict['expression'] = tp_info_dict['expression'].replace('t_value_a', tp_info_dict['ingredient'][2])
            tp_info_dict['expression'] = tp_info_dict['expression'].replace('t_value_b', tp_info_dict['ingredient'][3])
            tp_info_dict['expression'] = tp_info_dict['expression'].replace('SP_expr_1', sp_expr_1)
            tp_info_dict['expression'] = tp_info_dict['expression'].replace('SP_expr_2', sp_expr_2)

        self.tp_info_dict = tp_info_dict

    @ staticmethod
    def t_value_find():
        # flag = random.randint(0, 1)
        #
        # if flag == 0:  # generate integer number
        #     value = random.randint(1, 10000)
        # else:  # generate decimal number
        #     value = random.uniform(0.2, 10000)
        #     decimal_len = random.randint(1, 4)
        #     value = round(value, decimal_len)

        value = number_generate.t_value_find()
        return value
    
    @ staticmethod
    def t_value_range_find():
        # flag = random.randint(0, 1)
        #
        # if flag == 0:  # generate integer number
        #     t_value_a = random.randint(1, 9998)
        #     t_value_b = random.randint(t_value_a + 1, 10000)
        # else:  # generate real number
        #     t_value_a = random.uniform(0.2, 9999)
        #     decimal_len = random.randint(1, 4)
        #     t_value_a = round(t_value_a, decimal_len)
        #
        #     t_value_b = random.uniform(t_value_a + 0.1, 10000)
        #     decimal_len = random.randint(1, 4)
        #     t_value_b = round(t_value_b, decimal_len)

        [t_value_a, t_value_b] = number_generate.t_value_range_find()
        return [t_value_a, t_value_b]
