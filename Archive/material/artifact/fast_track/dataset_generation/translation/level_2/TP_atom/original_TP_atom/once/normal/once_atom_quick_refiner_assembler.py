from translation.level_1.atom.predicate_operation.predicate_refiner import PredicateRefiner
import copy
import random


class OnceAtomQuickRefinerAssembler:
    def __init__(self, template, predicate_cmd_dict, adverbial_para):
        # information about the atom expressions
        self.template = copy.deepcopy(template)
        # commands to operate predicate (with adverb modification)
        self.predicate_cmd = copy.deepcopy(predicate_cmd_dict)
        # adverbial list
        self.adverbial_para = copy.deepcopy(adverbial_para)

        # the methods of class PredicateProcessor are used in this class
        self.predicate_refiner = PredicateRefiner()

        # a list containing mood, translated subject, translated predicate and translated object
        self.assemble_guide = list()
        # a list containing the assembling results, namely English translation, of the refined template
        self.eng_list = list()

        self.assemble_guide = self.clause_refine()
        self.assemble_guide.reverse()
        self.eng_list = self.clause_assemble()

    def clause_refine(self):
        subject_refined = copy.deepcopy(self.template['subject'])
        template_key, mood = 'predicate', 'positive'
        predicate_refined = self.predicate_refine(template_key, mood)
        object_refined = copy.deepcopy(self.template['object'])
        conjunction_refined = copy.deepcopy(self.template['conjunction'])
        refined_template_dict = {'mood': mood,
                                 'subject_refined': subject_refined,
                                 'predicate_refined': predicate_refined,
                                 'object_refined': object_refined,
                                 'conjunction_refined': conjunction_refined
                                 }
        self.assemble_guide.append(refined_template_dict)

        return self.assemble_guide

    def predicate_refine(self, template_key, mood):
        predicate_template = copy.deepcopy(self.template[template_key])
        commands_selected = self.predicate_cmd[mood]
        predicate_refined = self.predicate_refiner.predicate_process(predicate_template, mood, commands_selected)
        return predicate_refined

    def clause_assemble(self):
        assemble_guide = copy.deepcopy(self.assemble_guide)
        while len(assemble_guide) != 0:
            refined_template_dict = assemble_guide.pop()
            self.assemble_process(refined_template_dict)

        return self.eng_list

    def assemble_process(self, refined_template_dict):
        # mood = refined_template_dict['mood']
        subject_refined = refined_template_dict['subject_refined']
        predicate_refined = refined_template_dict['predicate_refined']
        object_refined = refined_template_dict['object_refined']
        conjunction_refined = refined_template_dict['conjunction_refined']

        for i in range(len(predicate_refined)):
            for predicate in predicate_refined[i]:
                clause_para = [subject_refined, predicate, object_refined]
                eng_main = self.random_select(clause_para)
                eng = eng_main + conjunction_refined
                self.eng_list.append(eng)

                # check whether 'predicate' contains any adverb in self.adverbial_para
                flag = 0
                for scanned_word in self.adverbial_para:
                    if scanned_word in predicate:
                        flag = 1
                # If flag == 0, then 'predicate' doesn't contain any word in the adverbial list.
                # Generate new translations with adverbs and adverbial phrases.
                if flag == 0:
                    eng_list_adverbialAdded = self.adverbial_augment(clause_para, conjunction_refined)
                    self.eng_list = self.eng_list + eng_list_adverbialAdded

    def adverbial_augment(self, clause_para, conjunction_refined):
        eng_list_adverbialAdded = []

        for word in self.adverbial_para:
            eng_main = self.random_select(clause_para)
            eng_update = word + ' ' + eng_main + conjunction_refined
            eng_list_adverbialAdded.append(eng_update)

            eng_main = self.random_select(clause_para)
            eng_update = eng_main + ' ' + word + conjunction_refined
            eng_list_adverbialAdded.append(eng_update)

        return eng_list_adverbialAdded

    @staticmethod
    def random_select(clause_para):
        # randomly choose a subject in the 'subject_refined' list
        eng_subject = random.choice(clause_para[0])
        eng_predicate = clause_para[1]
        # randomly choose an object in the 'object_refined' list
        eng_object = random.choice(clause_para[2])
        eng = eng_subject + ' ' + eng_predicate + ' ' + eng_object

        return eng

    def display_assemble_guide(self):
        assemble_guide = copy.deepcopy(self.assemble_guide)
        while len(assemble_guide) != 0:
            refined_template_dict = assemble_guide.pop()
            print(refined_template_dict)
            print('mood:', refined_template_dict['mood'])
            print('subject:', refined_template_dict['subject_refined'])
            print('predicate:', refined_template_dict['predicate_refined'])
            print('object:', refined_template_dict['object_refined'])
            print('conjunction:', refined_template_dict['conjunction_refined'])
            print('\n')

    def display_translation(self):
        count = 1
        for eng in self.eng_list:
            print('%d: %s' % (count, eng))
            count = count + 1
