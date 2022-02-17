from translation.level_2.TP_atom.original_TP_atom.until.normal.until_atom_always.until_atom_always_preprocessor \
    import UntilAtomAlwaysPreprocessor
from translation.level_2.TP_atom.original_TP_atom.until.normal.until_atom_always.until_atom_always_organizer \
    import UntilAtomAlwaysOrganizer


class UntilAtomAlwaysTranslator:

    def __init__(self, translate_guide):
        self.translate_guide = translate_guide

        self.package_list = self.translate_preprocess()
        # [self.random_selected_translations, self.overall_translations, self.selection_rate,
        #  self.overall_translation_dict] = self.translate_organize()
        self.overall_translation_dict = self.translate_organize()

    def translate_preprocess(self):
        always_preprocessor = UntilAtomAlwaysPreprocessor(self.translate_guide)
        self.package_list = always_preprocessor.pack_key_list()

        return self.package_list

    def translate_organize(self):
        always_organizer = UntilAtomAlwaysOrganizer(self.package_list)
        # self.random_selected_translations = always_organizer.random_selected_translations
        # self.overall_translations = always_organizer.overall_translations
        # self.selection_rate = always_organizer.selection_rate
        self.overall_translation_dict = always_organizer.overall_translation_dict

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
