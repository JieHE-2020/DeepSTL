from public import parameters
import copy
import random


class SimplestUntilAtomOrganizer:

    def __init__(self, always_translation_list, eventually_translation_list, limit_num):
        self.always_translation_list = copy.deepcopy(always_translation_list)
        self.eventually_translation_list = copy.deepcopy(eventually_translation_list)

        self.overall_translations = self.organize_translate_type_1(limit_num)

        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.random_select_translation(limit_num)

    def organize_translate_type_1(self, limit_num):
        eng_list = []

        if (len(self.always_translation_list) * len(self.eventually_translation_list)) <= \
                1/parameters.union_operation_threshold_probability * limit_num:
            # use for loop
            for eng_always in self.always_translation_list:
                for eng_eventually in self.eventually_translation_list:
                    conj = self.until_till_selection()
                    eng = eng_always + conj + eng_eventually
                    eng_list.append(eng)
        else:
            # use union operation
            eng_set_auxiliary = set()
            eng_set = set()
            while len(eng_set) < limit_num:
                # probe
                old_count = len(eng_set_auxiliary)
                eng_always = random.choice(self.always_translation_list)
                eng_eventually = random.choice(self.eventually_translation_list)
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

    def random_select_translation(self, limit_num):
        if len(self.overall_translations) > limit_num:
            random_eng_list = random.sample(self.overall_translations, limit_num)
        else:
            random_eng_list = self.overall_translations
        random.shuffle(random_eng_list)

        # overall translations
        eng_list = self.overall_translations
        rate = format(len(random_eng_list)/len(eng_list) * 100, '.4f')
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
