from translation.level_2.TP_atom.not_TP_atom.public_class.not_continuation_atom_process.\
    not_continuation_atom_preprocessor import NotContinuationAtomPreprocessor
from translation.level_2.TP_atom.not_TP_atom.public_class.not_continuation_atom_process.\
    not_continuation_atom_organizer import NotContinuationAtomOrganizer


class NotContinuationAtomTranslator:

    def __init__(self, translate_guide, limit_num):
        self.translate_guide = translate_guide

        self.package_list = self.translate_preprocess()
        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.translate_organize(limit_num)

    def translate_preprocess(self):
        not_continuation_preprocessor = NotContinuationAtomPreprocessor(self.translate_guide)
        self.package_list = not_continuation_preprocessor.pack_key_list()

        return self.package_list

    def translate_organize(self, limit_num):
        nest_info_dict = self.translate_guide[0]['nest_info_dict']
        not_continuation_organizer = NotContinuationAtomOrganizer(self.package_list, nest_info_dict, limit_num)
        self.random_selected_translations = not_continuation_organizer.random_selected_translations
        self.overall_translations = not_continuation_organizer.overall_translations
        self.selection_rate = not_continuation_organizer.selection_rate

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
