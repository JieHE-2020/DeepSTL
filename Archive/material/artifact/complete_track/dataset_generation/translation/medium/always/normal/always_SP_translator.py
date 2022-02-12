from translation.medium.always.normal.always_SP_preprocessor import AlwaysSPPreprocessor
from translation.medium.always.normal.always_SP_organizer import AlwaysSPOrganizer


class AlwaysSPTranslator:

    def __init__(self, translate_guide, limit_num, whether_from_not_eventually=False):
        self.translate_guide = translate_guide
        self.whether_from_not_eventually = whether_from_not_eventually

        self.package_list = self.translate_preprocess(limit_num)
        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.translate_organize(limit_num)

    def translate_preprocess(self, limit_num):
        always_atom_preprocessor = AlwaysSPPreprocessor(self.translate_guide, limit_num,
                                                        self.whether_from_not_eventually)
        self.package_list = always_atom_preprocessor.pack_key_list()

        return self.package_list

    def translate_organize(self, limit_num):
        nest_info_dict = self.translate_guide[0]['nest_info_dict']
        tp_sp_type = self.translate_guide[1]['type'][0]
        always_atom_organizer = AlwaysSPOrganizer(self.package_list,
                                                  nest_info_dict, tp_sp_type, limit_num)
        self.random_selected_translations = always_atom_organizer.random_selected_translations
        self.overall_translations = always_atom_organizer.overall_translations
        self.selection_rate = always_atom_organizer.selection_rate

        def capitalize(sentence):
            return sentence.capitalize()

        self.random_selected_translations = list(map(capitalize, self.random_selected_translations))
        # self.overall_translations = list(map(capitalize, self.overall_translations))  # do not map considering speed

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