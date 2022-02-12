from public import parameters
import copy
import random
import math


class DirectNegateOnceAtomOrganizer:

    def __init__(self, package_list, nest_info_dict, limit_num):
        self.eng_temporal_phrase = copy.deepcopy(package_list[0])
        self.eng_main_sentence_type_1 = copy.deepcopy(package_list[1])
        self.eng_temporal_clause = copy.deepcopy(package_list[2])
        self.eng_main_sentence_type_2 = copy.deepcopy(package_list[3])
        self.nest_info_dict = copy.deepcopy(nest_info_dict)

        self.translation_list_phrase = list()
        self.translation_list_clause = list()

        self.translation_list_phrase = self.phrase_directed_translate(limit_num)
        if not self.nest_info_dict['hasParallelSuccessor']:   # there is no parallel successor
            self.translation_list_clause = self.clause_directed_translate(limit_num)

        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.random_select_translation(limit_num)

    def phrase_directed_translate(self, limit_num):
        eng_list = []

        if (len(self.eng_temporal_phrase) * len(self.eng_main_sentence_type_1)) <= \
                1/parameters.union_operation_threshold_probability * limit_num:
            # use for loop
            # print('for loop of phrase')
            for phrase in self.eng_temporal_phrase:
                for main in self.eng_main_sentence_type_1:
                    eng = main + ' ' + phrase
                    eng_list.append(eng)

                    if not self.nest_info_dict['hasParallelSuccessor']:  # there is no parallel successor
                        space = self.random_comma()
                        eng = phrase + space + main
                        eng_list.append(eng)
        else:
            # use union operation
            # print('union operation of phrase')
            # ratio = limit_num / (len(self.eng_temporal_phrase) * len(self.eng_main_sentence_type_1))
            # print('ratio:', ratio)
            eng_main_phrase_set = set()
            eng_phrase_main_set = set()
            while len(eng_main_phrase_set) < limit_num:
                # do not halve limit_num for consideration if self.nest_info_dict['hasParallelSuccessor'] == True
                old_count = len(eng_main_phrase_set)
                main = random.choice(self.eng_main_sentence_type_1)
                phrase = random.choice(self.eng_temporal_phrase)
                eng = main + ' ' + phrase
                eng_main_phrase_set.add(eng)
                new_count = len(eng_main_phrase_set)

                if (new_count - old_count) == 1:
                    if not self.nest_info_dict['hasParallelSuccessor']:
                        space = self.random_comma()
                        eng = phrase + space + main
                        eng_phrase_main_set.add(eng)

            eng_list = sorted(eng_main_phrase_set) + sorted(eng_phrase_main_set)

        self.translation_list_phrase = eng_list

        return self.translation_list_phrase

    def clause_directed_translate(self, limit_num):
        eng_list = []

        if (len(self.eng_temporal_clause) * len(self.eng_main_sentence_type_2)) <= \
                1/parameters.union_operation_threshold_probability * limit_num:
            # use for loop
            # print('for loop of clause')
            for clause in self.eng_temporal_clause:
                for main in self.eng_main_sentence_type_2:
                    eng = clause + ' ' + main
                    eng_list.append(eng)
        else:
            # use union operation
            # print('union operation of clause')
            # ratio = limit_num / (len(self.eng_temporal_clause) * len(self.eng_main_sentence_type_2))
            # print('ratio:', ratio)
            eng_clause_main_set = set()
            while len(eng_clause_main_set) < limit_num:
                phrase = random.choice(self.eng_temporal_clause)
                main = random.choice(self.eng_main_sentence_type_2)
                eng = phrase + ' ' + main
                eng_clause_main_set.add(eng)
            eng_list = sorted(eng_clause_main_set)

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
    def random_comma():
        string1 = ' '
        string2 = ', '
        point = random.randint(0, 1)
        if point == 0:
            return string1
        else:
            return string2
