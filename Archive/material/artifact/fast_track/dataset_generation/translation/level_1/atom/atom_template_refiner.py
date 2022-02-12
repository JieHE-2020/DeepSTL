from template import atom_expr_template
from translation.level_1.atom.sub_obj_extractor import SubObjExtractor
from translation.level_1.atom.predicate_operation.predicate_refiner import PredicateRefiner
import copy
import random


class AtomTemplateRefiner:
    def __init__(self, info_dict, predicate_cmd_dict):
        # information about the atom expressions
        self.info_dict = copy.deepcopy(info_dict)
        # commands to operate predicates
        self.main_predicate_cmd = copy.deepcopy(predicate_cmd_dict['main'])
        self.appositive_predicate_cmd = copy.deepcopy(predicate_cmd_dict['appositive'])

        # a list containing clause type, mood, translated subject, translated predicate and translated object
        self.assemble_guide = list()

        if self.info_dict['type'] == 'SE' or 'ERE':
            category = self.info_dict['index'][0]
            sub_category = self.info_dict['index'][1]
            # the methods of class PredicateProcessor are used in this class
            self.predicate_refiner = PredicateRefiner()
            if self.info_dict['type'] == 'SE':
                self.template = copy.deepcopy(atom_expr_template.Eng_SE[category][sub_category])
                # the methods of class SubObjExtractor are used in this class
                self.sub_obj_extractor = SubObjExtractor(self.info_dict, self.template)
                self.se_distribute(category, sub_category)
            else:  # self.expr_type == 'ERE'
                self.template = copy.deepcopy(atom_expr_template.Eng_ERE[category][sub_category])
                # the methods of class SubObjExtractor are used in class TemplateRefiner
                self.sub_obj_extractor = SubObjExtractor(self.info_dict, self.template)
                self.ere_refine(category)

        self.assemble_guide.reverse()

    def se_distribute(self, category, sub_category):
        if category == 0 or category == 4:
            if sub_category == 0:
                self.se_positive_refine(category, sub_category)
            elif sub_category == 1:
                self.se_negative_refine(category, sub_category)
            else:
                self.se_not_event_refine(category, sub_category)
        elif category == 1 or category == 2:
            if 0 <= sub_category <= 1:
                self.se_positive_refine(category, sub_category)
            elif 2 <= sub_category <= 3:
                self.se_negative_refine(category, sub_category)
            else:
                self.se_not_event_refine(category, sub_category)
        else:  # category == 3 or category == 5
            if (category == 3 and 0 <= sub_category <= 3) or (category == 5 and sub_category == 0):
                self.se_positive_refine(category, sub_category)
            elif (category == 3 and 4 <= sub_category <= 7) or (category == 5 and sub_category == 1):
                self.se_negative_refine(category, sub_category)
            else:
                self.se_not_event_refine(category, sub_category)

    def se_positive_refine(self, category, sub_category):
        # process the template of subject
        subject_refined = self.sub_obj_extractor.se_sub_process()

        # process the template of predicate
        channel = 'pure_positive'
        template_key, mood = self.positive_predicate_select(channel)
        predicate_refined = self.predicate_refine(template_key, mood)

        # process the template of object
        object_refined = self.sub_obj_extractor.se_obj_process(category, sub_category, mood)

        # combine all English templates plus clause type and mood
        # the value of key 'clause_type' means there are no prefix or suffix in the translation
        refined_template_dict = {'clause_type': 'NoPrefixNoSuffix',
                                 'mood': mood,
                                 'subject_refined': subject_refined,
                                 'predicate_refined': predicate_refined,
                                 'object_refined': object_refined
                                 }
        self.assemble_guide.append(refined_template_dict)

    def se_negative_refine(self, category, sub_category):
        # process the template of subject
        subject_refined = self.sub_obj_extractor.se_sub_process()

        # process the template of negative predicate
        template_key, mood = 'predicate_negative_logic', 'negative'
        predicate_refined = self.predicate_refine(template_key, mood)

        # process the template of object
        object_refined = self.sub_obj_extractor.se_obj_process(category, sub_category, mood)

        # combine all negative English templates plus clause type and mood into a dictionary
        # and append it into self.refined_template
        # the value of key 'clause_type' means there are no prefix or suffix in the translation
        refined_template_dict = {'clause_type': 'NoPrefixNoSuffix',
                                 'mood': mood,
                                 'subject_refined': subject_refined,
                                 'predicate_refined': predicate_refined,
                                 'object_refined': object_refined
                                 }
        self.assemble_guide.append(refined_template_dict)

        # if category != 0 and category != 4:
        if category == 3 or category == 5:
            # process the template of the positive predicate
            channel = 'positive_expr_for_negative_clause'
            template_key, mood = self.positive_predicate_select(channel)
            predicate_refined = self.predicate_refine(template_key, mood)

            # process the template of object
            object_refined = self.sub_obj_extractor.se_obj_process(category, sub_category, mood)

            # combine all positive English templates plus clause type and mood into a dictionary
            # and append it into self.refined_template
            # the value of key 'clause_type' means there are no prefix or suffix in the translation
            refined_template_dict = {'clause_type': 'NoPrefixNoSuffix',
                                     'mood': mood,
                                     'subject_refined': subject_refined,
                                     'predicate_refined': predicate_refined,
                                     'object_refined': object_refined
                                     }
            self.assemble_guide.append(refined_template_dict)

    def se_not_event_refine(self, category, sub_category):
        # 1. subject_refined is the real subject
        # process the template of subject
        subject_refined = self.sub_obj_extractor.se_sub_process()

        # process the template of predicate
        template_key, mood = 'predicate_action', 'negative'
        predicate_refined = self.predicate_refine(template_key, mood)

        # process the template of object
        object_refined = self.sub_obj_extractor.se_obj_process(category, sub_category, mood)

        # combine all English templates plus clause type and mood
        # the value of key 'clause_type' means there are no prefix or suffix in the translation
        refined_template_dict = {'clause_type': 'NoPrefixNoSuffix',
                                 'mood': mood,
                                 'subject_refined': subject_refined,
                                 'predicate_refined': predicate_refined,
                                 'object_refined': object_refined
                                 }
        self.assemble_guide.append(refined_template_dict)

        # 2. prefix is the real subject
        # process the template of prefix
        prefix = self.template['prefix']

        # process the template of subject in the appositive
        subject_refined = self.sub_obj_extractor.se_sub_process()

        # process the template of predicate in the appositive
        template_key, mood = 'predicate_action', 'positive'
        slave_predicate_refined = self.predicate_refine(template_key, mood, 'appositiveEnabled')

        # process the template of object in the appositive
        object_refined = self.sub_obj_extractor.se_obj_process(category, sub_category, mood)

        # process the template of the real predicate
        template_key, mood = 'suffix_negative', 'negative'
        master_predicate_refined = self.predicate_refine(template_key, mood)

        # combine all English templates plus clause type and mood
        # the value of key 'clause_type' means there are prefix and suffix in the translation
        refined_template_dict = {'clause_type': 'PrefixSuffix',
                                 'mood': mood,
                                 'prefix': prefix,
                                 'subject_refined': subject_refined,
                                 'slave_predicate_refined': slave_predicate_refined,
                                 'object_refined': object_refined,
                                 'suffix': master_predicate_refined
                                 }
        self.assemble_guide.append(refined_template_dict)

    def ere_refine(self, category):
        # replace the template of subject and object with actual words, numbers, etc.
        [subject_refined, object_refined] = self.sub_obj_extractor.ere_sub_obj_process(category)

        # 1. subject_refined is the real subject
        template_key, mood = 'predicate_action', 'positive'
        predicate_refined = self.predicate_refine(template_key, mood)

        # combine all English templates plus clause type and mood
        # the value of key 'clause_type' means there are no prefix or suffix in the translation
        refined_template_dict = {'clause_type': 'NoPrefixNoSuffix',
                                 'mood': mood,
                                 'subject_refined': subject_refined,
                                 'predicate_refined': predicate_refined,
                                 'object_refined': object_refined
                                 }
        self.assemble_guide.append(refined_template_dict)

        # 2. prefix is the real subject
        # process the template of prefix
        prefix = self.template['prefix']

        # since subject is processed in the beginning, do not need to process it again

        # process the template of predicate in the appositive
        template_key, mood = 'predicate_action', 'positive'
        slave_predicate_refined = self.predicate_refine(template_key, mood, 'appositiveEnabled')

        # since object is processed in the beginning, do not need to process it again

        # process the template of the real predicate
        template_key, mood = 'suffix_positive', 'positive'
        master_predicate_refined = self.predicate_refine(template_key, mood)

        # combine all English templates plus clause type and mood
        # the value of key 'clause_type' means there are prefix and suffix in the translation
        refined_template_dict = {'clause_type': 'PrefixSuffix',
                                 'mood': mood,
                                 'prefix': prefix,
                                 'subject_refined': subject_refined,
                                 'slave_predicate_refined': slave_predicate_refined,
                                 'object_refined': object_refined,
                                 'suffix': master_predicate_refined
                                 }
        self.assemble_guide.append(refined_template_dict)

    @staticmethod
    def positive_predicate_select(channel):
        # positive_predicate_version == 'randomUseDuration'
        # choose positive predicate version randomly
        template_key = ''
        mood = ''

        if channel == 'pure_positive':
            point = random.randint(1, 100)
            if point <= 80:
                template_key, mood = 'predicate_logic', 'positive'
            else:
                template_key, mood = 'predicate_duration', 'positive'

        if channel == 'positive_expr_for_negative_clause':
            point = random.randint(1, 100)
            if point <= 80:
                template_key, mood = 'predicate_positive_logic', 'positive'
            else:
                template_key, mood = 'predicate_positive_duration', 'positive'

        return template_key, mood

    def predicate_refine(self, key, mood, appositive='appositiveDisabled'):
        predicate_template = copy.deepcopy(self.template[key])
        if appositive == 'appositiveDisabled':  # by default
            commands_selected = copy.deepcopy(self.main_predicate_cmd[mood])
        else:  # appositive == 'appositiveEnabled'
            commands_selected = copy.deepcopy(self.appositive_predicate_cmd[mood])
        predicate_refined = self.predicate_refiner.predicate_process(predicate_template, mood, commands_selected)
        return predicate_refined

    # def display_assemble_guide(self):
    #     assemble_guide = copy.deepcopy(self.assemble_guide)
    #     while len(assemble_guide) != 0:
    #         refined_template_dict = assemble_guide.pop()
    #         print(refined_template_dict)
    #
    #         if refined_template_dict['clause_type'] == 'NoPrefixNoSuffix':
    #             print('clause_type:', refined_template_dict['clause_type'])
    #             print('mood:', refined_template_dict['mood'])
    #             print('subject:', refined_template_dict['subject_refined'])
    #             print('predicate:', refined_template_dict['predicate_refined'])
    #             print('object:', refined_template_dict['object_refined'])
    #             print('\n')
    #
    #         if refined_template_dict['clause_type'] == 'PrefixSuffix':
    #             print('clause_type:', refined_template_dict['clause_type'])
    #             print('mood:', refined_template_dict['mood'])
    #             print('prefix:', refined_template_dict['prefix'])
    #             print('subject:', refined_template_dict['subject_refined'])
    #             print('slave_predicate:', refined_template_dict['slave_predicate_refined'])
    #             print('object:', refined_template_dict['object_refined'])
    #             print('suffix:', refined_template_dict['suffix'])
    #             print('\n')