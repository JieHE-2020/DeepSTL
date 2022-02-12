from translation.level_2.TP_atom.not_TP_atom.not_once.direct_negation.\
    direct_negate_once_atom_preprocessor import DirectNegateOnceAtomPreprocessor
from translation.level_2.TP_atom.not_TP_atom.not_once.direct_negation.\
    direct_negate_once_atom_organizer import DirectNegateOnceAtomOrganizer
import copy


class DirectNegateOnceAtomTranslator:

    def __init__(self, translate_guide, limit_num):
        self.translate_guide = copy.deepcopy(translate_guide)

        self.package_list = self.translate_preprocess()
        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.translate_organize(limit_num)

    def translate_preprocess(self):
        direct_negate_once_preprocessor = DirectNegateOnceAtomPreprocessor(self.translate_guide)
        self.package_list = direct_negate_once_preprocessor.pack_key_list()

        return self.package_list

    def translate_organize(self, limit_num):
        nest_info_dict = self.translate_guide['instruction_dict']['nest_info_dict']
        direct_negate_once_organizer = \
            DirectNegateOnceAtomOrganizer(self.package_list, nest_info_dict, limit_num)
        self.random_selected_translations = direct_negate_once_organizer.random_selected_translations
        self.overall_translations = direct_negate_once_organizer.overall_translations
        self.selection_rate = direct_negate_once_organizer.selection_rate

        return [self.random_selected_translations, self.overall_translations, self.selection_rate]

    def display_overall_translation(self):
        print('overall translations:')
        count = 1
        for eng in self.overall_translations:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

    def display_random_translation(self):
        print('randomly selected translation:')
        count = 1
        for eng in self.random_selected_translations:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('selection rate:', self.selection_rate)
        print('\n')
