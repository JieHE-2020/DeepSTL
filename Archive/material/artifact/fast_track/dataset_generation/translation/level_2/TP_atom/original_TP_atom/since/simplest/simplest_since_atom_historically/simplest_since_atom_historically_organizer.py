import copy
import random


class SimplestSinceAtomHistoricallyOrganizer:

    def __init__(self, eng_main_sentence_type1, limit_num):
        self.eng_main_sentence_type1 = copy.deepcopy(eng_main_sentence_type1)

        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.random_select_translation(limit_num)

    def random_select_translation(self, limit_num):
        if len(self.eng_main_sentence_type1) > limit_num:
            eng_list_type1 = random.sample(self.eng_main_sentence_type1, limit_num)
        else:
            eng_list_type1 = self.eng_main_sentence_type1

        # random selected translation
        random_eng_list = eng_list_type1
        random.shuffle(random_eng_list)
        # overall translations
        eng_list = self.eng_main_sentence_type1
        # selection rate
        rate = format(len(random_eng_list)/len(eng_list) * 100, '.4f')
        selection_rate = str(rate) + '%'

        return [random_eng_list, eng_list, selection_rate]
