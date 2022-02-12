import copy
import random


class UntilAtomEventuallyType2Organizer:
    def __init__(self, package_list, template, nest_info_dict, limit_num):
        self.eng_main_sentence = copy.deepcopy(package_list[0])
        self.eng_attributive_clause = copy.deepcopy(package_list[1])
        self.template = copy.deepcopy(template)
        self.nest_info_dict = copy.deepcopy(nest_info_dict)

        if not self.nest_info_dict['hasParallelSuccessor']:   # there is no parallel successor
            self.translation_list = self.attributive_clause_appended_translate()
            [self.random_selected_translations, self.overall_translations,
             self.selection_rate] = self.random_select_translation(limit_num)
        else:
            self.translation_list = []
            self.random_selected_translations = []
            self.overall_translations = []
            self.selection_rate = '0%'

    def attributive_clause_appended_translate(self):
        eng_list = []
        adverb_list = copy.deepcopy(self.template['adverb']['adverb'])

        # organize
        for main in self.eng_main_sentence:
            for clause in self.eng_attributive_clause:
                if not self.check_repetition(main, adverb_list):
                    # if main does not contain any word in adverb_list
                    eng = main + ', ' + clause
                    eng_list.append(eng)
                else:
                    # main contains some word in adverb_list
                    if not self.check_repetition(clause, adverb_list):
                        # if clause does not contain any word in adverb_list
                        eng = main + ', ' + clause
                        eng_list.append(eng)

        return eng_list

    def random_select_translation(self, limit_num):
        if len(self.translation_list) > limit_num:
            random_eng_list = random.sample(self.translation_list, limit_num)
        else:
            random_eng_list = self.translation_list
        random.shuffle(random_eng_list)
        # overall translations
        eng_list = self.translation_list

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
