from public import parameters
import copy
import random
import math


class AlwaysAtomOrganizer:
    def __init__(self, package_list, nest_info_dict, limit_num):
        self.eng_temporal_phrase = copy.deepcopy(package_list[0])
        # print('eng_temporal_phrase:', len(self.eng_temporal_phrase))
        self.eng_main_sentence_type1 = copy.deepcopy(package_list[1])
        # print('eng_main_sentence_type1:', len(self.eng_main_sentence_type1))
        self.eng_main_sentence_type2 = copy.deepcopy(package_list[2])
        # print('eng_main_sentence_type2:', len(self.eng_main_sentence_type2))

        self.nest_info_dict = copy.deepcopy(nest_info_dict)

        self.translation_list_type1 = self.translate_type1(limit_num)
        self.translation_list_type2 = self.translate_type2(limit_num)

        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.random_select_translation(limit_num)

    def translate_type1(self, limit_num):
        eng_list = []
        if (len(self.eng_main_sentence_type1) * len(self.eng_temporal_phrase)) <= \
                1/parameters.union_operation_threshold_probability * limit_num:
            # use for loop
            # print('use for loop')
            for main in self.eng_main_sentence_type1:
                for phrase in self.eng_temporal_phrase:
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
            # count = 0
            while len(eng_main_phrase_set) < math.ceil(limit_num/2):
                # count = count + 1  # enter loop
                old_count = len(eng_main_phrase_set)
                main = random.choice(self.eng_main_sentence_type1)
                phrase = random.choice(self.eng_temporal_phrase)
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

        return eng_list

    def translate_type2(self, limit_num):
        eng_list = []

        if (len(self.eng_main_sentence_type2) * len(self.eng_temporal_phrase)) <= \
                1/parameters.union_operation_threshold_probability * limit_num:
            # use for loop
            # print('use for loop')
            for main in self.eng_main_sentence_type2:
                for phrase in self.eng_temporal_phrase:
                    eng = main + ' ' + phrase
                    eng_list.append(eng)
        else:
            # use union operation
            # print('use union operation')
            eng_main_phrase_set = set()
            # count = 0
            while len(eng_main_phrase_set) < math.ceil(limit_num/2):
                # count = count + 1
                main = random.choice(self.eng_main_sentence_type2)
                phrase = random.choice(self.eng_temporal_phrase)
                eng = main + ' ' + phrase
                eng_main_phrase_set.add(eng)
            # print('count:', count)
            eng_list = sorted(eng_main_phrase_set)

        return eng_list

    def random_select_translation(self, limit_num):
        half_limit_num = math.ceil(limit_num/2)
        if len(self.translation_list_type1) > half_limit_num:
            eng_list_type1 = random.sample(self.translation_list_type1, half_limit_num)
        else:
            eng_list_type1 = self.translation_list_type1
        if len(self.translation_list_type2) > (limit_num - half_limit_num):
            eng_list_type2 = random.sample(self.translation_list_type2, limit_num-half_limit_num)
        else:
            eng_list_type2 = self.translation_list_type2

        # random selected translation
        random_eng_list = eng_list_type1 + eng_list_type2
        random.shuffle(random_eng_list)
        # overall translations
        eng_list = self.translation_list_type1 + self.translation_list_type2
        # selection rate
        rate = format(len(random_eng_list)/len(eng_list) * 100, '.4f')
        selection_rate = str(rate) + '%'

        return [random_eng_list, eng_list, selection_rate]

    def display_translation(self):
        print('translations of type 1:')
        count = 1
        for eng in self.translation_list_type1:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

        print('translations of type 2:')
        count = 1
        for eng in self.translation_list_type2:
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
