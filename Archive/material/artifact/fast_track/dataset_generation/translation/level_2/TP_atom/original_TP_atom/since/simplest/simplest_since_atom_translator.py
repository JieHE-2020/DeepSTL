from translation.level_2.TP_atom.original_TP_atom.since.simplest.simplest_since_atom_historically.\
    simplest_since_atom_historically_translator import SimplestSinceAtomHistoricallyTranslator
from translation.level_2.TP_atom.original_TP_atom.since.simplest.simplest_since_atom_once.\
    simplest_since_atom_once_translator import SimplestSinceAtomOnceTranslator
from translation.level_2.TP_atom.original_TP_atom.since.simplest.simplest_since_atom_organizer \
    import SimplestSinceAtomOrganizer
import copy


class SimplestSinceAtomTranslator:

    def __init__(self, translate_guide, limit_num_dict):
        self.translate_guide = copy.deepcopy(translate_guide)

        limit_num = limit_num_dict['total']
        historically_limit_num = limit_num_dict['historically']
        once_limit_num = limit_num_dict['once']

        self.historically_translator = self.historically_translate_process(historically_limit_num)
        self.once_translator = self.once_translate_process(once_limit_num)

        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.translate_organize(limit_num)

    def historically_translate_process(self, historically_limit_num):
        historically_translate_guide = [
            self.translate_guide['historically_instruction'],
            self.translate_guide['historically_tp_info']
        ]
        historically_translator = \
            SimplestSinceAtomHistoricallyTranslator(historically_translate_guide, historically_limit_num)

        return historically_translator

    def once_translate_process(self, once_limit_num):
        once_translate_guide = [
            self.translate_guide['once_instruction'],
            self.translate_guide['once_tp_info']
        ]
        once_translator = SimplestSinceAtomOnceTranslator(once_translate_guide, once_limit_num)

        return once_translator

    def translate_organize(self, limit_num):
        historically_translation_list = self.historically_translator.random_selected_translations
        once_translation_list = self.once_translator.random_selected_translations

        since_atom_organizer = \
            SimplestSinceAtomOrganizer(historically_translation_list, once_translation_list, limit_num)
        self.random_selected_translations = since_atom_organizer.random_selected_translations
        self.overall_translations = since_atom_organizer.overall_translations
        self.selection_rate = since_atom_organizer.selection_rate

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
