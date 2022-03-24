from translation.level_2.TP_atom.original_TP_atom.since.normal.since_atom_historically. \
    since_atom_historically_translator import SinceAtomHistoricallyTranslator
from translation.level_2.TP_atom.original_TP_atom.since.normal.since_atom_once.since_atom_once_translator \
    import SinceAtomOnceTranslator
from translation.level_2.TP_atom.original_TP_atom.since.normal.since_atom_organizer \
    import SinceAtomOrganizer
import copy


class SinceAtomTranslator:

    def __init__(self, translate_guide, limit_num_dict):
        self.translate_guide = copy.deepcopy(translate_guide)

        limit_num = limit_num_dict['total']
        once_limit_num = limit_num_dict['once_each_type']
        historically_limit_num = limit_num_dict['historically_overall']

        self.historically_translator = self.historically_translate_process()
        self.once_translator = self.once_translate_process(once_limit_num)

        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.translate_organize(limit_num, historically_limit_num)

    def historically_translate_process(self):
        historically_translate_guide = [
            self.translate_guide['historically_instruction'],
            self.translate_guide['historically_tp_info']
        ]
        historically_translator = SinceAtomHistoricallyTranslator(historically_translate_guide)

        return historically_translator

    def once_translate_process(self, once_limit_num):
        once_translate_guide = [
            self.translate_guide['once_instruction'],
            self.translate_guide['once_tp_info']
        ]
        once_translator = SinceAtomOnceTranslator(once_translate_guide, once_limit_num)

        return once_translator

    def translate_organize(self, limit_num, historically_limit_num):
        historically_overall_translation_dict = self.historically_translator.overall_translation_dict
        once_random_translation_dict = self.once_translator.random_selected_translation_dict
        since_info_dict = self.translate_guide['since_tp_info']

        since_atom_organizer = \
            SinceAtomOrganizer(historically_overall_translation_dict, once_random_translation_dict,
                               since_info_dict, limit_num, historically_limit_num)
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
