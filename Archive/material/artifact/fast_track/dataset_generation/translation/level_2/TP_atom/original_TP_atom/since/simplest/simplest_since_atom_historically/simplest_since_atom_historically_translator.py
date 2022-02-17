from translation.level_2.TP_atom.original_TP_atom.since.simplest.simplest_since_atom_historically.\
    simplest_since_atom_historically_preprocessor import SimplestSinceAtomHistoricallyPreprocessor
from translation.level_2.TP_atom.original_TP_atom.since.simplest.simplest_since_atom_historically.\
    simplest_since_atom_historically_organizer import SimplestSinceAtomHistoricallyOrganizer


class SimplestSinceAtomHistoricallyTranslator:

    def __init__(self, translate_guide, limit_num):
        self.translate_guide = translate_guide

        self.eng_main_sentence_type1 = self.translate_preprocess()
        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.translate_organize(limit_num)

    def translate_preprocess(self):
        historically_preprocessor = SimplestSinceAtomHistoricallyPreprocessor(self.translate_guide)
        self.eng_main_sentence_type1 = historically_preprocessor.pack_key_list()

        return self.eng_main_sentence_type1

    def translate_organize(self, limit_num):
        historically_organizer = SimplestSinceAtomHistoricallyOrganizer(self.eng_main_sentence_type1, limit_num)
        self.random_selected_translations = historically_organizer.random_selected_translations
        self.overall_translations = historically_organizer.overall_translations
        self.selection_rate = historically_organizer.selection_rate

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
