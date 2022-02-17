from translation.level_2.TP_atom.original_TP_atom.since.normal.since_atom_historically.\
    since_atom_historically_preprocessor import SinceAtomHistoricallyPreprocessor
from translation.level_2.TP_atom.original_TP_atom.since.normal.since_atom_historically.\
    since_atom_historically_organizer import SinceAtomHistoricallyOrganizer


class SinceAtomHistoricallyTranslator:

    def __init__(self, translate_guide):
        self.translate_guide = translate_guide

        self.package_list = self.translate_preprocess()
        # [self.random_selected_translations, self.overall_translations, self.selection_rate,
        #  self.overall_translation_dict] = self.translate_organize()
        self.overall_translation_dict = self.translate_organize()

    def translate_preprocess(self):
        historically_preprocessor = SinceAtomHistoricallyPreprocessor(self.translate_guide)
        self.package_list = historically_preprocessor.pack_key_list()

        return self.package_list

    def translate_organize(self):
        historically_organizer = SinceAtomHistoricallyOrganizer(self.package_list)
        # self.random_selected_translations = historically_organizer.random_selected_translations
        # self.overall_translations = historically_organizer.overall_translations
        # self.selection_rate = historically_organizer.selection_rate
        self.overall_translation_dict = historically_organizer.overall_translation_dict

        # return [self.random_selected_translations, self.overall_translations, self.selection_rate,
        #         self.overall_translation_dict]

        return self.overall_translation_dict

    # def display_overall_translation(self):
    #     print('overall translations:')
    #     count = 1
    #     for eng in self.overall_translations:
    #         print('%d: %s' % (count, eng))
    #         count = count + 1
    #     print('\n')
    #
    # def display_random_translation(self):
    #     print('randomly selected translation:')
    #     count = 1
    #     for eng in self.random_selected_translations:
    #         print('%d: %s' % (count, eng))
    #         count = count + 1
    #     print('selection rate:', self.selection_rate)
    #     print('\n')
