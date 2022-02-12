from translation.level_3.eventually_always.normal.eventually_always_atom_preprocessor \
    import EventuallyAlwaysAtomPreprocessor
from translation.level_3.eventually_always.normal.eventually_always_atom_organizer \
    import EventuallyAlwaysAtomOrganizer


class EventuallyAlwaysAtomTranslator:

    def __init__(self, translate_guide, limit_num, whether_from_not_eventually=False):
        self.translate_guide = translate_guide
        self.whether_from_not_eventually = whether_from_not_eventually

        self.package_list = self.translate_preprocess()
        self.random_selected_translations = self.translate_organize(limit_num)

    def translate_preprocess(self):
        eventually_always_atom_preprocessor = \
            EventuallyAlwaysAtomPreprocessor(self.translate_guide, self.whether_from_not_eventually)
        self.package_list = eventually_always_atom_preprocessor.pack_key_list()

        return self.package_list

    def translate_organize(self, limit_num):
        nest_info_dict = self.translate_guide[0]['nest_info_dict']
        eventually_always_atom_organizer = EventuallyAlwaysAtomOrganizer(self.package_list, nest_info_dict, limit_num)
        random_selected_translations = eventually_always_atom_organizer.random_selected_translations

        return random_selected_translations

    def display_random_translation(self):
        print('randomly selected translation:')
        count = 1
        for eng in self.random_selected_translations:
            print('%d: %s' % (count, eng))
            count = count + 1
