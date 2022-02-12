from translation.level_1.atom.atom_translator import AtomTranslator
from public import parameters
import copy
import random
import math


class BCAtomTranslator:

    def __init__(self, translate_guide, limit_num):
        self.instruction_dict = copy.deepcopy(translate_guide[0])
        self.bc_atom_info_dict = copy.deepcopy(translate_guide[1])
        self.adverbial_dict = copy.deepcopy(translate_guide[2])
        self.predicate_cmd_dict = copy.deepcopy(translate_guide[3])

        self.package_list = self.translate_preprocess(limit_num)
        self.random_selected_translations = self.translate_organize(limit_num)

    def translate_preprocess(self, limit_num):
        package_list = []
        raw_translate_guide = [self.instruction_dict, self.adverbial_dict, self.predicate_cmd_dict]

        # # calculate the limited number for translations of each atomic preposition
        # limit_num_square_root = math.exp(math.log(float(self.limit_num))/2)
        # limit_num_cube_root = math.exp(math.log(float(self.limit_num))/3)

        index = self.bc_atom_info_dict['index']
        if index == 0 or index == 1:  # 'A and B', 'A or B'
            # process atomic proposition A
            atom_info_dict_1 = self.bc_atom_info_dict['ingredient'][0]
            translate_guide = copy.deepcopy(raw_translate_guide)
            translate_guide.insert(1, atom_info_dict_1)
            # process translation
            atom_translator = AtomTranslator(translate_guide, limit_num)
            eng_list_1 = atom_translator.random_selected_translations
            package_list.append(eng_list_1)

            # process atomic proposition B
            atom_info_dict_2 = self.bc_atom_info_dict['ingredient'][1]
            translate_guide = copy.deepcopy(raw_translate_guide)
            translate_guide.insert(1, atom_info_dict_2)
            # process translation
            atom_translator = AtomTranslator(translate_guide, limit_num)
            eng_list_2 = atom_translator.random_selected_translations
            package_list.append(eng_list_2)

        else:   # index == 2 or index == 3, 'A and B and C', 'A or B or C'
            # process atomic proposition A
            atom_info_dict_1 = self.bc_atom_info_dict['ingredient'][0]
            translate_guide = copy.deepcopy(raw_translate_guide)
            translate_guide.insert(1, atom_info_dict_1)
            # process translation
            atom_translator = AtomTranslator(translate_guide, limit_num)
            eng_list_1 = atom_translator.random_selected_translations
            package_list.append(eng_list_1)

            # process atomic proposition B
            atom_info_dict_2 = self.bc_atom_info_dict['ingredient'][1]
            translate_guide = copy.deepcopy(raw_translate_guide)
            translate_guide.insert(1, atom_info_dict_2)
            # process translation
            atom_translator = AtomTranslator(translate_guide, limit_num)
            eng_list_2 = atom_translator.random_selected_translations
            package_list.append(eng_list_2)

            # process atomic proposition C
            atom_info_dict_3 = self.bc_atom_info_dict['ingredient'][2]
            translate_guide = copy.deepcopy(raw_translate_guide)
            translate_guide.insert(1, atom_info_dict_3)
            # process translation
            atom_translator = AtomTranslator(translate_guide, limit_num)
            eng_list_3 = atom_translator.random_selected_translations
            package_list.append(eng_list_3)

        return package_list

    def translate_organize(self, limit_num):
        index = self.bc_atom_info_dict['index']
        eng_list = []

        if index == 0:   # 'A and B'
            if (len(self.package_list[0]) * len(self.package_list[1])) <= \
                    1 / parameters.union_operation_threshold_probability * limit_num:
                # use for loop
                for eng_a in self.package_list[0]:
                    for eng_b in self.package_list[1]:
                        point = random.randint(0, 1)
                        if point == 0:
                            eng = eng_a + ' and ' + eng_b
                        else:
                            eng = eng_a + ', and ' + eng_b
                        eng_list.append(eng)
            else:
                # use union operation
                eng_set = set()
                while len(eng_set) < math.ceil(limit_num):
                    eng_a = random.choice(self.package_list[0])
                    eng_b = random.choice(self.package_list[1])
                    point = random.randint(0, 1)
                    if point == 0:
                        eng = eng_a + ' and ' + eng_b
                    else:
                        eng = eng_a + ', and ' + eng_b
                    eng_set.add(eng)
                eng_list = sorted(eng_set)

        elif index == 1:  # 'A or B'
            if (len(self.package_list[0]) * len(self.package_list[1])) <= \
                    1 / parameters.union_operation_threshold_probability * limit_num:
                # use for loop
                for eng_a in self.package_list[0]:
                    for eng_b in self.package_list[1]:
                        point = random.randint(0, 1)
                        if point == 0:
                            eng = eng_a + ' or ' + eng_b
                        else:
                            eng = eng_a + ', or ' + eng_b
                        eng_list.append(eng)
            else:
                # use union operation
                eng_set = set()
                while len(eng_set) < math.ceil(limit_num):
                    eng_a = random.choice(self.package_list[0])
                    eng_b = random.choice(self.package_list[1])
                    point = random.randint(0, 1)
                    if point == 0:
                        eng = eng_a + ' or ' + eng_b
                    else:
                        eng = eng_a + ', or ' + eng_b
                    eng_set.add(eng)
                eng_list = sorted(eng_set)

        elif index == 2:  # 'A and B and C'
            if (len(self.package_list[0]) * len(self.package_list[1]) * len(self.package_list[2])) <= \
                    1 / parameters.union_operation_threshold_probability * limit_num:
                # use for loop
                for eng_a in self.package_list[0]:
                    for eng_b in self.package_list[1]:
                        for eng_c in self.package_list[2]:
                            point = random.randint(0, 1)
                            if point == 0:
                                eng = eng_a + ' and ' + eng_b + ' and ' + eng_c
                            else:
                                eng = eng_a + ', and ' + eng_b + ', and ' + eng_c
                            eng_list.append(eng)
            else:
                # use union operation
                eng_set = set()
                while len(eng_set) < math.ceil(limit_num):
                    eng_a = random.choice(self.package_list[0])
                    eng_b = random.choice(self.package_list[1])
                    eng_c = random.choice(self.package_list[2])
                    point = random.randint(0, 1)
                    if point == 0:
                        eng = eng_a + ' and ' + eng_b + ' and ' + eng_c
                    else:
                        eng = eng_a + ', and ' + eng_b + ', and ' + eng_c
                    eng_set.add(eng)
                eng_list = sorted(eng_set)

        else:  # index == 3, 'A or B or C'
            if (len(self.package_list[0]) * len(self.package_list[1]) * len(self.package_list[2])) <= \
                    1 / parameters.union_operation_threshold_probability * limit_num:
                # use for loop
                for eng_a in self.package_list[0]:
                    for eng_b in self.package_list[1]:
                        for eng_c in self.package_list[2]:
                            point = random.randint(0, 1)
                            if point == 0:
                                eng = eng_a + ' or ' + eng_b + ' or ' + eng_c
                            else:
                                eng = eng_a + ', or ' + eng_b + ', or ' + eng_c
                            eng_list.append(eng)
            else:
                # use union operation
                eng_set = set()
                while len(eng_set) < math.ceil(limit_num):
                    eng_a = random.choice(self.package_list[0])
                    eng_b = random.choice(self.package_list[1])
                    eng_c = random.choice(self.package_list[2])
                    point = random.randint(0, 1)
                    if point == 0:
                        eng = eng_a + ' or ' + eng_b + ' or ' + eng_c
                    else:
                        eng = eng_a + ', or ' + eng_b + ', or ' + eng_c
                    eng_set.add(eng)
                eng_list = sorted(eng_set)

        random_eng_list = self.random_select_translation(eng_list, limit_num)

        return random_eng_list

    @staticmethod
    def random_select_translation(eng_list, limit_num):
        if len(eng_list) > limit_num:
            random_eng_list = random.sample(eng_list, limit_num)
        else:
            random_eng_list = eng_list

        return random_eng_list

    def display_random_translation(self):
        print('randomly selected translation:')
        count = 1
        for eng in self.random_selected_translations:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')
