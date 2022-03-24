from template import TP_template
from public import parameters
import copy
import random
import math


class SinceAtomOrganizer:

    def __init__(self, historically_overall_translation_dict, once_random_translation_dict, since_info_dict,
                 limit_num, historically_limit_num):
        self.historically_overall_translation_dict = copy.deepcopy(historically_overall_translation_dict)
        self.once_translation_list_type1 = copy.deepcopy(once_random_translation_dict['type1'])
        self.once_translation_list_type2 = copy.deepcopy(once_random_translation_dict['type2'])
        self.once_translation_list_type3 = copy.deepcopy(once_random_translation_dict['type3'])

        self.since_info_dict = copy.deepcopy(since_info_dict)

        # translation type is determined by the translating type of 'once' operator
        self.translations_type1 = self.organize_translate_type_1_2(1, historically_limit_num, limit_num)
        # self.once_translation_list_type2 may be empty -> see since_atom_once_type2_organizer.py
        if len(self.once_translation_list_type2) > 0:
            self.translations_type2 = self.organize_translate_type_1_2(2, historically_limit_num, limit_num)
        self.translations_type3 = self.organize_translate_type_3(historically_limit_num, limit_num)

        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.random_select_since_translation(limit_num)

    def organize_translate_type_1_2(self, type_index, historically_limit_num, limit_num):
        eng_list = []
        historically_translation_list = self.random_select_historically_translation_type_1_2(historically_limit_num)
        if type_index == 1:
            once_translation_list = self.once_translation_list_type1
        else:  # type_index == 2
            once_translation_list = self.once_translation_list_type2

        if (len(historically_translation_list) * len(once_translation_list)) <= \
                1/parameters.union_operation_threshold_probability * limit_num:
            # use for loop
            for eng_historically in historically_translation_list:
                for eng_once in once_translation_list:
                    conj = ' since '
                    eng = eng_historically + conj + eng_once
                    eng_list.append(eng)
        else:
            # use union operation
            eng_set_auxiliary = set()
            eng_set = set()
            while len(eng_set) < limit_num:
                # probe
                old_count = len(eng_set_auxiliary)
                eng_historically = random.choice(historically_translation_list)
                eng_once = random.choice(once_translation_list)
                eng = eng_historically + ' ' + eng_once
                eng_set_auxiliary.add(eng)
                new_count = len(eng_set_auxiliary)

                # no repetition for this time, then formally organize translation
                if (new_count - old_count) == 1:
                    conj = ' since '
                    eng = eng_historically + conj + eng_once
                    eng_set.add(eng)

            eng_list = sorted(eng_set)

        return eng_list

    def organize_translate_type_3(self, historically_limit_num, limit_num):
        eng_list = []
        historically_translation_list = self.random_select_historically_translation_type_3(historically_limit_num)
        once_translation_list = self.once_translation_list_type3

        category = self.since_info_dict['index'][0]
        sub_category = self.since_info_dict['index'][1]
        since_template = copy.deepcopy(TP_template.Eng_TP[category][sub_category])
        concatenate_list = copy.deepcopy(since_template['concatenation'])

        if (len(once_translation_list) * len(historically_translation_list)) <= \
                1/parameters.union_operation_threshold_probability * limit_num:
            # use for loop
            for eng_once in once_translation_list:
                for eng_historically in historically_translation_list:
                    conj = random.choice(concatenate_list)
                    conj_with_punctuation = self.punctuation_add(conj)
                    eng = eng_once + conj_with_punctuation + eng_historically
                    eng_list.append(eng)
        else:
            # use union operation
            eng_set_auxiliary = set()
            eng_set = set()
            while len(eng_set) < limit_num:
                # probe
                old_count = len(eng_set_auxiliary)
                eng_once = random.choice(once_translation_list)
                eng_historically = random.choice(historically_translation_list)
                eng = eng_once + ' ' + eng_historically
                eng_set_auxiliary.add(eng)
                new_count = len(eng_set_auxiliary)

                # no repetition for this time, then formally organize translation
                if (new_count - old_count) == 1:
                    conj = random.choice(concatenate_list)
                    conj_with_punctuation = self.punctuation_add(conj)
                    eng = eng_once + conj_with_punctuation + eng_historically
                    eng_set.add(eng)

            eng_list = sorted(eng_set)

        return eng_list

    def random_select_historically_translation_type_1_2(self, historically_limit_num):
        translation_list_type1 = self.historically_overall_translation_dict['type1']
        translation_list_type2 = self.historically_overall_translation_dict['type2']
        half_historically_limit_num = math.ceil(historically_limit_num/2)

        if len(translation_list_type1) > half_historically_limit_num:
            eng_list_type1 = random.sample(translation_list_type1, half_historically_limit_num)
        else:
            eng_list_type1 = translation_list_type1

        if len(translation_list_type2) > (historically_limit_num - half_historically_limit_num):
            eng_list_type2 = random.sample(translation_list_type2, historically_limit_num-half_historically_limit_num)
        else:
            eng_list_type2 = translation_list_type2

        # random selected translation
        random_eng_list = eng_list_type1 + eng_list_type2
        random.shuffle(random_eng_list)

        return random_eng_list

    def random_select_historically_translation_type_3(self, historically_limit_num):
        # only accept type 1 translation of 'historically' operator
        translation_list_type1 = self.historically_overall_translation_dict['type1']

        if len(translation_list_type1) > historically_limit_num:
            eng_list_type1 = random.sample(translation_list_type1, historically_limit_num)
        else:
            eng_list_type1 = translation_list_type1

        # random selected translation
        random_eng_list = eng_list_type1
        random.shuffle(random_eng_list)

        return random_eng_list

    def random_select_since_translation(self, limit_num):
        # self.once_translation_list_type2 is not empty
        if len(self.once_translation_list_type2) > 0:
            limit_num_type2 = math.ceil(limit_num/3)
            limit_num_type3 = math.ceil(limit_num/3)
            limit_num_type1 = limit_num - limit_num_type2 - limit_num_type3

            if len(self.translations_type1) > limit_num_type1:
                random_eng_list_type1 = random.sample(self.translations_type1, limit_num_type1)
            else:
                random_eng_list_type1 = self.translations_type1

            if len(self.translations_type2) > limit_num_type2:
                random_eng_list_type2 = random.sample(self.translations_type2, limit_num_type2)
            else:
                random_eng_list_type2 = self.translations_type2

            if len(self.translations_type3) > limit_num_type3:
                random_eng_list_type3 = random.sample(self.translations_type3, limit_num_type3)
            else:
                random_eng_list_type3 = self.translations_type3

            random_eng_list = random_eng_list_type1 + random_eng_list_type2 + random_eng_list_type3
            random.shuffle(random_eng_list)
            # overall translations
            eng_list = self.translations_type1 + self.translations_type2 + self.translations_type3

            rate = format(len(random_eng_list)/len(eng_list) * 100, '.4f')
            selection_rate = str(rate) + '%'

            return [random_eng_list, eng_list, selection_rate]

        # self.once_translation_list_type2 is empty
        else:
            limit_num_type3 = math.ceil(limit_num/2)
            limit_num_type1 = limit_num - limit_num_type3

            if len(self.translations_type1) > limit_num_type1:
                random_eng_list_type1 = random.sample(self.translations_type1, limit_num_type1)
            else:
                random_eng_list_type1 = self.translations_type1

            if len(self.translations_type3) > limit_num_type3:
                random_eng_list_type3 = random.sample(self.translations_type3, limit_num_type3)
            else:
                random_eng_list_type3 = self.translations_type3

            random_eng_list = random_eng_list_type1 + random_eng_list_type3
            random.shuffle(random_eng_list)
            # overall translations
            eng_list = self.translations_type1 + self.translations_type3

            rate = format(len(random_eng_list) / len(eng_list) * 100, '.4f')
            selection_rate = str(rate) + '%'

            return [random_eng_list, eng_list, selection_rate]

    @staticmethod
    def punctuation_add(conj):
        comma = ','
        # e.g. conj = 'since then', conj_with_comma = ', since then '
        conj_with_comma = comma + ' ' + conj + ' '
        semicolon = ';'
        # e.g. conj = 'since then', conj_with_semicolon = '; since then '
        conj_with_semicolon = semicolon + ' ' + conj + ' '
        # point = random.randint(0, 1)
        point = 0  # consider boolean combination
        if point == 0:
            return conj_with_comma
        else:
            return conj_with_semicolon
