from translation.level_1.atom.predicate_operation.predicate_refiner import PredicateRefiner
from translation.level_2.TP_atom.original_TP_atom.eventually.simplest.simplest_eventually_atom_handler \
    import SimplestEventuallyAtomHandler
from translation.level_2.TP_atom.original_TP_atom.always.simplest.simplest_always_atom_handler \
    import SimplestAlwaysAtomHandler
from translation.level_2.TP_atom.original_TP_atom.once.simplest.simplest_once_atom_handler \
    import SimplestOnceAtomHandler
from translation.level_2.TP_atom.original_TP_atom.historically.simplest.simplest_historically_atom_handler \
    import SimplestHistoricallyAtomHandler
from translation.level_2.TP_atom.original_TP_atom.until.simplest.simplest_until_atom_handler \
    import SimplestUntilAtomHandler
from translation.level_2.TP_atom.original_TP_atom.since.simplest.simplest_since_atom_handler \
    import SimplestSinceAtomHandler
import copy
import random


class FallTPAtomType1RefinerAssembler:
    def __init__(self, template, predicate_cmd_dict, adverbial_para, translate_guide):
        # information about the template
        self.template = copy.deepcopy(template)
        # commands to operate predicate
        self.predicate_cmd = copy.deepcopy(predicate_cmd_dict)
        # adverbial list
        self.adverbial_para = copy.deepcopy(adverbial_para)
        # translating guide
        self.translate_guide = copy.deepcopy(translate_guide)

        # the methods of class PredicateProcessor are used in this class
        self.predicate_refiner = PredicateRefiner()

        # a list containing assembling guide
        self.assemble_guide = list()
        # a list containing the assembling results, namely English translation, of the refined template
        self.eng_list = list()

        self.assemble_guide = self.main_sentence_refine()
        self.assemble_guide.reverse()
        self.eng_list = self.main_sentence_assemble()

    def main_sentence_refine(self):
        subject_refined = copy.deepcopy(self.template['subject'])

        # get the simplest translation version of the temporal operator
        simplest_material = self.translate_guide['original_tp_instruction']
        limit_num = self.translate_guide['tp_operator_limit_num']
        tp_operator_type = self.translate_guide['tp_operator_type']
        if tp_operator_type == 'eventually':
            simplest_eventually_atom_handler \
                = SimplestEventuallyAtomHandler(simplest_material, limit_num)
            appositive_refined = \
                simplest_eventually_atom_handler.simplest_eventually_atom_translator.random_selected_translations
        elif tp_operator_type == 'always':
            simplest_always_atom_handler = \
                SimplestAlwaysAtomHandler(simplest_material, limit_num)
            appositive_refined = \
                simplest_always_atom_handler.simplest_always_atom_translator.random_selected_translations
        elif tp_operator_type == 'once':
            simplest_once_atom_handler = \
                SimplestOnceAtomHandler(simplest_material, limit_num)
            appositive_refined = \
                simplest_once_atom_handler.simplest_once_atom_translator.random_selected_translations
        elif tp_operator_type == 'historically':
            simplest_historically_atom_handler = \
                SimplestHistoricallyAtomHandler(simplest_material, limit_num)
            appositive_refined = \
                simplest_historically_atom_handler.simplest_historically_atom_translator.random_selected_translations
        elif tp_operator_type == 'until':
            simplest_until_atom_handler = \
                SimplestUntilAtomHandler(simplest_material, limit_num)
            appositive_refined = \
                simplest_until_atom_handler.simplest_until_atom_translator.random_selected_translations
        else:  # tp_operator_type == 'since':
            simplest_since_atom_handler = \
                SimplestSinceAtomHandler(simplest_material, limit_num)
            appositive_refined = \
                simplest_since_atom_handler.simplest_since_atom_translator.random_selected_translations

        template_key, mood = 'predicate', 'positive'
        predicate_refined = self.predicate_refine(template_key, mood)

        object_refined = copy.deepcopy(self.template['object'])

        refined_template_dict = {'mood': mood,
                                 'subject_refined': subject_refined,
                                 'appositive_refined': appositive_refined,
                                 'predicate_refined': predicate_refined,
                                 'object_refined': object_refined
                                 }
        self.assemble_guide.append(refined_template_dict)

        return self.assemble_guide

    def predicate_refine(self, template_key, mood):
        predicate_template = copy.deepcopy(self.template[template_key])
        commands_selected = self.predicate_cmd[mood]
        predicate_refined = self.predicate_refiner.predicate_process(predicate_template, mood, commands_selected)
        return predicate_refined

    def main_sentence_assemble(self):
        assemble_guide = copy.deepcopy(self.assemble_guide)
        while len(assemble_guide) != 0:
            refined_template_dict = assemble_guide.pop()
            self.assemble_process(refined_template_dict)

        return self.eng_list

    def assemble_process(self, refined_template_dict):
        subject_refined = refined_template_dict['subject_refined']
        appositive_refined = refined_template_dict['appositive_refined']
        predicate_refined = refined_template_dict['predicate_refined']
        object_refined = refined_template_dict['object_refined']

        for i in range(len(predicate_refined)):
            for predicate in predicate_refined[i]:
                for appositive in appositive_refined:
                    main_para = [subject_refined, appositive, predicate, object_refined]
                    eng = self.random_select_assemble(main_para)
                    self.eng_list.append(eng)

                    if len(self.adverbial_para) != 0:  # temporarily set like this
                        # check whether 'predicate' contains any adverb in self.adverbial_para
                        flag = 0
                        for scanned_word in self.adverbial_para:
                            if scanned_word in predicate:
                                flag = 1
                        # If flag == 0, then 'predicate' doesn't contain any word in the adverbial list.
                        # Generate new translations with adverbs and adverbial phrases.
                        if flag == 0:
                            eng_list_adverbialAdded = self.adverbial_augment(main_para)
                            self.eng_list = self.eng_list + eng_list_adverbialAdded

    def adverbial_augment(self, main_para):
        eng_list_adverbialAdded = []

        for word in self.adverbial_para:
            eng_main = self.random_select_assemble(main_para)
            eng_update = word + ' ' + eng_main
            eng_list_adverbialAdded.append(eng_update)

            eng_main = self.random_select_assemble(main_para)
            eng_update = eng_main + ' ' + word
            eng_list_adverbialAdded.append(eng_update)

        return eng_list_adverbialAdded

    @staticmethod
    def random_select_assemble(main_para):
        # randomly choose a subject in the 'subject_refined' list
        eng_subject = random.choice(main_para[0])
        eng_appositive = main_para[1]
        eng_predicate = main_para[2]
        # randomly choose an object in the 'object_refined' list
        eng_object = random.choice(main_para[3])
        eng = eng_subject + ' ' + eng_appositive + ' ' + eng_predicate + ' ' + eng_object

        return eng

    def display_assemble_guide(self):
        assemble_guide = copy.deepcopy(self.assemble_guide)
        while len(assemble_guide) != 0:
            refined_template_dict = assemble_guide.pop()
            print(refined_template_dict)
            print('mood:', refined_template_dict['mood'])
            print('subject:', refined_template_dict['subject_refined'])
            print('appositive:', refined_template_dict['appositive_refined'])
            print('predicate:', refined_template_dict['predicate_refined'])
            print('object:', refined_template_dict['object_refined'])
            print('\n')

    def display_translation(self):
        count = 1
        for eng in self.eng_list:
            print('%d: %s' % (count, eng))
            count = count + 1
