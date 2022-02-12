import copy
import random
import math


class AlwaysEventuallyAtomOrganizer:

    def __init__(self, package_list, template, nest_info_dict, limit_num):
        self.always_eng_temporal_phrase = copy.deepcopy(package_list[0])
        self.eventually_eng_temporal_phrase = copy.deepcopy(package_list[1])
        self.eventually_eng_temporal_clause = copy.deepcopy(package_list[2])
        self.eventually_eng_main_sentence = copy.deepcopy(package_list[3])
        self.eventually_template = copy.deepcopy(template)
        self.nest_info_dict = copy.deepcopy(nest_info_dict)

        self.eventually_translation_list_phrase = list()
        self.eventually_translation_list_clause = list()

        self.eventually_translation_list_phrase = self.eventually_phrase_directed_translate()
        if not self.nest_info_dict['hasParallelSuccessor']:   # there is no parallel successor
            self.eventually_translation_list_clause = self.eventually_clause_directed_translate()

        self.random_selected_eventually_translations = self.eventually_random_select_translation(limit_num)
        self.random_selected_translations = self.random_select_translation(limit_num)

    def eventually_phrase_directed_translate(self):
        eng_list = []
        adverb_list = copy.deepcopy(self.eventually_template['adverb']['adverb'])
        for phrase in self.eventually_eng_temporal_phrase:
            for main in self.eventually_eng_main_sentence:
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

        self.eventually_translation_list_phrase = eng_list

        return self.eventually_translation_list_phrase

    def eventually_clause_directed_translate(self):
        eng_list = []
        adverb_list = copy.deepcopy(self.eventually_template['adverb']['adverb'])

        # organize
        for clause in self.eventually_eng_temporal_clause:
            for main in self.eventually_eng_main_sentence:
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

        self.eventually_translation_list_clause = eng_list

        return self.eventually_translation_list_clause

    def eventually_random_select_translation(self, limit_num):
        if not self.nest_info_dict['hasParallelSuccessor']:
            half_limit_num = math.ceil(limit_num/2)
            if len(self.eventually_translation_list_phrase) > half_limit_num:
                random_eng_list_phrase = random.sample(self.eventually_translation_list_phrase, half_limit_num)
            else:
                random_eng_list_phrase = self.eventually_translation_list_phrase

            if len(self.eventually_translation_list_clause) > (limit_num - half_limit_num):
                random_eng_list_clause = random.sample(self.eventually_translation_list_clause, limit_num-half_limit_num)
            else:
                random_eng_list_clause = self.eventually_translation_list_clause

            random_eng_list = random_eng_list_phrase + random_eng_list_clause
            random.shuffle(random_eng_list)

        else:  # self.nest_info_dict['hasParallelSuccessor'] == True
            if len(self.eventually_translation_list_phrase) > limit_num:
                random_eng_list_phrase = random.sample(self.eventually_translation_list_phrase, limit_num)
            else:
                random_eng_list_phrase = self.eventually_translation_list_phrase
            random_eng_list = random_eng_list_phrase
            random.shuffle(random_eng_list)

        return random_eng_list

    def random_select_translation(self, limit_num):
        eng_set = set()
        while len(eng_set) < limit_num:
            always = random.choice(self.always_eng_temporal_phrase)
            eventually = random.choice(self.random_selected_eventually_translations)
            space = self.random_comma()
            eng = always + space + eventually
            eng_set.add(eng)

        eng_list = sorted(eng_set)
        return eng_list

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
