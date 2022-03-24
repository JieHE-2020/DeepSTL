from template import TP_template
from public import parameters
import copy
import random
import math


class UntilAtomOrganizer:

    def __init__(self, always_overall_translation_dict, eventually_random_translation_dict, until_info_dict, 
                 limit_num, always_limit_num):
        self.always_overall_translation_dict = copy.deepcopy(always_overall_translation_dict)
        self.eventually_translation_list_type1 = copy.deepcopy(eventually_random_translation_dict['type1'])
        self.eventually_translation_list_type2 = copy.deepcopy(eventually_random_translation_dict['type2'])
        self.eventually_translation_list_type3 = copy.deepcopy(eventually_random_translation_dict['type3'])

        self.until_info_dict = copy.deepcopy(until_info_dict)

        # translation type is determined by the translating type of 'eventually' operator
        self.translations_type1 = self.organize_translate_type_1_2(1, always_limit_num, limit_num)
        # self.eventually_translation_list_type2 may be empty -> see until_atom_eventually_type2_organizer.py
        if len(self.eventually_translation_list_type2) > 0:
            self.translations_type2 = self.organize_translate_type_1_2(2, always_limit_num, limit_num)
        self.translations_type3 = self.organize_translate_type_3(always_limit_num, limit_num)

        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.random_select_until_translation(limit_num)

    def organize_translate_type_1_2(self, type_index, always_limit_num, limit_num):
        eng_list = []
        always_translation_list = self.random_select_always_translation_type_1_2(always_limit_num)
        if type_index == 1:
            eventually_translation_list = self.eventually_translation_list_type1
        else:  # type_index == 2
            eventually_translation_list = self.eventually_translation_list_type2

        if (len(always_translation_list) * len(eventually_translation_list)) <= \
                1/parameters.union_operation_threshold_probability * limit_num:
            # use for loop
            # print('use for loop')
            for eng_always in always_translation_list:
                for eng_eventually in eventually_translation_list:
                    conj = self.until_till_selection()
                    eng = eng_always + conj + eng_eventually
                    eng_list.append(eng)
        else:
            # use union operation
            # print('use union operation')
            eng_set_auxiliary = set()
            eng_set = set()
            while len(eng_set) < limit_num:
                # probe
                old_count = len(eng_set_auxiliary)
                eng_always = random.choice(always_translation_list)
                eng_eventually = random.choice(eventually_translation_list)
                eng = eng_always + ' ' + eng_eventually
                eng_set_auxiliary.add(eng)
                new_count = len(eng_set_auxiliary)

                # no repetition for this time, then formally organize translation
                if (new_count - old_count) == 1:
                    conj = self.until_till_selection()
                    eng = eng_always + conj + eng_eventually
                    eng_set.add(eng)

            eng_list = sorted(eng_set)

        return eng_list

    def organize_translate_type_3(self, always_limit_num, limit_num):
        eng_list = []
        always_translation_list = self.random_select_always_translation_type_3(always_limit_num)
        eventually_translation_list = self.eventually_translation_list_type3

        category = self.until_info_dict['index'][0]
        sub_category = self.until_info_dict['index'][1]
        until_template = copy.deepcopy(TP_template.Eng_TP[category][sub_category])
        concatenate_list = copy.deepcopy(until_template['concatenation'])

        if (len(eventually_translation_list) * len(always_translation_list)) <= \
                1/parameters.union_operation_threshold_probability * limit_num:
            # use for loop
            # print('use for loop')
            for eng_eventually in eventually_translation_list:
                for eng_always in always_translation_list:
                    conj = random.choice(concatenate_list)
                    conj_with_punctuation = self.punctuation_add(conj)
                    eng = eng_eventually + conj_with_punctuation + eng_always
                    eng_list.append(eng)
        else:
            # use union operation
            # print('use union operation')
            eng_set_auxiliary = set()
            eng_set = set()
            while len(eng_set) < limit_num:
                # probe
                old_count = len(eng_set_auxiliary)
                eng_eventually = random.choice(eventually_translation_list)
                eng_always = random.choice(always_translation_list)
                eng = eng_eventually + ' ' + eng_always
                eng_set_auxiliary.add(eng)
                new_count = len(eng_set_auxiliary)

                # no repetition for this time, then formally organize translation
                if (new_count - old_count) == 1:
                    conj = random.choice(concatenate_list)
                    conj_with_punctuation = self.punctuation_add(conj)
                    eng = eng_eventually + conj_with_punctuation + eng_always
                    eng_set.add(eng)

            eng_list = sorted(eng_set)

        return eng_list

    def random_select_always_translation_type_1_2(self, always_limit_num):
        translation_list_type1 = self.always_overall_translation_dict['type1']
        translation_list_type2 = self.always_overall_translation_dict['type2']
        half_always_limit_num = math.ceil(always_limit_num/2)

        if len(translation_list_type1) > half_always_limit_num:
            eng_list_type1 = random.sample(translation_list_type1, half_always_limit_num)
        else:
            eng_list_type1 = translation_list_type1

        if len(translation_list_type2) > (always_limit_num - half_always_limit_num):
            eng_list_type2 = random.sample(translation_list_type2, always_limit_num-half_always_limit_num)
        else:
            eng_list_type2 = translation_list_type2

        # random selected translation
        random_eng_list = eng_list_type1 + eng_list_type2
        random.shuffle(random_eng_list)

        return random_eng_list

    def random_select_always_translation_type_3(self, always_limit_num):
        # only accept type 1 translation of 'always' operator
        translation_list_type1 = self.always_overall_translation_dict['type1']

        if len(translation_list_type1) > always_limit_num:
            eng_list_type1 = random.sample(translation_list_type1, always_limit_num)
        else:
            eng_list_type1 = translation_list_type1

        # random selected translation
        random_eng_list = eng_list_type1
        random.shuffle(random_eng_list)

        return random_eng_list

    def random_select_until_translation(self, limit_num):
        # self.eventually_translation_list_type2 is not empty
        if len(self.eventually_translation_list_type2) > 0:
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

        # self.eventually_translation_list_type2 is empty
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
    def until_till_selection():
        string1 = ' until '
        string2 = ' till '
        point = random.randint(0, 1)
        if point == 0:
            return string1
        else:
            return string2

    @staticmethod
    def punctuation_add(conj):
        comma = ','
        # e.g. conj = 'until then', conj_with_comma = ', until then '
        conj_with_comma = comma + ' ' + conj + ' '
        semicolon = ';'
        # e.g. conj = 'until then', conj_with_semicolon = '; until then '
        conj_with_semicolon = semicolon + ' ' + conj + ' '
        # point = random.randint(0, 1)
        point = 0  # consider boolean combination
        if point == 0:
            return conj_with_comma
        else:
            return conj_with_semicolon
