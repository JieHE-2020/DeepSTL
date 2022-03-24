from grammar.level_3.NTP_atom_BC_atom import original_NTP_SP_rules
from selection.level_1.atom.atom_selector import AtomSelector
from corpus import number_generate
import random
import copy


class OriginalNTPAtomSelector:
    def __init__(self, tp_type='random'):
        self.ntp_info_dict = dict()
        self.tp_type = tp_type
        self.tp_select()

    # This function uses class AtomSelector
    def tp_select(self):
        # select category
        if self.tp_type == 'eventually_always':
            category = 0
        elif self.tp_type == 'always_eventually':
            category = 1
        else:
            # randomly choose the category of NTP
            category = random.randint(0, len(original_NTP_SP_rules.NTP) - 1)

        # randomly choose the sub_category of the chosen category (in a weighted manner)
        sum_list = []
        sum = 0.0

        for i in range(len(original_NTP_SP_rules.NTP[category])):
            sum = sum + original_NTP_SP_rules.NTP[category][i]['probability']
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
        ntp_info_dict = copy.deepcopy(original_NTP_SP_rules.NTP[category][sub_category])
        del ntp_info_dict['probability']
        ntp_info_dict['type'][0] = ntp_info_dict['type'][0] + '_Atom'

        self.ntp_filling(ntp_info_dict, category, sub_category)

    def ntp_filling(self, ntp_info_dict, category, sub_category):
        """
        the following part selects SP expressions
        # category == 0 => eventually_always
        # category == 1 => always_eventually
        """
        if category == 0:  # for 'eventually_always'
            atom_type = 'SE'
            atom_selector = AtomSelector(atom_type)
            sp_info_dict = atom_selector.info_dict
            self.ntp_replacement_1(sub_category, ntp_info_dict, sp_info_dict)

        if category == 1:  # for 'always_eventually'
            select_cmd = random.randint(0, 1)
            if select_cmd == 0:
                atom_type = 'SE'
            else:
                atom_type = 'ERE'
            atom_selector = AtomSelector(atom_type)
            sp_info_dict = atom_selector.info_dict
            self.ntp_replacement_1(sub_category, ntp_info_dict, sp_info_dict)

    def ntp_replacement_1(self, sub_category, ntp_info_dict, sp_info_dict):
        ntp_info_dict['ingredient'][0] = sp_info_dict
        sp_expr = sp_info_dict['expression']
        if sub_category == 0:
            ntp_info_dict['expression'] = ntp_info_dict['expression'].replace('SP_expr', sp_expr)

        if sub_category == 1:
            t_value_21 = self.t_value_find()
            ntp_info_dict['ingredient'][1] = str(t_value_21)
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_21', ntp_info_dict['ingredient'][1])
            ntp_info_dict['expression'] = ntp_info_dict['expression'].replace('SP_expr', sp_expr)

        if sub_category == 2:
            [t_value_21, t_value_22] = self.t_value_range_find()
            ntp_info_dict['ingredient'][1] = str(t_value_21)
            ntp_info_dict['ingredient'][2] = str(t_value_22)
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_21', ntp_info_dict['ingredient'][1])
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_22', ntp_info_dict['ingredient'][2])
            ntp_info_dict['expression'] = ntp_info_dict['expression'].replace('SP_expr', sp_expr)

        if sub_category == 3:
            t_value_11 = self.t_value_find()
            ntp_info_dict['ingredient'][1] = str(t_value_11)
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_11', ntp_info_dict['ingredient'][1])
            ntp_info_dict['expression'] = ntp_info_dict['expression'].replace('SP_expr', sp_expr)

        if sub_category == 4:
            t_value_11 = self.t_value_find()
            t_value_21 = self.t_value_find()
            ntp_info_dict['ingredient'][1] = str(t_value_11)
            ntp_info_dict['ingredient'][2] = str(t_value_21)
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_11', ntp_info_dict['ingredient'][1])
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_21', ntp_info_dict['ingredient'][2])
            ntp_info_dict['expression'] = ntp_info_dict['expression'].replace('SP_expr', sp_expr)

        if sub_category == 5:
            t_value_11 = self.t_value_find()
            [t_value_21, t_value_22] = self.t_value_range_find()
            ntp_info_dict['ingredient'][1] = str(t_value_11)
            ntp_info_dict['ingredient'][2] = str(t_value_21)
            ntp_info_dict['ingredient'][3] = str(t_value_22)
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_11', ntp_info_dict['ingredient'][1])
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_21', ntp_info_dict['ingredient'][2])
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_22', ntp_info_dict['ingredient'][3])
            ntp_info_dict['expression'] = ntp_info_dict['expression'].replace('SP_expr', sp_expr)

        if sub_category == 6:
            [t_value_11, t_value_12] = self.t_value_range_find()
            ntp_info_dict['ingredient'][1] = str(t_value_11)
            ntp_info_dict['ingredient'][2] = str(t_value_12)
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_11', ntp_info_dict['ingredient'][1])
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_12', ntp_info_dict['ingredient'][2])
            ntp_info_dict['expression'] = ntp_info_dict['expression'].replace('SP_expr', sp_expr)

        if sub_category == 7:
            [t_value_11, t_value_12] = self.t_value_range_find()
            t_value_21 = self.t_value_find()
            ntp_info_dict['ingredient'][1] = str(t_value_11)
            ntp_info_dict['ingredient'][2] = str(t_value_12)
            ntp_info_dict['ingredient'][3] = str(t_value_21)
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_11', ntp_info_dict['ingredient'][1])
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_12', ntp_info_dict['ingredient'][2])
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_21', ntp_info_dict['ingredient'][3])
            ntp_info_dict['expression'] = ntp_info_dict['expression'].replace('SP_expr', sp_expr)

        if sub_category == 8:
            [t_value_11, t_value_12] = self.t_value_range_find()
            [t_value_21, t_value_22] = self.t_value_range_find()
            ntp_info_dict['ingredient'][1] = str(t_value_11)
            ntp_info_dict['ingredient'][2] = str(t_value_12)
            ntp_info_dict['ingredient'][3] = str(t_value_21)
            ntp_info_dict['ingredient'][4] = str(t_value_22)
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_11', ntp_info_dict['ingredient'][1])
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_12', ntp_info_dict['ingredient'][2])
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_21', ntp_info_dict['ingredient'][3])
            ntp_info_dict['expression'] = \
                ntp_info_dict['expression'].replace('t_value_22', ntp_info_dict['ingredient'][4])
            ntp_info_dict['expression'] = ntp_info_dict['expression'].replace('SP_expr', sp_expr)

        self.ntp_info_dict = ntp_info_dict

    @staticmethod
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

    @staticmethod
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


# for i in range(100):
#     original_ntp_atom_selector = OriginalNTPAtomSelector('random')
#     ntp_atom_info_dict = original_ntp_atom_selector.ntp_info_dict
#     # print(ntp_atom_info_dict)
#     # print(ntp_atom_info_dict['ingredient'])
#     print(ntp_atom_info_dict['expression'])
