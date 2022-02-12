import copy
import random


class SimplestEventuallyAtomOrganizer:

    def __init__(self, package_list, template, limit_num):
        self.eng_temporal_phrase = copy.deepcopy(package_list[0])
        self.eng_main_sentence = copy.deepcopy(package_list[1])
        self.template = copy.deepcopy(template)

        self.translation_list_phrase = self.phrase_directed_translate()

        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.random_select_translation(limit_num)

    def phrase_directed_translate(self):
        eng_list = []
        adverb_list = copy.deepcopy(self.template['adverb']['adverb'])
        for phrase in self.eng_temporal_phrase:
            for main in self.eng_main_sentence:
                if not self.check_repetition(phrase, adverb_list):
                    # if phrase does not contain any word in adverb_list
                    eng = main + ' ' + phrase
                    eng_list.append(eng)
                else:
                    # phrase contains some word in adverb_list
                    if not self.check_repetition(main, adverb_list):
                        # if main does not contain any word in adverb_list
                        eng = main + ' ' + phrase
                        eng_list.append(eng)

        return eng_list

    def random_select_translation(self, limit_num):
        if len(self.translation_list_phrase) > limit_num:
            random_eng_list_phrase = random.sample(self.translation_list_phrase, limit_num)
        else:
            random_eng_list_phrase = self.translation_list_phrase
        random_eng_list = random_eng_list_phrase
        random.shuffle(random_eng_list)
        # overall translations
        eng_list = self.translation_list_phrase

        rate = format(len(random_eng_list) / len(eng_list) * 100, '.4f')
        selection_rate = str(rate) + '%'

        return [random_eng_list, eng_list, selection_rate]

    @staticmethod
    def check_repetition(expr, checked_list):
        result = False
        for scanned_word in checked_list:
            if scanned_word in expr:
                result = True

        return result
