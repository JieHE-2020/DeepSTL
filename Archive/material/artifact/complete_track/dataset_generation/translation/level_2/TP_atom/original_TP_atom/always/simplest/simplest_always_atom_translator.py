from translation.level_2.TP_atom.original_TP_atom.always.simplest.simplest_always_atom_preprocessor \
    import SimplestAlwaysAtomPreprocessor
from translation.level_2.TP_atom.original_TP_atom.always.simplest.simplest_always_atom_organizer \
    import SimplestAlwaysAtomOrganizer


class SimplestAlwaysAtomTranslator:

    def __init__(self, translate_guide, limit_num, whether_from_not_eventually=False):
        self.translate_guide = translate_guide
        self.whether_from_not_eventually = whether_from_not_eventually

        self.package_list = self.translate_preprocess()
        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.translate_organize(limit_num)

    def translate_preprocess(self):
        always_atom_preprocessor = SimplestAlwaysAtomPreprocessor(self.translate_guide, self.whether_from_not_eventually)
        self.package_list = always_atom_preprocessor.pack_key_list()

        return self.package_list

    def translate_organize(self, limit_num):
        always_atom_organizer = SimplestAlwaysAtomOrganizer(self.package_list, limit_num)
        self.random_selected_translations = always_atom_organizer.random_selected_translations
        self.overall_translations = always_atom_organizer.overall_translations
        self.selection_rate = always_atom_organizer.selection_rate

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
