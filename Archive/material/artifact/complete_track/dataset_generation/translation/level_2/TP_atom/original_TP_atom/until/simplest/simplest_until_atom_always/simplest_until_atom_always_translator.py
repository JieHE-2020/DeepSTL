from translation.level_2.TP_atom.original_TP_atom.until.simplest.simplest_until_atom_always.\
    simplest_until_atom_always_preprocessor import SimplestUntilAtomAlwaysPreprocessor
from translation.level_2.TP_atom.original_TP_atom.until.simplest.simplest_until_atom_always.\
    simplest_until_atom_always_organizer import SimplestUntilAtomAlwaysOrganizer


class SimplestUntilAtomAlwaysTranslator:

    def __init__(self, translate_guide, limit_num):
        self.translate_guide = translate_guide

        self.eng_main_sentence_type1 = self.translate_preprocess()
        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.translate_organize(limit_num)

    def translate_preprocess(self):
        always_preprocessor = SimplestUntilAtomAlwaysPreprocessor(self.translate_guide)
        self.eng_main_sentence_type1 = always_preprocessor.pack_key_list()

        return self.eng_main_sentence_type1

    def translate_organize(self, limit_num):
        always_organizer = SimplestUntilAtomAlwaysOrganizer(self.eng_main_sentence_type1, limit_num)
        self.random_selected_translations = always_organizer.random_selected_translations
        self.overall_translations = always_organizer.overall_translations
        self.selection_rate = always_organizer.selection_rate

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
