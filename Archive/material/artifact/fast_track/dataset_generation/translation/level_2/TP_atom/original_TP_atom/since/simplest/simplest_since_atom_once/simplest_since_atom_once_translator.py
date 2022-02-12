from translation.level_2.TP_atom.original_TP_atom.since.simplest.simplest_since_atom_once.\
    simplest_since_atom_once_preprocessor import SimplestSinceAtomOncePreprocessor
from translation.level_2.TP_atom.original_TP_atom.since.simplest.simplest_since_atom_once.\
    simplest_since_atom_once_organizer import SimplestSinceAtomOnceOrganizer


class SimplestSinceAtomOnceTranslator:

    def __init__(self, translate_guide, limit_num):
        self.translate_guide = translate_guide

        [self.package_list, self.template] = self.translate_preprocess()
        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.translate_organize(limit_num)

    def translate_preprocess(self):
        once_preprocessor = SimplestSinceAtomOncePreprocessor(self.translate_guide)
        self.package_list = once_preprocessor.pack_key_list()
        self.template = once_preprocessor.template

        return [self.package_list, self.template]

    def translate_organize(self, limit_num):
        once_organizer = SimplestSinceAtomOnceOrganizer(self.package_list, self.template, limit_num)
        self.random_selected_translations = once_organizer.random_selected_translations
        self.overall_translations = once_organizer.overall_translations
        self.selection_rate = once_organizer.selection_rate

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
