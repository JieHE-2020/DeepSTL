from translation.level_2.TP_atom.not_TP_atom.public_class.not_tp_atom_process.type1.not_tp_atom_type1_translator \
    import NotTPAtomType1Translator
from translation.level_2.TP_atom.not_TP_atom.public_class.not_tp_atom_process.type2.not_tp_atom_type2_translator \
    import NotTPAtomType2Translator
from translation.level_2.TP_atom.not_TP_atom.public_class.not_tp_atom_process.not_tp_atom_organizer \
    import NotTPAtomOrganizer
import copy


class NotTPAtomTranslator:

    def __init__(self, translate_guide, limit_num):
        self.translate_guide = copy.deepcopy(translate_guide)

        # use appositive
        self.type1_translator = self.type1_translate_process()
        # do not use appositive
        self.type2_translator = self.type2_translate_process()

        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.translate_organize(limit_num)

    def type1_translate_process(self):
        type1_translator = NotTPAtomType1Translator(self.translate_guide)
        return type1_translator

    def type2_translate_process(self):
        type2_translator = NotTPAtomType2Translator(self.translate_guide)
        return type2_translator

    def translate_organize(self, limit_num):
        main_sentence_type_1 = self.type1_translator.eng_main_sentence
        main_sentence_type_2 = self.type2_translator.eng_main_sentence

        not_tp_atom_organizer = NotTPAtomOrganizer(main_sentence_type_1, main_sentence_type_2, limit_num)
        self.random_selected_translations = not_tp_atom_organizer.random_selected_translations
        self.overall_translations = not_tp_atom_organizer.overall_translations
        self.selection_rate = not_tp_atom_organizer.selection_rate

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
