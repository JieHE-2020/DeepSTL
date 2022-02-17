from translation.level_1.atom.atom_template_refiner import AtomTemplateRefiner
from translation.level_1.atom.atom_assembler import AtomAssembler
import copy
import random


class AtomTranslator:

    def __init__(self, translate_guide, limit_num):
        self.instruction_dict = copy.deepcopy(translate_guide[0])
        self.atom_info_dict = copy.deepcopy(translate_guide[1])
        self.adverbial_dict = copy.deepcopy(translate_guide[2])
        self.predicate_cmd_dict = copy.deepcopy(translate_guide[3])

        [self.assemble_guide, self.random_selected_translations, self.overall_translations, self.selection_rate] \
            = self.translate_process(limit_num)

    def translate_process(self, limit_num):
        # get all translations
        refiner = AtomTemplateRefiner(self.atom_info_dict, self.predicate_cmd_dict)
        assemble_guide = refiner.assemble_guide

        adverbial_query = self.instruction_dict['adverbial_query']
        adverbial_para = copy.deepcopy(self.adverbial_dict['assemble_list'])
        assembler = AtomAssembler(adverbial_query, refiner.assemble_guide, adverbial_para)
        overall_eng_list = assembler.eng_list

        # random selection
        if len(overall_eng_list) > limit_num:
            random_eng_list = random.sample(overall_eng_list, limit_num)
        else:
            random_eng_list = copy.deepcopy(overall_eng_list)
        random.shuffle(random_eng_list)

        rate = format(len(random_eng_list) / len(overall_eng_list) * 100, '.4f')
        selection_rate = str(rate) + '%'

        return [assemble_guide, random_eng_list, overall_eng_list, selection_rate]

    def display_assemble_guide(self):
        assemble_guide = copy.deepcopy(self.assemble_guide)
        while len(assemble_guide) != 0:
            refined_template_dict = assemble_guide.pop()
            print(refined_template_dict)

            if refined_template_dict['clause_type'] == 'NoPrefixNoSuffix':
                print('clause_type:', refined_template_dict['clause_type'])
                print('mood:', refined_template_dict['mood'])
                print('subject:', refined_template_dict['subject_refined'])
                print('predicate:', refined_template_dict['predicate_refined'])
                print('object:', refined_template_dict['object_refined'])
                print('\n')

            if refined_template_dict['clause_type'] == 'PrefixSuffix':
                print('clause_type:', refined_template_dict['clause_type'])
                print('mood:', refined_template_dict['mood'])
                print('prefix:', refined_template_dict['prefix'])
                print('subject:', refined_template_dict['subject_refined'])
                print('slave_predicate:', refined_template_dict['slave_predicate_refined'])
                print('object:', refined_template_dict['object_refined'])
                print('suffix:', refined_template_dict['suffix'])
                print('\n')

    def display_translation(self):
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
