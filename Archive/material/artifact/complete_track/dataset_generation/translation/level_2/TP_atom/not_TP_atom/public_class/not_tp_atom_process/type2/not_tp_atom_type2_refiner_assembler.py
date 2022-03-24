from translation.level_1.atom.predicate_operation.predicate_refiner import PredicateRefiner
from translation.level_2.TP_atom.original_TP_atom.eventually.normal.eventually_atom_hook import EventuallyAtomHook
from translation.level_2.TP_atom.original_TP_atom.always.normal.always_atom_hook import AlwaysAtomHook
from translation.level_2.TP_atom.original_TP_atom.once.normal.once_atom_hook import OnceAtomHook
from translation.level_2.TP_atom.original_TP_atom.historically.normal.historically_atom_hook import HistoricallyAtomHook
from translation.level_2.TP_atom.original_TP_atom.until.normal.until_atom_hook import UntilAtomHook
from translation.level_2.TP_atom.original_TP_atom.since.normal.since_atom_hook import SinceAtomHook
import copy
import random


class NotTPAtomType2RefinerAssembler:
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
        template_key, mood = 'predicate', 'negative'
        predicate_refined = self.predicate_refine(template_key, mood)
        object_refined = copy.deepcopy(self.template['object'])

        # get the normal translation version of the temporal operator
        normal_material = self.translate_guide['original_tp_instruction']
        limit_num = self.translate_guide['tp_operator_limit_num']
        tp_operator_type = self.translate_guide['tp_operator_type']
        if tp_operator_type == 'eventually':
            eventually_atom_hook = EventuallyAtomHook(normal_material, limit_num)
            appendix_refined = eventually_atom_hook.eventually_atom_translator.random_selected_translations
        elif tp_operator_type == 'always':
            always_atom_hook = AlwaysAtomHook(normal_material, limit_num)
            appendix_refined = always_atom_hook.always_atom_translator.random_selected_translations
        elif tp_operator_type == 'once':
            once_atom_hook = OnceAtomHook(normal_material, limit_num)
            appendix_refined = once_atom_hook.once_atom_translator.random_selected_translations
        elif tp_operator_type == 'historically':
            historically_atom_hook = HistoricallyAtomHook(normal_material, limit_num)
            appendix_refined = historically_atom_hook.historically_atom_translator.random_selected_translations
        elif tp_operator_type == 'until':
            until_atom_hook = UntilAtomHook(normal_material, limit_num)
            appendix_refined = until_atom_hook.until_atom_translator.random_selected_translations
        else:  # tp_operator_type == 'since':
            since_atom_hook = SinceAtomHook(normal_material, limit_num)
            appendix_refined = since_atom_hook.since_atom_translator.random_selected_translations

        refined_template_dict = {'mood': mood,
                                 'subject_refined': subject_refined,
                                 'predicate_refined': predicate_refined,
                                 'object_refined': object_refined,
                                 'appendix_refined': appendix_refined
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
        predicate_refined = refined_template_dict['predicate_refined']
        object_refined = refined_template_dict['object_refined']
        appendix_refined = refined_template_dict['appendix_refined']

        for i in range(len(predicate_refined)):
            for predicate in predicate_refined[i]:
                for appendix in appendix_refined:
                    main_para = [subject_refined, predicate, object_refined]
                    eng_main = self.random_select_assemble(main_para)
                    eng = eng_main + ': ' + appendix
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
                            eng_list_adverbialAdded = self.adverbial_augment(main_para, appendix)
                            self.eng_list = self.eng_list + eng_list_adverbialAdded

    def adverbial_augment(self, main_para, appendix):
        eng_list_adverbialAdded = []

        for word in self.adverbial_para:
            eng_main = self.random_select_assemble(main_para)
            eng_update = word + ' ' + eng_main + ': ' + appendix
            eng_list_adverbialAdded.append(eng_update)

            # # the mood of the sentence is negative,
            # # so do not put adverbs or adverbial phrases to the end of the sentence
            # eng_main = self.random_select_assemble(main_para)
            # eng_update = eng_main + ' ' + word + ': ' + appendix
            # eng_list_adverbialAdded.append(eng_update)

        return eng_list_adverbialAdded

    @staticmethod
    def random_select_assemble(main_para):
        # randomly choose a subject in the 'subject_refined' list
        eng_subject = random.choice(main_para[0])
        eng_predicate = main_para[1]
        # randomly choose an object in the 'object_refined' list
        eng_object = random.choice(main_para[2])
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
            print('appendix:', refined_template_dict['appendix_refined'])
            print('\n')

    def display_translation(self):
        count = 1
        for eng in self.eng_list:
            print('%d: %s' % (count, eng))
            count = count + 1
