import copy
import random
import math


class OnceAtomOrganizer:
    def __init__(self, package_list, template, nest_info_dict, limit_num):
        self.eng_temporal_phrase = copy.deepcopy(package_list[0])
        self.eng_temporal_clause = copy.deepcopy(package_list[1])
        self.eng_main_sentence = copy.deepcopy(package_list[2])
        self.template = copy.deepcopy(template)
        self.nest_info_dict = copy.deepcopy(nest_info_dict)

        self.translation_list_phrase = list()
        self.translation_list_clause = list()

        self.translation_list_phrase = self.phrase_directed_translate()
        if not self.nest_info_dict['hasParallelSuccessor']:   # there is no parallel successor
            self.translation_list_clause = self.clause_directed_translate()

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

                    if not self.nest_info_dict['hasParallelSuccessor']:  # there is no parallel successor
                        space = self.random_comma()
                        eng = phrase + space + main
                        eng_list.append(eng)
                else:
                    # phrase contains some word in adverb_list
                    if not self.check_repetition(main, adverb_list):
                        # if main does not contain any word in adverb_list
                        eng = main + ' ' + phrase
                        eng_list.append(eng)

                        if not self.nest_info_dict['hasParallelSuccessor']:  # there is no parallel successor
                            space = self.random_comma()
                            eng = phrase + space + main
                            eng_list.append(eng)

        self.translation_list_phrase = eng_list

        return self.translation_list_phrase

    def clause_directed_translate(self):
        eng_list = []
        adverb_list = copy.deepcopy(self.template['adverb']['adverb'])

        # organize
        for clause in self.eng_temporal_clause:
            for main in self.eng_main_sentence:
                if not self.check_repetition(clause, adverb_list):
                    # if clause does not contain any word in adverb_list
                    eng = clause + ' ' + main
                    eng_list.append(eng)
                else:
                    # clause contains some word in adverb_list
                    if not self.check_repetition(main, adverb_list):
                        # if main does not contain any word in adverb_list
                        eng = clause + ' ' + main
                        eng_list.append(eng)

        self.translation_list_clause = eng_list

        return self.translation_list_clause

    def random_select_translation(self, limit_num):
        if not self.nest_info_dict['hasParallelSuccessor']:
            half_limit_num = math.ceil(limit_num/2)
            if len(self.translation_list_phrase) > half_limit_num:
                random_eng_list_phrase = random.sample(self.translation_list_phrase, half_limit_num)
            else:
                random_eng_list_phrase = self.translation_list_phrase

            if len(self.translation_list_clause) > (limit_num - half_limit_num):
                random_eng_list_clause = random.sample(self.translation_list_clause, limit_num-half_limit_num)
            else:
                random_eng_list_clause = self.translation_list_clause

            random_eng_list = random_eng_list_phrase + random_eng_list_clause
            random.shuffle(random_eng_list)
            # overall translations
            eng_list = self.translation_list_phrase + self.translation_list_clause

        else:  # self.nest_info_dict['hasParallelSuccessor'] == True
            if len(self.translation_list_phrase) > limit_num:
                random_eng_list_phrase = random.sample(self.translation_list_phrase, limit_num)
            else:
                random_eng_list_phrase = self.translation_list_phrase
            random_eng_list = random_eng_list_phrase
            random.shuffle(random_eng_list)
            # overall translations
            eng_list = self.translation_list_phrase

        rate = format(len(random_eng_list)/len(eng_list) * 100, '.4f')
        selection_rate = str(rate) + '%'

        return [random_eng_list, eng_list, selection_rate]

    @staticmethod
    def check_repetition(expr, checked_list):
        result = False
        for scanned_word in checked_list:
            if scanned_word in expr:
                result = True

        return result

    @staticmethod
    def random_comma():
        string1 = ' '
        string2 = ', '
        point = random.randint(0, 1)
        if point == 0:
            return string1
        else:
            return string2
