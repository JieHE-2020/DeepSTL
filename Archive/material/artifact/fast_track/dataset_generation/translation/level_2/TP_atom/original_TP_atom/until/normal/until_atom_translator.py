from translation.level_2.TP_atom.original_TP_atom.until.normal.until_atom_always.until_atom_always_translator \
    import UntilAtomAlwaysTranslator
from translation.level_2.TP_atom.original_TP_atom.until.normal.until_atom_eventually.until_atom_eventually_translator \
    import UntilAtomEventuallyTranslator
from translation.level_2.TP_atom.original_TP_atom.until.normal.until_atom_organizer import UntilAtomOrganizer
import copy


class UntilAtomTranslator:

    def __init__(self, translate_guide, limit_num_dict):
        self.translate_guide = copy.deepcopy(translate_guide)

        limit_num = limit_num_dict['total']
        eventually_limit_num = limit_num_dict['eventually_each_type']
        always_limit_num = limit_num_dict['always_overall']

        self.always_translator = self.always_translate_process()
        self.eventually_translator = self.eventually_translate_process(eventually_limit_num)

        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.translate_organize(limit_num, always_limit_num)

    def always_translate_process(self):
        always_translate_guide = [
            self.translate_guide['always_instruction'],
            self.translate_guide['always_tp_info']
        ]

        always_translator = UntilAtomAlwaysTranslator(always_translate_guide)

        return always_translator

    def eventually_translate_process(self, eventually_limit_num):
        eventually_translate_guide = [
            self.translate_guide['eventually_instruction'],
            self.translate_guide['eventually_tp_info']
        ]
        eventually_translator = UntilAtomEventuallyTranslator(eventually_translate_guide, eventually_limit_num)

        return eventually_translator

    def translate_organize(self, limit_num, always_limit_num):
        always_overall_translation_dict = self.always_translator.overall_translation_dict
        eventually_random_translation_dict = self.eventually_translator.random_selected_translation_dict
        until_info_dict = self.translate_guide['until_tp_info']

        until_atom_organizer = \
            UntilAtomOrganizer(always_overall_translation_dict, eventually_random_translation_dict,
                               until_info_dict, limit_num, always_limit_num)
        self.random_selected_translations = until_atom_organizer.random_selected_translations
        self.overall_translations = until_atom_organizer.overall_translations
        self.selection_rate = until_atom_organizer.selection_rate

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
