from translation.level_2.TP_atom.original_TP_atom.historically.normal.historically_atom_preprocessor \
    import HistoricallyAtomPreprocessor
from translation.level_2.TP_atom.original_TP_atom.historically.normal.historically_atom_organizer \
    import HistoricallyAtomOrganizer


class HistoricallyAtomTranslator:

    def __init__(self, translate_guide, limit_num, whether_from_not_once=False):
        self.translate_guide = translate_guide
        self.whether_from_not_once = whether_from_not_once

        self.package_list = self.translate_preprocess()
        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.translate_organize(limit_num)

    def translate_preprocess(self):
        historically_atom_preprocessor = HistoricallyAtomPreprocessor(self.translate_guide, self.whether_from_not_once)
        self.package_list = historically_atom_preprocessor.pack_key_list()

        return self.package_list

    def translate_organize(self, limit_num):
        nest_info_dict = self.translate_guide[0]['nest_info_dict']
        historically_atom_organizer = HistoricallyAtomOrganizer(self.package_list, nest_info_dict, limit_num)
        self.random_selected_translations = historically_atom_organizer.random_selected_translations
        self.overall_translations = historically_atom_organizer.overall_translations
        self.selection_rate = historically_atom_organizer.selection_rate

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