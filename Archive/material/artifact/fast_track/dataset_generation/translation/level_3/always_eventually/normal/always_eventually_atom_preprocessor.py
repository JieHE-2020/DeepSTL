from template import TP_template
from commands.command_eventually import PreCmdEventually
from translation.level_2.TP_atom.original_TP_atom.eventually.normal.eventually_atom_quick_refiner_assembler \
    import EventuallyAtomQuickRefinerAssembler
from translation.level_2.TP_atom.original_TP_atom.eventually.normal.SP.eventually_atom_template_refiner \
    import EventuallyAtomTemplateRefiner
from translation.level_2.TP_atom.original_TP_atom.eventually.normal.SP.eventually_atom_assembler \
    import EventuallyAtomAssembler
import copy
import random


class AlwaysEventuallyAtomPreprocessor:
    """
    functions:
    1. process the temporal information of 'always' operator in the form of phrase
       and assemble them into English expressions
    2. process the temporal information of 'eventually' operator in the form of phrase
       and assemble the ingredients into English expressions
    3. process the temporal information of 'eventually' operator in the form of clause
       and assemble the ingredients into English expressions
    4. refine the templates of Atom expressions and assemble them into English translations
    """

    def __init__(self, translate_guide):
        self.instruction_dict = copy.deepcopy(translate_guide[0])
        self.ntp_info_dict = copy.deepcopy(translate_guide[1])

        # extract information for temporal operator
        self.tp_template_index = self.ntp_info_dict['TP_template_index']
        self.always_index = self.tp_template_index[0]
        self.eventually_index = self.tp_template_index[1]

        always_category = self.always_index[0]
        always_sub_category = self.always_index[1]
        eventually_category = self.eventually_index[0]
        eventually_sub_category = self.eventually_index[1]

        self.always_template = copy.deepcopy(TP_template.Eng_TP[always_category][always_sub_category])
        self.eventually_template = copy.deepcopy(TP_template.Eng_TP[eventually_category][eventually_sub_category])

        # extract information for simple phrase
        self.sp_info_dict = self.ntp_info_dict['ingredient'][0]

        # Start Preprocessing

        # prepare adverbial modifiers and commands for later use
        self.eventually_adverbial_dict = self.eventually_adverbial_prepare()
        self.eventually_predicate_cmd_dict = self.eventually_command_process()  # tense is 'future'

        # process the temporal information for 'always' (in the form of phrase)
        # and assemble them into English expressions
        # 1. temporal_phrase_each_time;  2. admit 'first' in adverbials
        self.always_eng_temporal_phrase = self.always_temporal_phrase_process()

        # process the temporal information for 'eventually' in the form of phrase
        # and assemble them into English expressions
        [self.eventually_temporal_info_refined, self.eventually_eng_temporal_phrase] = \
            self.eventually_temporal_phrase_process()  # not admit 'first' in adverbials

        # process the temporal information for 'eventually' in the form of clause
        # and assemble them into English expressions
        self.eventually_eng_temporal_clause = self.eventually_temporal_clause_process()

        if self.instruction_dict['nest_info_dict']['whetherBottom']:
            # refine the templates of Atom expressions and assemble them into English translations
            self.eng_main_sentence = self.main_sentence_process()

    def eventually_adverbial_prepare(self):
        adv_refine_dict = copy.deepcopy(self.eventually_template['adverb'])

        adv_list = copy.deepcopy(self.eventually_template['adverb']['adverb'])
        adv_phrase_list = []  # only assemble adverbs, do not assemble phrases
        adv_assemble_list = [adv_list, adv_phrase_list]

        adverbial_dict = {
            'refine_dict': adv_refine_dict,
            'assemble_list': adv_assemble_list,
            'adv_general_list': adv_list
        }

        return adverbial_dict

    def eventually_command_process(self):
        adverb_dict = copy.deepcopy(self.eventually_adverbial_dict['refine_dict'])
        pre_cmd = PreCmdEventually(adverb_dict)

        position = self.instruction_dict['position']
        tense = self.instruction_dict['nest_info_dict']['tense']

        if tense == 'present':
            if position == 'before_imply':
                main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_after_imply)
            appositive_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_appositive)

        elif tense == 'future':
            if position == 'before_imply':
                main_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_after_imply)
            appositive_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_appositive)

        else:  # tense == 'past'
            if position == 'before_imply':
                main_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_after_imply)
            appositive_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_appositive)

        predicate_cmd_dict = {
            'main': main_cmd_dict,
            'appositive': appositive_cmd_dict
        }

        return predicate_cmd_dict

    def always_temporal_phrase_process(self):
        temporal_info_raw = copy.deepcopy(self.always_template['temporal_phrase_each_time'])
        eng_temporal_phrase = []
        # nest_info_dict = self.instruction_dict['nest_info_dict']

        if self.always_index == [1, 0]:  # always
            eng_temporal_phrase = temporal_info_raw

        elif self.always_index == [1, 1]:  # always [0:t] (0 < t)
            t_value = self.ntp_info_dict['ingredient'][1]
            for phrase in temporal_info_raw:
                # if nest_info_dict['whetherNest'] and nest_info_dict['nestLayer'] > 1:
                #     if 'first' in phrase:
                #         continue
                phrase_modified = phrase.replace('t_value', t_value)
                eng_temporal_phrase.append(phrase_modified)

        else:  # always [a:b] (0 < a < b)
            t_value_a = self.ntp_info_dict['ingredient'][1]
            t_value_b = self.ntp_info_dict['ingredient'][2]
            for phrase in temporal_info_raw:
                # if nest_info_dict['whetherNest'] and nest_info_dict['nestLayer'] > 1:
                #     if 'first' in phrase:
                #         continue
                phrase_modified = phrase.replace('t_value_a', t_value_a)
                phrase_modified = phrase_modified.replace('t_value_b', t_value_b)
                eng_temporal_phrase.append(phrase_modified)

        return eng_temporal_phrase

    def eventually_temporal_phrase_process(self):
        temporal_info_raw = copy.deepcopy(self.eventually_template['temporal_phrase'])
        temporal_info_refined = []

        if self.eventually_index == [0, 0]:  # eventually
            temporal_info_refined = temporal_info_raw

        elif self.eventually_index == [0, 1]:  # eventually [0:t] (0 < t)
            t_value = self.ntp_info_dict['ingredient'][-1]
            for phrase in temporal_info_raw:
                phrase_modified = phrase.replace('t_value', t_value)
                temporal_info_refined.append(phrase_modified)

        else:  # eventually [a:b] (0 < a < b)
            t_value_a = self.ntp_info_dict['ingredient'][-2]
            t_value_b = self.ntp_info_dict['ingredient'][-1]
            for phrase in temporal_info_raw:
                phrase_modified = phrase.replace('t_value_a', t_value_a)
                phrase_modified = phrase_modified.replace('t_value_b', t_value_b)
                temporal_info_refined.append(phrase_modified)

        eng_temporal_phrase = self.eventually_random_temporal_phrase_assemble(temporal_info_refined)

        return [temporal_info_refined, eng_temporal_phrase]

    def eventually_random_temporal_phrase_assemble(self, temporal_info_refined):
        eng_temporal_phrase = []

        adv_list = copy.deepcopy(self.eventually_adverbial_dict['adv_general_list'])
        semantics_sometime = copy.deepcopy(self.eventually_template['semantics_sometime'])
        nest_info_dict = self.instruction_dict['nest_info_dict']

        for phrase_sometime in semantics_sometime:
            for phrase_temporal in temporal_info_refined:

                if nest_info_dict['whetherNest'] and nest_info_dict['nestLayer'] > 1:
                    if 'first' in phrase_temporal:
                        continue

                flag = random.randint(0, 1)
                if flag == 0:  # do not add adverb
                    phrase_at_sometime = 'at ' + phrase_sometime
                    eng = phrase_at_sometime + ' ' + phrase_temporal
                else:  # add adverb
                    adverb = random.choice(adv_list)
                    phrase_at_sometime = 'at ' + phrase_sometime
                    eng = adverb + ' ' + phrase_at_sometime + ' ' + phrase_temporal
                eng_temporal_phrase.append(eng)

        return eng_temporal_phrase

    def eventually_temporal_clause_process(self):
        new_template = dict()
        # subject
        new_template['subject'] = copy.deepcopy(self.eventually_template['clause']['subject'])
        # predicate
        new_template['predicate'] = copy.deepcopy(self.eventually_template['clause']['predicate'])
        # object
        object_ingredient = copy.deepcopy(self.eventually_template['clause']['object'])
        clause_object = []
        for ingredient in object_ingredient:
            for phrase in self.eventually_temporal_info_refined:
                obj = ingredient + ' ' + phrase
                clause_object.append(obj)
        new_template['object'] = clause_object
        # conjunction to link the following clause
        new_template['conjunction'] = ', at which'

        predicate_cmd_dict = copy.deepcopy(self.eventually_predicate_cmd_dict['main'])
        adverbial_list = copy.deepcopy(self.eventually_adverbial_dict['adv_general_list'])
        quick_refiner_assembler = EventuallyAtomQuickRefinerAssembler(new_template, predicate_cmd_dict, adverbial_list)
        self.eventually_eng_temporal_clause = quick_refiner_assembler.eng_list

        return self.eventually_eng_temporal_clause

    def main_sentence_process(self):
        main_sentence_refiner = EventuallyAtomTemplateRefiner(self.sp_info_dict, self.eventually_predicate_cmd_dict)

        adverbial_query = self.instruction_dict['adverbial_query']
        adverbial_para = copy.deepcopy(self.eventually_adverbial_dict['assemble_list'])
        main_sentence_assembler = EventuallyAtomAssembler(adverbial_query, main_sentence_refiner.assemble_guide,
                                                          adverbial_para)
        # main_sentence_assembler.display_translation()
        self.eng_main_sentence = main_sentence_assembler.eng_list

        return self.eng_main_sentence

    def display_key_list(self):
        count = 1
        for eng in self.eventually_eng_temporal_phrase:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

        count = 1
        for eng in self.eventually_eng_temporal_clause:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

        count = 1
        for eng in self.eng_main_sentence:
            print('%d: %s' % (count, eng))
            count = count + 1

    def pack_key_list(self):
        return [self.always_eng_temporal_phrase, self.eventually_eng_temporal_phrase,
                self.eventually_eng_temporal_clause, self.eng_main_sentence, self.eventually_template]
