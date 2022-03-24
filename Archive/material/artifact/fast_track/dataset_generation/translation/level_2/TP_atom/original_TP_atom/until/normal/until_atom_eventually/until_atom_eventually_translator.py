from translation.level_2.TP_atom.original_TP_atom.until.normal.until_atom_eventually. \
    until_atom_eventually_type1_preprocessor import UntilAtomEventuallyType1Preprocessor
from translation.level_2.TP_atom.original_TP_atom.until.normal.until_atom_eventually.type2. \
    until_atom_eventually_type2_preprocessor import UntilAtomEventuallyType2Preprocessor
from translation.level_2.TP_atom.original_TP_atom.until.normal.until_atom_eventually. \
    until_atom_eventually_type3_preprocessor import UntilAtomEventuallyType3Preprocessor
from translation.level_2.TP_atom.original_TP_atom.until.normal.until_atom_eventually. \
    until_atom_eventually_type1_type3_organizer import UntilAtomEventuallyType1Type3Organizer
from translation.level_2.TP_atom.original_TP_atom.until.normal.until_atom_eventually.type2. \
    until_atom_eventually_type2_organizer import UntilAtomEventuallyType2Organizer
import copy


class UntilAtomEventuallyTranslator:

    def __init__(self, translate_guide, limit_num):
        self.translate_guide = copy.deepcopy(translate_guide)
        # extract information from self.translate_guide
        self.instruction_dict_type1 = self.translate_guide[0]['eventually_type1']
        self.instruction_dict_type2 = self.translate_guide[0]['eventually_type2']
        self.instruction_dict_type3 = self.translate_guide[0]['eventually_type3']
        self.tp_info_dict = self.translate_guide[1]

        [self.package_list_type1, self.package_list_type2, self.package_list_type3, self.template] \
            = self.translate_preprocess()

        [self.random_selected_translation_dict, self.overall_translation_info_dict] \
            = self.translate_organize(limit_num)

    def translate_preprocess(self):
        translate_guide_type1 = [self.instruction_dict_type1, self.tp_info_dict]
        eventually_preprocessor_type1 = UntilAtomEventuallyType1Preprocessor(translate_guide_type1)
        # package_list_type1: [eng_temporal_phrase, eng_temporal_clause, eng_main_sentence]
        package_list_type1 = eventually_preprocessor_type1.pack_key_list()

        translate_guide_type2 = [self.instruction_dict_type2, self.tp_info_dict]
        eventually_preprocessor_type2 = UntilAtomEventuallyType2Preprocessor(translate_guide_type2)
        # package_list_type2: [eng_main_sentence, eng_attributive_clause]
        package_list_type2 = eventually_preprocessor_type2.pack_key_list()

        translate_guide_type3 = [self.instruction_dict_type3, self.tp_info_dict]
        eventually_preprocessor_type3 = UntilAtomEventuallyType3Preprocessor(translate_guide_type3)
        # package_list_type3: [eng_temporal_phrase, eng_temporal_clause, eng_main_sentence]
        package_list_type3 = eventually_preprocessor_type3.pack_key_list()

        # type 1, type 2 and type 3 share the same template
        template = eventually_preprocessor_type3.template

        return [package_list_type1, package_list_type2, package_list_type3, template]

    def translate_organize(self, limit_num):
        nest_info_dict_type1 = self.instruction_dict_type1['nest_info_dict']
        eventually_organizer_type1 = \
            UntilAtomEventuallyType1Type3Organizer(self.package_list_type1, self.template, nest_info_dict_type1,
                                                   limit_num)
        random_selected_translations_type1 = eventually_organizer_type1.random_selected_translations
        overall_translations_type1 = eventually_organizer_type1.overall_translations
        selection_rate_type1 = eventually_organizer_type1.selection_rate

        nest_info_dict_type2 = self.instruction_dict_type2['nest_info_dict']
        eventually_organizer_type2 = \
            UntilAtomEventuallyType2Organizer(self.package_list_type2, self.template, nest_info_dict_type2, limit_num)
        random_selected_translations_type2 = eventually_organizer_type2.random_selected_translations
        overall_translations_type2 = eventually_organizer_type2.overall_translations
        selection_rate_type2 = eventually_organizer_type2.selection_rate

        nest_info_dict_type3 = self.instruction_dict_type3['nest_info_dict']
        eventually_organizer_type3 = \
            UntilAtomEventuallyType1Type3Organizer(self.package_list_type3, self.template, nest_info_dict_type3,
                                                   limit_num)
        random_selected_translations_type3 = eventually_organizer_type3.random_selected_translations
        overall_translations_type3 = eventually_organizer_type3.overall_translations
        selection_rate_type3 = eventually_organizer_type3.selection_rate

        random_selected_translation_dict = {
            'type1': random_selected_translations_type1,
            'type2': random_selected_translations_type2,
            'type3': random_selected_translations_type3
        }

        # overall_translation_info_dict = {
        #     'type1': [random_selected_translations_type1, overall_translations_type1, selection_rate_type1],
        #     'type2': [random_selected_translations_type2, overall_translations_type2, selection_rate_type2],
        #     'type3': [random_selected_translations_type3, overall_translations_type3, selection_rate_type3]
        # }

        overall_translation_info_dict = {}

        return [random_selected_translation_dict, overall_translation_info_dict]

    def display_overall_translation(self):
        print('overall translations:')

        print('type 1:')
        count = 1
        for eng in self.overall_translation_info_dict['type1'][1]:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

        print('type 2:')
        count = 1
        for eng in self.overall_translation_info_dict['type2'][1]:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

        print('type 3:')
        count = 1
        for eng in self.overall_translation_info_dict['type3'][1]:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

    def display_random_translation(self):
        print('randomly selected translation:')

        print('type 1:')
        count = 1
        for eng in self.random_selected_translation_dict['type1']:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('selection rate:', self.overall_translation_info_dict['type1'][2])
        print('\n')

        print('type 2:')
        count = 1
        for eng in self.random_selected_translation_dict['type2']:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('selection rate:', self.overall_translation_info_dict['type2'][2])
        print('\n')

        print('type 3:')
        count = 1
        for eng in self.random_selected_translation_dict['type3']:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('selection rate:', self.overall_translation_info_dict['type3'][2])
        print('\n')
