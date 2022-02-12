from public import parameters
import copy
import random


class SimplestAlwaysAtomOrganizer:
    def __init__(self, package_list, limit_num):
        self.eng_temporal_phrase = copy.deepcopy(package_list[0])
        self.eng_main_sentence_type1 = copy.deepcopy(package_list[1])

        self.translation_list_type1 = self.translate_type1(limit_num)

        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.random_select_translation(limit_num)

    def translate_type1(self, limit_num):
        eng_list = []

        if (len(self.eng_main_sentence_type1) * len(self.eng_temporal_phrase)) <= \
                1/parameters.union_operation_threshold_probability * limit_num:
            # use for loop
            for main in self.eng_main_sentence_type1:
                for phrase in self.eng_temporal_phrase:
                    eng = main + ' ' + phrase
                    eng_list.append(eng)
        else:
            # use union operation
            eng_main_phrase_set = set()
            while len(eng_main_phrase_set) < limit_num:
                main = random.choice(self.eng_main_sentence_type1)
                phrase = random.choice(self.eng_temporal_phrase)
                eng = main + ' ' + phrase
                eng_main_phrase_set.add(eng)

            eng_list = sorted(eng_main_phrase_set)

        return eng_list

    def random_select_translation(self, limit_num):
        if len(self.translation_list_type1) > limit_num:
            eng_list_type1 = random.sample(self.translation_list_type1, limit_num)
        else:
            eng_list_type1 = self.translation_list_type1

        # random selected translation
        random_eng_list = eng_list_type1
        random.shuffle(random_eng_list)
        # overall translations
        eng_list = self.translation_list_type1
        # selection rate
        rate = format(len(random_eng_list)/len(eng_list) * 100, '.4f')
        selection_rate = str(rate) + '%'

        return [random_eng_list, eng_list, selection_rate]
