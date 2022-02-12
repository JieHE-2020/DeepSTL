from translation.level_2.TP_atom.original_TP_atom.once.normal.once_atom_preprocessor import OnceAtomPreprocessor
from translation.level_2.TP_atom.original_TP_atom.once.normal.once_atom_organizer import OnceAtomOrganizer


class OnceAtomTranslator:

    def __init__(self, translate_guide, limit_num):
        self.translate_guide = translate_guide

        [self.package_list, self.template] = self.translate_preprocess()
        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.translate_organize(limit_num)

    def translate_preprocess(self):
        once_atom_preprocessor = OnceAtomPreprocessor(self.translate_guide)
        self.package_list = once_atom_preprocessor.pack_key_list()
        self.template = once_atom_preprocessor.template

        return [self.package_list, self.template]

    def translate_organize(self, limit_num):
        nest_info_dict = self.translate_guide[0]['nest_info_dict']
        once_atom_organizer = OnceAtomOrganizer(self.package_list, self.template, nest_info_dict, limit_num)
        self.random_selected_translations = once_atom_organizer.random_selected_translations
        self.overall_translations = once_atom_organizer.overall_translations
        self.selection_rate = once_atom_organizer.selection_rate

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