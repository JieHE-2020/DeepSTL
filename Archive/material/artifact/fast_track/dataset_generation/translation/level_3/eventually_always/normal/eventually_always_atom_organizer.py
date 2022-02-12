from public import parameters
import copy
import random
import math


class EventuallyAlwaysAtomOrganizer:
    def __init__(self, package_list, nest_info_dict, limit_num):
        self.eventually_eng_temporal_phrase = copy.deepcopy(package_list[0])
        self.eventually_eng_temporal_clause = copy.deepcopy(package_list[1])
        self.always_eng_temporal_phrase = copy.deepcopy(package_list[2])
        self.always_eng_main_sentence_type1 = copy.deepcopy(package_list[3])
        self.always_eng_main_sentence_type2 = copy.deepcopy(package_list[4])

        self.nest_info_dict = copy.deepcopy(nest_info_dict)

        self.always_translation_list_type1 = self.always_translate_type1(limit_num)
        self.always_translation_list_type2 = self.always_translate_type2(limit_num)

        operator = 'eventually'
        self.random_selected_eventually_translations = \
            self.random_select_half_translation(self.eventually_eng_temporal_phrase, 
                                                self.eventually_eng_temporal_clause, limit_num, operator)
        operator = 'always'
        self.random_selected_always_translations = \
            self.random_select_half_translation(self.always_translation_list_type1, self.always_translation_list_type2, 
                                                limit_num, operator)

        self.random_selected_translations = self.random_select_translation(limit_num)

    def always_translate_type1(self, limit_num):
        eng_list = []
        if (len(self.always_eng_main_sentence_type1) * len(self.always_eng_temporal_phrase)) <= \
                1 / parameters.union_operation_threshold_probability * limit_num:
            # use for loop
            # print('use for loop')
            for main in self.always_eng_main_sentence_type1:
                for phrase in self.always_eng_temporal_phrase:
                    eng = main + ' ' + phrase
                    eng_list.append(eng)

                    if not self.nest_info_dict['hasParallelSuccessor']:
                        space = self.random_comma()
                        eng = phrase + space + main
                        eng_list.append(eng)
        else:
            # use union operation
            # print('use union operation')
            eng_main_phrase_set = set()
            eng_phrase_main_set = set()
            while len(eng_main_phrase_set) < math.ceil(limit_num / 2):
                old_count = len(eng_main_phrase_set)
                main = random.choice(self.always_eng_main_sentence_type1)
                phrase = random.choice(self.always_eng_temporal_phrase)
                eng = main + ' ' + phrase
                eng_main_phrase_set.add(eng)
                new_count = len(eng_main_phrase_set)

                if (new_count - old_count) == 1:
                    if not self.nest_info_dict['hasParallelSuccessor']:
                        space = self.random_comma()
                        eng = phrase + space + main
                        eng_phrase_main_set.add(eng)
            # print('count:', count)
            eng_list = sorted(eng_main_phrase_set) + sorted(eng_phrase_main_set)
            # eng_list = sorted(eng_main_phrase_set)

        return eng_list

    def always_translate_type2(self, limit_num):
        eng_list = []

        if (len(self.always_eng_main_sentence_type2) * len(self.always_eng_temporal_phrase)) <= \
                1 / parameters.union_operation_threshold_probability * limit_num:
            # use for loop
            # print('use for loop')
            for main in self.always_eng_main_sentence_type2:
                for phrase in self.always_eng_temporal_phrase:
                    eng = main + ' ' + phrase
                    eng_list.append(eng)
        else:
            # use union operation
            # print('use union operation')
            eng_main_phrase_set = set()
            # count = 0
            while len(eng_main_phrase_set) < math.ceil(limit_num / 2):
                # count = count + 1
                main = random.choice(self.always_eng_main_sentence_type2)
                phrase = random.choice(self.always_eng_temporal_phrase)
                eng = main + ' ' + phrase
                eng_main_phrase_set.add(eng)
            # print('count:', count)
            eng_list = sorted(eng_main_phrase_set)

        return eng_list

    @staticmethod
    def random_select_half_translation(translation_list_type1, translation_list_type2, limit_num, operator):
        half_limit_num = math.ceil(limit_num / 2)
        if operator == 'always':
            if len(translation_list_type1) > (limit_num - half_limit_num):
                eng_list_type1 = random.sample(translation_list_type1, limit_num - half_limit_num)
            else:
                eng_list_type1 = translation_list_type1
        else:  # operator == 'eventually':
            if len(translation_list_type1) > (limit_num - half_limit_num):
                eng_list_type1_temp = random.sample(translation_list_type1, limit_num - half_limit_num)
            else:
                eng_list_type1_temp = translation_list_type1
            eng_list_type1 = []
            for eng in eng_list_type1_temp:
                point = random.randint(0, 1)
                if point == 0:
                    eng_list_type1.append(eng)
                else:
                    eng_list_type1.append(eng + ',')

        if len(translation_list_type2) > half_limit_num:
            eng_list_type2 = random.sample(translation_list_type2, half_limit_num)
        else:
            eng_list_type2 = translation_list_type2

        # random selected translation
        random_eng_list = eng_list_type1 + eng_list_type2
        random.shuffle(random_eng_list)
        # # overall translations
        # eng_list = translation_list_type1 + translation_list_type2
        # # selection rate
        # rate = format(len(random_eng_list) / len(eng_list) * 100, '.4f')
        # selection_rate = str(rate) + '%'

        # return [random_eng_list, eng_list, selection_rate]
        return random_eng_list

    def random_select_translation(self, limit_num):
        eng_set = set()
        while len(eng_set) < limit_num:
            eventually = random.choice(self.random_selected_eventually_translations)
            always = random.choice(self.random_selected_always_translations)
            eng = eventually + ' ' + always
            eng_set.add(eng)

        eng_list = sorted(eng_set)
        return eng_list

    def display_translation(self):
        print('translations of type 1:')
        count = 1
        for eng in self.always_translation_list_type1:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

        print('translations of type 2:')
        count = 1
        for eng in self.always_translation_list_type2:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

    @staticmethod
    def random_comma():
        string1 = ' '
        string2 = ', '
        point = random.randint(0, 1)
        if point == 0:
            return string1
        else:
            return string2
