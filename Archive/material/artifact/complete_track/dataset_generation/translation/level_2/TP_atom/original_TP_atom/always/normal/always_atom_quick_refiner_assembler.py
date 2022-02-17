from translation.level_1.atom.predicate_operation.predicate_refiner import PredicateRefiner
import copy
import random


class AlwaysAtomQuickRefinerAssembler:
    def __init__(self, template, predicate_cmd_dict, adverbial_para):
        # information about the template
        self.template = copy.deepcopy(template)
        # commands to operate predicate
        self.predicate_cmd = copy.deepcopy(predicate_cmd_dict)
        # adverbial list
        self.adverbial_para = copy.deepcopy(adverbial_para)

        # the methods of class PredicateProcessor are used in this class
        self.predicate_refiner = PredicateRefiner()

        # a list containing assembling guide
        self.assemble_guide = list()
        # a list containing the assembling results, namely English translation, of the refined template
        self.eng_list = list()

        self.distribute()

    def distribute(self):
        kind = copy.deepcopy(self.template['kind'])
        if kind == 'clause_general' or kind == 'clause_value' or kind == 'clause_range' or kind == 'clause_mode':
            self.assemble_guide = self.clause_refine()
            self.assemble_guide.reverse()
            self.eng_list = self.clause_assemble()

        if kind == 'special_clause':
            self.assemble_guide = self.special_clause_refine()
            self.assemble_guide.reverse()
            self.eng_list = self.special_clause_assemble()

    def clause_refine(self):
        conjunction_refined = copy.deepcopy(self.template['conjunction'])
        template_key, mood = 'predicate', 'positive'
        predicate_refined = self.predicate_refine(template_key, mood)
        object_refined = copy.deepcopy(self.template['object'])
        refined_template_dict = {'mood': mood,
                                 'conjunction_refined': conjunction_refined,
                                 'predicate_refined': predicate_refined,
                                 'object_refined': object_refined
                                 }
        self.assemble_guide.append(refined_template_dict)

        return self.assemble_guide

    def special_clause_refine(self):
        conjunction_refined = copy.deepcopy(self.template['conjunction'])
        subject_refined = copy.deepcopy(self.template['subject'])
        template_key, mood = 'predicate', 'positive'
        predicate_refined = self.predicate_refine(template_key, mood)
        refined_template_dict = {'mood': mood,
                                 'conjunction_refined': conjunction_refined,
                                 'subject_refined': subject_refined,
                                 'predicate_refined': predicate_refined
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
            self.clause_assemble_process(refined_template_dict)

        return self.eng_list

    def special_clause_assemble(self):
        assemble_guide = copy.deepcopy(self.assemble_guide)
        while len(assemble_guide) != 0:
            refined_template_dict = assemble_guide.pop()
            self.special_clause_assemble_process(refined_template_dict)

        return self.eng_list

    def clause_assemble_process(self, refined_template_dict):
        conjunction_refined = refined_template_dict['conjunction_refined']
        predicate_refined = refined_template_dict['predicate_refined']
        object_refined = refined_template_dict['object_refined']

        for i in range(len(predicate_refined)):
            for predicate in predicate_refined[i]:
                clause_para = [conjunction_refined, predicate, object_refined]
                eng = self.clause_random_select(clause_para)
                repetition = self.check_continue_continuously(eng)
                if repetition:
                    # if continue and continuously are in the same clause,
                    # the probability for this clause to discard is 0.8
                    point = random.randint(1, 100)
                    if point <= 80:
                        continue
                    else:
                        self.eng_list.append(eng)
                else:
                    self.eng_list.append(eng)

                # check whether 'predicate' contains any adverbs
                flag = self.check_adverb_existence(predicate)
                # If flag == 0, then 'predicate' doesn't contain any adverbs.
                # Generate new translations with adverbs and adverbial phrases.
                if flag == 0:
                    eng_list_adverbialAdded = self.clause_adverbial_augment(clause_para)
                    self.eng_list = self.eng_list + eng_list_adverbialAdded

    def special_clause_assemble_process(self, refined_template_dict):
        conjunction_refined = refined_template_dict['conjunction_refined']
        subject_refined = refined_template_dict['subject_refined']
        predicate_refined = refined_template_dict['predicate_refined']

        for i in range(len(predicate_refined)):
            for predicate in predicate_refined[i]:
                clause_para = [subject_refined, predicate]
                eng_main = self.special_clause_random_select(clause_para)
                repetition = self.check_continue_continuously(eng_main)
                if repetition:
                    # if continue and continuously are in the same clause,
                    # the probability for this clause to discard is 0.8
                    point = random.randint(1, 100)
                    if point <= 80:
                        continue
                    else:
                        eng = random.choice(conjunction_refined) + ' ' + eng_main
                        self.eng_list.append(eng)
                else:
                    eng = random.choice(conjunction_refined) + ' ' + eng_main
                    self.eng_list.append(eng)

                    # check whether 'predicate' contains any adverbs
                    flag = self.check_adverb_existence(predicate)
                    # If flag == 0, then 'predicate' doesn't contain any adverbs.
                    # Generate new translations with adverbs and adverbial phrases.
                    if flag == 0:
                        eng_list_adverbialAdded = self.special_clause_adverbial_augment(clause_para,
                                                                                        conjunction_refined)
                        self.eng_list = self.eng_list + eng_list_adverbialAdded

    def clause_adverbial_augment(self, clause_para):
        eng_list_adverbialAdded = []

        for word in self.adverbial_para[0]:
            eng = self.clause_random_select(clause_para)
            eng_update = eng + ' ' + word
            repetition = self.check_continue_continuously(eng_update)
            if repetition:
                # if continue and continuously are in the same clause, the probability for this clause to discard is 0.8
                point = random.randint(1, 100)
                if point > 80:
                    eng_list_adverbialAdded.append(eng_update)
            else:
                eng_list_adverbialAdded.append(eng_update)

        for phrase in self.adverbial_para[1]:
            eng = self.clause_random_select(clause_para)
            eng_update = eng + ' ' + phrase
            eng_list_adverbialAdded.append(eng_update)

        return eng_list_adverbialAdded

    def special_clause_adverbial_augment(self, clause_para, conjunction_refined):
        eng_list_adverbialAdded = []

        for word in self.adverbial_para[0]:
            eng_main = self.special_clause_random_select(clause_para)
            eng_update = random.choice(conjunction_refined) + ' ' + word + ' ' + eng_main
            repetition = self.check_continue_continuously(eng_update)
            if repetition:
                # if continue and continuously are in the same clause, the probability for this clause to discard is 0.8
                point = random.randint(1, 100)
                if point > 80:
                    eng_list_adverbialAdded.append(eng_update)
            else:
                eng_list_adverbialAdded.append(eng_update)

            eng_main = self.special_clause_random_select(clause_para)
            eng_update = random.choice(conjunction_refined) + ' ' + eng_main + ' ' + word
            repetition = self.check_continue_continuously(eng_update)
            if repetition:
                # if continue and continuously are in the same clause, the probability for this clause to discard is 0.8
                point = random.randint(1, 100)
                if point > 80:
                    eng_list_adverbialAdded.append(eng_update)
            else:
                eng_list_adverbialAdded.append(eng_update)

        for phrase in self.adverbial_para[1]:
            # add 'all the time' at the end of the clause
            eng_main = self.special_clause_random_select(clause_para)
            eng_update = random.choice(conjunction_refined) + ' ' + eng_main + ' ' + phrase
            eng_list_adverbialAdded.append(eng_update)

        return eng_list_adverbialAdded

    def check_adverb_existence(self, predicate):
        adverb_list_checked = copy.deepcopy(self.adverbial_para[0])
        adverb_list_checked.append('always')
        flag = 0
        for scanned_word in adverb_list_checked:
            if scanned_word in predicate:
                flag = 1

        return flag

    @staticmethod
    def check_continue_continuously(eng_main):
        repetition = False
        # in case of 'continuing', we check whether 'continu' exists in eng_main
        if 'continu' in eng_main and 'continuously' in eng_main:
            repetition = True

        return repetition

    @staticmethod
    def clause_random_select(clause_para):
        # randomly choose a subject in the 'conjunction_refined' list
        eng_conjunction = random.choice(clause_para[0])
        eng_predicate = clause_para[1]
        # randomly choose an object in the 'object_refined' list
        eng_object = random.choice(clause_para[2])
        eng = eng_conjunction + ' ' + eng_predicate + ' ' + eng_object

        return eng

    @staticmethod
    def special_clause_random_select(clause_para):
        # randomly choose a subject in the 'subject_refined' list
        eng_subject = random.choice(clause_para[0])
        eng_predicate = clause_para[1]
        eng = eng_subject + ' ' + eng_predicate

        return eng

    # def display_assemble_guide(self):
    #     assemble_guide = copy.deepcopy(self.assemble_guide)
    #     while len(assemble_guide) != 0:
    #         refined_template_dict = assemble_guide.pop()
    #         print(refined_template_dict)
    #         print('mood:', refined_template_dict['mood'])
    #         print('subject:', refined_template_dict['subject_refined'])
    #         print('predicate:', refined_template_dict['predicate_refined'])
    #         print('object:', refined_template_dict['object_refined'])
    #         print('conjunction:', refined_template_dict['conjunction_refined'])
    #         print('\n')

    def display_translation(self):
        count = 1
        for eng in self.eng_list:
            print('%d: %s' % (count, eng))
            count = count + 1
