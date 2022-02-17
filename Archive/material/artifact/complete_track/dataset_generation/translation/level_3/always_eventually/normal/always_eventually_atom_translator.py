from translation.level_3.always_eventually.normal.always_eventually_atom_preprocessor \
    import AlwaysEventuallyAtomPreprocessor
from translation.level_3.always_eventually.normal.always_eventually_atom_organizer \
    import AlwaysEventuallyAtomOrganizer


class AlwaysEventuallyAtomTranslator:

    def __init__(self, translate_guide, limit_num):
        self.translate_guide = translate_guide

        [self.package_list, self.template] = self.translate_preprocess()
        self.random_selected_translations = self.translate_organize(limit_num)

    def translate_preprocess(self):
        always_eventually_atom_preprocessor = AlwaysEventuallyAtomPreprocessor(self.translate_guide)
        self.package_list = always_eventually_atom_preprocessor.pack_key_list()
        self.template = self.package_list[-1]

        return [self.package_list, self.template]

    def translate_organize(self, limit_num):
        nest_info_dict = self.translate_guide[0]['nest_info_dict']
        always_eventually_atom_organizer = \
            AlwaysEventuallyAtomOrganizer(self.package_list, self.template, nest_info_dict, limit_num)
        random_selected_translations = always_eventually_atom_organizer.random_selected_translations

        return random_selected_translations

    def display_random_translation(self):
        print('randomly selected translation:')
        count = 1
        for eng in self.random_selected_translations:
            print('%d: %s' % (count, eng))
            count = count + 1
