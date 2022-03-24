import copy
import random
import math


class AlwaysAtomOrganizer:
    def __init__(self, package_list, nest_info_dict, limit_num):
        self.eng_temporal_phrase = copy.deepcopy(package_list[0])
        # self.eng_temporal_phrase = \
        #     random.sample(self.eng_temporal_phrase, math.ceil(len(self.eng_temporal_phrase)/2))
        self.eng_main_sentence_type1 = copy.deepcopy(package_list[1])
        # self.eng_main_sentence_type1 = \
        #     random.sample(self.eng_main_sentence_type1, math.ceil(len(self.eng_main_sentence_type1)/2))
        self.eng_main_sentence_type2 = copy.deepcopy(package_list[2])
        # self.eng_main_sentence_type2 = \
        #     random.sample(self.eng_main_sentence_type2, math.ceil(len(self.eng_main_sentence_type2)/2))

        self.nest_info_dict = copy.deepcopy(nest_info_dict)

        self.translation_list_type1 = self.translate_type1()
        self.translation_list_type2 = self.translate_type2()

        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.random_select_translation(limit_num)

    def translate_type1(self):
        eng_list = []

        for main in self.eng_main_sentence_type1:
            for phrase in self.eng_temporal_phrase:
                eng = main + ' ' + phrase
                eng_list.append(eng)

                if not self.nest_info_dict['hasParallelSuccessor']:
                    space = self.random_comma()
                    eng = phrase + space + main
                    eng_list.append(eng)

        return eng_list

    def translate_type2(self):
        eng_list = []

        for main in self.eng_main_sentence_type2:
            for phrase in self.eng_temporal_phrase:
                eng = main + ' ' + phrase
                eng_list.append(eng)

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
