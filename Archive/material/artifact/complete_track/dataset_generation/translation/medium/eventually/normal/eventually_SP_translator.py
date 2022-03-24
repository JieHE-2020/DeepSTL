from translation.medium.eventually.normal.eventually_SP_preprocessor \
    import EventuallySPPreprocessor
from translation.medium.eventually.normal.eventually_SP_organizer \
    import EventuallySPOrganizer


class EventuallySPTranslator:

    def __init__(self, translate_guide, limit_num):
        self.translate_guide = translate_guide

        [self.package_list, self.template] = self.translate_preprocess(limit_num)
        [self.random_selected_translations, self.overall_translations,
         self.selection_rate] = self.translate_organize(limit_num)

    def translate_preprocess(self, limit_num):
        eventually_atom_preprocessor = EventuallySPPreprocessor(self.translate_guide, limit_num)
        self.package_list = eventually_atom_preprocessor.pack_key_list()
        self.template = eventually_atom_preprocessor.template

        return [self.package_list, self.template]

    def translate_organize(self, limit_num):
        nest_info_dict = self.translate_guide[0]['nest_info_dict']
        tp_sp_type = self.translate_guide[1]['type'][0]
        eventually_atom_organizer = EventuallySPOrganizer(self.package_list, self.template,
                                                          nest_info_dict, tp_sp_type, limit_num)
        self.random_selected_translations = eventually_atom_organizer.random_selected_translations
        self.overall_translations = eventually_atom_organizer.overall_translations
        self.selection_rate = eventually_atom_organizer.selection_rate

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
