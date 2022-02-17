from translation.level_2.TP_atom.not_TP_atom.not_once.direct_negation.direct_negate_once_atom_translator \
    import DirectNegateOnceAtomTranslator
from translation.level_2.TP_atom.not_TP_atom.not_once.appositive_appendix.\
    appositive_appendix_negate_once_atom_handler import AppositiveAppendixNegateOnceAtomHandler
from translation.level_2.TP_atom.original_TP_atom.historically.normal.historically_atom_translator \
    import HistoricallyAtomTranslator
import copy
import math
import random


class NotOnceAtomTranslator:

    def __init__(self, translate_guide, limit_num, distribution_vector):
        self.translate_guide = copy.deepcopy(translate_guide)
        self.limit_num = copy.deepcopy(limit_num)
        self.distribution_vector = copy.deepcopy(distribution_vector)

        # check feasibility of direct negation
        self.direct_negation_feasibility = self.check_direct_negation_feasibility()

        self.random_shuffled_translations = self.translate_coordinate()

    def translate_coordinate(self):
        # # option 1 - support transformation
        # # process translation according to the truth value of self.direct_negation_feasibility
        # if self.direct_negation_feasibility:
        #     distribution = self.distribution_vector['with_direct_negate']
        #
        #     # direct negation
        #     direct_negate_limit_num = math.ceil(self.limit_num * distribution[0])
        #     direct_negate_translator = self.direct_negate_translate_process(direct_negate_limit_num)
        #     # note that it is likely that len(eng_direct_negate_list) is smaller than direct_negate_limit_num
        #     # because there are no variations of adverbial modifiers
        #     eng_direct_negate_list = direct_negate_translator.random_selected_translations
        #
        #     # use appositive and appendix
        #     appositive_appendix_limit_num = math.ceil(self.limit_num * distribution[1])
        #     appositive_appendix_translator = self.appositive_appendix_translate_process(appositive_appendix_limit_num)
        #     eng_appositive_appendix_list = appositive_appendix_translator.random_selected_translations
        #
        #     # use transformation
        #     transform_limit_num = self.limit_num - len(eng_direct_negate_list) - len(eng_appositive_appendix_list)
        #     transform_translator = self.transform_translate_process(transform_limit_num)
        #     eng_transform_list = transform_translator.random_selected_translations
        #
        #     random_shuffled_translations = eng_direct_negate_list + eng_appositive_appendix_list + eng_transform_list
        #     random.shuffle(random_shuffled_translations)
        #
        # else:
        #     distribution = self.distribution_vector['without_direct_negate']
        #
        #     # use appositive and appendix
        #     appositive_appendix_limit_num = math.ceil(self.limit_num * distribution[0])
        #     appositive_appendix_translator = self.appositive_appendix_translate_process(appositive_appendix_limit_num)
        #     eng_appositive_appendix_list = appositive_appendix_translator.random_selected_translations
        #
        #     # use transformation
        #     transform_limit_num = self.limit_num - len(eng_appositive_appendix_list)
        #     transform_translator = self.transform_translate_process(transform_limit_num)
        #     eng_transform_list = transform_translator.random_selected_translations
        #
        #     random_shuffled_translations = eng_appositive_appendix_list + eng_transform_list
        #     random.shuffle(random_shuffled_translations)

        # option 2 - do not support transformation
        # process translation according to the truth value of self.direct_negation_feasibility
        if self.direct_negation_feasibility:
            distribution = self.distribution_vector['with_direct_negate']

            # direct negation
            direct_negate_limit_num = math.ceil(self.limit_num * distribution[0])
            direct_negate_translator = self.direct_negate_translate_process(direct_negate_limit_num)
            # note that it is likely that len(eng_direct_negate_list) is smaller than direct_negate_limit_num
            # because there are no variations of adverbial modifiers
            eng_direct_negate_list = direct_negate_translator.random_selected_translations

            # use appositive and appendix
            appositive_appendix_limit_num = self.limit_num - len(eng_direct_negate_list)
            appositive_appendix_translator = self.appositive_appendix_translate_process(appositive_appendix_limit_num)
            eng_appositive_appendix_list = appositive_appendix_translator.random_selected_translations

            random_shuffled_translations = eng_direct_negate_list + eng_appositive_appendix_list
            random.shuffle(random_shuffled_translations)

        else:
            distribution = self.distribution_vector['without_direct_negate']

            # use appositive and appendix
            appositive_appendix_limit_num = math.ceil(self.limit_num * self.limit_num * distribution[0])
            appositive_appendix_translator = self.appositive_appendix_translate_process(appositive_appendix_limit_num)
            eng_appositive_appendix_list = appositive_appendix_translator.random_selected_translations

            random_shuffled_translations = eng_appositive_appendix_list
            random.shuffle(random_shuffled_translations)

        return random_shuffled_translations

    def direct_negate_translate_process(self, direct_negate_limit_num):
        direct_negate_translator = DirectNegateOnceAtomTranslator(self.translate_guide, direct_negate_limit_num)

        return direct_negate_translator

    def appositive_appendix_translate_process(self, appositive_appendix_limit_num):
        appositive_appendix_handler = \
            AppositiveAppendixNegateOnceAtomHandler(self.translate_guide, appositive_appendix_limit_num)
        appositive_appendix_translator = appositive_appendix_handler.appositive_appendix_negate_once_atom_translator

        return appositive_appendix_translator

    def transform_translate_process(self, transform_limit_num):
        historically_not_instruction = {
            'position': self.translate_guide['instruction_dict']['position'],
            'adverbial_query_main_type1': 'adverbialEnabled',
            'adverbial_query_main_type2_main_part': 'adverbialDisabled',
            'nest_info_dict': self.translate_guide['instruction_dict']['nest_info_dict']
        }
        guide = [historically_not_instruction, self.translate_guide['historically_not_info_dict']]
        whether_from_not_once = True
        # not (once expr) -> historically (not expr)
        transform_translator = HistoricallyAtomTranslator(guide, transform_limit_num, whether_from_not_once)

        return transform_translator

    def check_direct_negation_feasibility(self):
        feasibility = False
        not_once_info_dict = self.translate_guide['not_once_info_dict']
        sp_info_dict = not_once_info_dict['ingredient'][0]
        atom_type = sp_info_dict['type']

        if atom_type == 'ERE':
            feasibility = True
        else:  # atom_type == 'SE'
            index = sp_info_dict['index']
            SE_condition = (index == [0, 0]) or \
                           (index == [1, 0]) or (index == [1, 1]) or \
                           (index == [2, 0]) or (index == [2, 1]) or \
                           (index == [3, 0]) or (index == [3, 1]) or (index == [3, 2]) or (index == [3, 3]) or \
                           (index == [4, 0]) or \
                           (index == [5, 0])
            if SE_condition:
                feasibility = True

        return feasibility

    def display_random_translation(self):
        print('randomly shuffled translation:')
        count = 1
        for eng in self.random_shuffled_translations:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')
