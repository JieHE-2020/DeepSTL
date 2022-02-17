from translation.level_2.TP_atom.original_TP_atom.until.simplest.simplest_until_atom_always.\
    simplest_until_atom_always_translator import SimplestUntilAtomAlwaysTranslator
from translation.level_2.TP_atom.original_TP_atom.until.simplest.simplest_until_atom_eventually.\
    simplest_until_atom_eventually_translator import SimplestUntilAtomEventuallyTranslator
from translation.level_2.TP_atom.original_TP_atom.until.simplest.simplest_until_atom_organizer \
    import SimplestUntilAtomOrganizer
import copy


class SimplestUntilAtomTranslator:

    def __init__(self, translate_guide, limit_num_dict):
        self.translate_guide = copy.deepcopy(translate_guide)

        limit_num = limit_num_dict['total']
        always_limit_num = limit_num_dict['always']
        eventually_limit_num = limit_num_dict['eventually']

        self.always_translator = self.always_translate_process(always_limit_num)
        self.eventually_translator = self.eventually_translate_process(eventually_limit_num)

        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.translate_organize(limit_num)

    def always_translate_process(self, always_limit_num):
        always_translate_guide = [
            self.translate_guide['always_instruction'],
            self.translate_guide['always_tp_info']
        ]
        always_translator = SimplestUntilAtomAlwaysTranslator(always_translate_guide, always_limit_num)

        return always_translator

    def eventually_translate_process(self, eventually_limit_num):
        eventually_translate_guide = [
            self.translate_guide['eventually_instruction'],
            self.translate_guide['eventually_tp_info']
        ]
        eventually_translator = SimplestUntilAtomEventuallyTranslator(eventually_translate_guide, eventually_limit_num)

        return eventually_translator

    def translate_organize(self, limit_num):
        always_translation_list = self.always_translator.random_selected_translations
        eventually_translation_list = self.eventually_translator.random_selected_translations

        until_atom_organizer = \
            SimplestUntilAtomOrganizer(always_translation_list, eventually_translation_list, limit_num)
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
