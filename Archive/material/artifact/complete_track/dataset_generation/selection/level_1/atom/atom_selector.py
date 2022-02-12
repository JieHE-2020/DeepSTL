from grammar.level_1.atom import atom_rules
from corpus import basic_words
from corpus import sig_mode_name_generate
from corpus import number_generate
import random
import copy


class AtomSelector:
    def __init__(self, atom_type, boolean_combination=False):
        self.atom_type = atom_type
        self.boolean_combination = boolean_combination
        self.info_dict = dict()
        if self.atom_type == 'SE':
            self.se_select()
        if self.atom_type == 'ERE':
            self.ere_select()

    def se_select(self):
        # randomly choose the category of SE
        if not self.boolean_combination:
            category = random.randint(0, len(atom_rules.SE) - 1)
        else:
            # no category 5
            # category = random.randint(0, len(atom_rules.SE) - 2)  # category 5 is banned
            category = random.randint(0, len(atom_rules.SE) - 1)

        # randomly choose the sub_category of the chosen category (in a weighted manner)
        sum_list = []
        sum = 0.0

        for i in range(len(atom_rules.SE[category])):
            sum = sum + atom_rules.SE[category][i]['probability']
            sum_list.append(sum)

        # take category = 0 for example
        # sum_list = [0.6, 0.8, 0.9, 1]
        # 0 <= point < sum_list[0]            =>  sub_category == 0
        # sum_list[0] <= point < sum_list[1]  =>  sub_category == 1
        # sum_list[1] <= point < sum_list[2]  =>  sub_category == 2
        # sum_list[2] <= point < sum_list[3]  =>  sub_category == 3
        point = random.random()
        sub_category = 0
        if 0 <= point < sum_list[0]:
            sub_category = 0
        else:
            for i in range(len(sum_list) - 1):
                # len(sum_list) - 1 = 4 - 1 = 3 => i = 0, 1, 2
                if sum_list[i] <= point < sum_list[i + 1]:
                    sub_category = i + 1

        # se_dict and atom_rules.SE[category][sub_category] are different
        se_dict = copy.deepcopy(atom_rules.SE[category][sub_category])
        del se_dict['probability']

        if category == 0 or category == 1 or category == 2:
            sig = self.signal_continuous_find()
            value = self.value_find()

            se_dict['ingredient'][0] = sig
            se_dict['ingredient'][1] = str(value)

            se_dict['expression'] = se_dict['expression'].replace('sig', se_dict['ingredient'][0])
            se_dict['expression'] = se_dict['expression'].replace('value', se_dict['ingredient'][1])

        elif category == 3:
            sig = self.signal_continuous_find()
            [value1, value2] = self.value_range_find()

            se_dict['ingredient'][0] = sig
            se_dict['ingredient'][1] = str(value1)
            se_dict['ingredient'][2] = str(value2)

            se_dict['expression'] = se_dict['expression'].replace('sig', se_dict['ingredient'][0])
            se_dict['expression'] = se_dict['expression'].replace('value1', se_dict['ingredient'][1])
            se_dict['expression'] = se_dict['expression'].replace('value2', se_dict['ingredient'][2])

        elif category == 4:
            if sub_category < 4:
                sig = self.signal_discrete_find()
                mode = self.mode_find()

                se_dict['ingredient'][0] = sig
                se_dict['ingredient'][1] = mode

                se_dict['expression'] = se_dict['expression'].replace('sig', se_dict['ingredient'][0])
                se_dict['expression'] = se_dict['expression'].replace('mode', se_dict['ingredient'][1])

            else:
                substitution = self.substitution_find()
                se_dict['ingredient'][0] = substitution
                se_dict['expression'] = se_dict['expression'].replace('substitution', se_dict['ingredient'][0])

        else:
            if sub_category < 4:
                sig = self.signal_discrete_find()
                [mode1, mode2] = self.multi_mode_find()

                se_dict['ingredient'][0] = sig
                se_dict['ingredient'][1] = mode1
                se_dict['ingredient'][2] = mode2

                se_dict['expression'] = se_dict['expression'].replace('sig', se_dict['ingredient'][0])
                se_dict['expression'] = se_dict['expression'].replace('mode1', se_dict['ingredient'][1])
                se_dict['expression'] = se_dict['expression'].replace('mode2', se_dict['ingredient'][2])

            # else:
            #     [substitution1, substitution2] = self.multi_substitution_find()
            #
            #     se_dict['ingredient'][0] = substitution1
            #     se_dict['ingredient'][1] = substitution2
            #
            #     se_dict['expression'] = se_dict['expression'].replace('substitution1', se_dict['ingredient'][0])
            #     se_dict['expression'] = se_dict['expression'].replace('substitution2', se_dict['ingredient'][1])

        self.info_dict = se_dict

    def ere_select(self):
        # randomly choose the category of ERE
        if not self.boolean_combination:
            category = random.randint(0, len(atom_rules.ERE) - 1)
        else:
            # no category 5
            category = random.randint(0, len(atom_rules.ERE) - 2)

        # randomly choose the sub_category of the chosen category (in a weighted manner)
        sum_list = []
        sum = 0.0

        for i in range(len(atom_rules.ERE[category])):
            sum = sum + atom_rules.ERE[category][i]['probability']
            sum_list.append(sum)

        # take category = 1 for example
        # sum_list = [0.3, 0.6, 0.8, 1]
        # 0 <= point < sum_list[0]            =>  sub_category == 0
        # sum_list[0] <= point < sum_list[1]  =>  sub_category == 1
        # sum_list[1] <= point < sum_list[2]  =>  sub_category == 2
        # sum_list[2] <= point < sum_list[3]  =>  sub_category == 3
        point = random.random()
        sub_category = 0
        if 0 <= point < sum_list[0]:
            sub_category = 0
        else:
            for i in range(len(sum_list) - 1):
                # len(sum_list) - 1 = 4 - 1 = 3 => i = 0, 1, 2
                if sum_list[i] <= point < sum_list[i + 1]:
                    sub_category = i + 1

        # ere_dict and atom_rules.ERE[category][sub_category] are different
        ere_dict = copy.deepcopy(atom_rules.ERE[category][sub_category])
        del ere_dict['probability']

        if category == 0 or category == 1 or category == 2:
            sig = self.signal_continuous_find()
            value = self.value_find()

            ere_dict['ingredient'][0] = sig
            ere_dict['ingredient'][1] = str(value)

            ere_dict['expression'] = ere_dict['expression'].replace('sig', ere_dict['ingredient'][0])
            ere_dict['expression'] = ere_dict['expression'].replace('value', ere_dict['ingredient'][1])

        elif category == 3:
            sig = self.signal_continuous_find()
            [value1, value2] = self.value_range_find()

            ere_dict['ingredient'][0] = sig
            ere_dict['ingredient'][1] = str(value1)
            ere_dict['ingredient'][2] = str(value2)

            ere_dict['expression'] = ere_dict['expression'].replace('sig', ere_dict['ingredient'][0])
            ere_dict['expression'] = ere_dict['expression'].replace('value1', ere_dict['ingredient'][1])
            ere_dict['expression'] = ere_dict['expression'].replace('value2', ere_dict['ingredient'][2])

        elif category == 4:
            sig = self.signal_discrete_find()
            mode = self.mode_find()

            ere_dict['ingredient'][0] = sig
            ere_dict['ingredient'][1] = mode

            ere_dict['expression'] = ere_dict['expression'].replace('sig', ere_dict['ingredient'][0])
            ere_dict['expression'] = ere_dict['expression'].replace('mode', ere_dict['ingredient'][1])

        else:
            sig = self.signal_discrete_find()
            [mode1, mode2] = self.multi_mode_find()

            ere_dict['ingredient'][0] = sig
            ere_dict['ingredient'][1] = mode1
            ere_dict['ingredient'][2] = mode2

            ere_dict['expression'] = ere_dict['expression'].replace('sig', ere_dict['ingredient'][0])
            ere_dict['expression'] = ere_dict['expression'].replace('mode1', ere_dict['ingredient'][1])
            ere_dict['expression'] = ere_dict['expression'].replace('mode2', ere_dict['ingredient'][2])

        self.info_dict = ere_dict
    @ staticmethod
    def signal_continuous_find():
        # # option 1
        # index = random.randint(0, len(basic_words.signal_continuous) - 1)
        # return basic_words.signal_continuous[index]

        # option 2
        return sig_mode_name_generate.random_identifier_generate()

    @ staticmethod
    def signal_discrete_find():
        # # option 1
        # index = random.randint(0, len(basic_words.signal_discrete) - 1)
        # return basic_words.signal_discrete[index]

        # option 2
        return sig_mode_name_generate.random_identifier_generate()
    
    @ staticmethod
    def substitution_find():
        index = random.randint(0, len(basic_words.substitution) - 1)
        return basic_words.substitution[index]

    @ staticmethod
    def value_find():
        # flag = random.randint(0, 1)
        # # flag = 0
        #
        # if flag == 0:  # generate integer number
        #     value = random.randint(0, 10000)
        # else:  # generate decimal number
        #     value = random.uniform(0, 10000)
        #     decimal_len = random.randint(1, 4)
        #     value = round(value, decimal_len)

        value = number_generate.atom_value_find()
        return value

    @ staticmethod
    def value_range_find():
        # flag = random.randint(0, 1)
        # # flag = 0
        #
        # if flag == 0:  # generate integer number
        #     value1 = random.randint(0, 9998)
        #     value2 = random.randint(value1 + 1, 10000)
        # else:  # generate real number
        #     value1 = random.uniform(0, 9999)
        #     decimal_len = random.randint(1, 4)
        #     value1 = round(value1, decimal_len)
        #
        #     value2 = random.uniform(value1 + 0.1, 10000)
        #     decimal_len = random.randint(1, 4)
        #     value2 = round(value2, decimal_len)

        [value1, value2] = number_generate.atom_value_range_find()
        return [value1, value2]
    
    @ staticmethod
    def mode_find():
        # # option 1
        # index = random.randint(0, len(basic_words.mode) - 1)
        # return basic_words.mode[index]

        # option 2
        return sig_mode_name_generate.random_identifier_generate()
    
    @ staticmethod
    def multi_mode_find():
        # # option 1
        # index1 = random.randint(0, len(basic_words.mode) - 1)
        # index2 = random.randint(0, len(basic_words.mode) - 1)
        # while index1 == index2:
        #     index2 = random.randint(0, len(basic_words.mode) - 1)
        # 
        # mode1 = basic_words.mode[index1]
        # mode2 = basic_words.mode[index2]
        # 
        # return [mode1, mode2]

        # option 2
        mode1 = sig_mode_name_generate.random_identifier_generate()
        mode2 = sig_mode_name_generate.random_identifier_generate()
        while mode1 == mode2:
            mode2 = sig_mode_name_generate.random_identifier_generate()

        return [mode1, mode2]
    
    @staticmethod
    def multi_substitution_find():
        index1 = random.randint(0, len(basic_words.substitution) - 1)
        index2 = random.randint(0, len(basic_words.substitution) - 1)
        while index1 == index2:
            index2 = random.randint(0, len(basic_words.substitution) - 1)

        substitution1 = basic_words.substitution[index1]
        substitution2 = basic_words.substitution[index2]

        return [substitution1, substitution2]


# atom_selector = AtomSelector('SE', True)
# sp_info_dict = atom_selector.info_dict
# print(sp_info_dict)
