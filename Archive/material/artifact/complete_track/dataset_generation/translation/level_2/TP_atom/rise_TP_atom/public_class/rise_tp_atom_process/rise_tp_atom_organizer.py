import copy
import math
import random


class RiseTPAtomOrganizer:

    def __init__(self, main_sentence_type_1, main_sentence_type_2, limit_num):
        self.main_sentence_type_1 = copy.deepcopy(main_sentence_type_1)
        self.main_sentence_type_2 = copy.deepcopy(main_sentence_type_2)

        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.random_select_translation(limit_num)

    def random_select_translation(self, limit_num):
        half_limit_num = math.ceil(limit_num / 2)
        if len(self.main_sentence_type_1) > half_limit_num:
            random_eng_list_type_1 = random.sample(self.main_sentence_type_1, half_limit_num)
        else:
            random_eng_list_type_1 = self.main_sentence_type_1

        if len(self.main_sentence_type_2) > (limit_num - half_limit_num):
            random_eng_list_type_2 = random.sample(self.main_sentence_type_2, limit_num-half_limit_num)
        else:
            random_eng_list_type_2 = self.main_sentence_type_2

        random_eng_list = random_eng_list_type_1 + random_eng_list_type_2
        random.shuffle(random_eng_list)
        # overall translations
        eng_list = self.main_sentence_type_1 + self.main_sentence_type_2

        rate = format(len(random_eng_list) / len(eng_list) * 100, '.4f')
        selection_rate = str(rate) + '%'

        return [random_eng_list, eng_list, selection_rate]

