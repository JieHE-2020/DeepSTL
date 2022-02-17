from template import TP_template
from commands.command_eventually import PreCmdEventually
from commands.command_always import PreCmdAlways
from translation.level_2.TP_atom.original_TP_atom.eventually.normal.eventually_atom_quick_refiner_assembler \
    import EventuallyAtomQuickRefinerAssembler
from translation.level_2.TP_atom.original_TP_atom.always.normal.SP.always_atom_template_refiner \
    import AlwaysAtomTemplateRefiner
from translation.level_2.TP_atom.original_TP_atom.always.normal.SP.always_atom_assembler \
    import AlwaysAtomAssembler
from translation.level_2.TP_atom.original_TP_atom.always.normal.always_atom_quick_refiner_assembler \
    import AlwaysAtomQuickRefinerAssembler
import copy
import random


class EventuallyAlwaysAtomPreprocessor:
    """
    functions:
    1.1. process the temporal information of 'eventually' operator in the form of phrase
       and assemble the ingredients into English expressions
    1.2. process the temporal information of 'eventually' operator in the form of clause
       and assemble the ingredients into English expressions
    2. process the temporal information of 'always' operator in the form of phrase
       and assemble them into English expressions
    3. process main sentences of type 1:
       refine the templates of SP and assemble them into English expressions
    4. process main sentences of type 2:
       with auxiliary clause like 'stays like that + temporal information'
    """

    def __init__(self, translate_guide, whether_from_not_eventually=False):
        self.instruction_dict = copy.deepcopy(translate_guide[0])
        self.ntp_info_dict = copy.deepcopy(translate_guide[1])
        self.whether_from_not_eventually = whether_from_not_eventually

        # extract information for temporal operator
        self.tp_template_index = self.ntp_info_dict['TP_template_index']
        self.eventually_index = self.tp_template_index[0]
        self.always_index = self.tp_template_index[1]
        
        eventually_category = self.eventually_index[0]
        eventually_sub_category = self.eventually_index[1]
        always_category = self.always_index[0]
        always_sub_category = self.always_index[1]
        
        self.eventually_template = copy.deepcopy(TP_template.Eng_TP[eventually_category][eventually_sub_category])
        self.always_template = copy.deepcopy(TP_template.Eng_TP[always_category][always_sub_category])

        # extract information for simple phrase
        self.sp_info_dict = self.ntp_info_dict['ingredient'][0]

        # Start Preprocessing

        # prepare adverbial modifiers and commands for later use
        self.eventually_adverbial_dict = self.eventually_adverbial_prepare()
        self.always_adverbial_dict = self.always_adverbial_prepare()
        self.eventually_predicate_cmd_dict = self.eventually_command_process()  # tense is 'present'
        self.always_predicate_cmd_dict = self.always_command_process()  # tense is ''future

        # process the temporal information for 'eventually' in the form of phrase
        # and assemble them into English expressions
        [self.eventually_temporal_info_refined, self.eventually_eng_temporal_phrase] = \
            self.eventually_temporal_phrase_process()  # admit 'first' in adverbials
        # process the temporal information for 'eventually' in the form of clause
        # and assemble them into English expressions
        self.eventually_eng_temporal_clause = self.eventually_temporal_clause_process()  # at which -> after which

        # process the temporal information for 'always' (in the form of phrase)
        # and assemble them into English expressions
        self.always_eng_temporal_phrase = self.always_temporal_phrase_process()  # not admit 'first' in adverbials

        if self.instruction_dict['nest_info_dict']['whetherBottom']:
            # process main sentences of type 1
            # refine the templates of SP and assemble them into English expressions
            self.eng_main_sentence_type1 = self.main_sentence_type1_process()
            # process main sentences of type 2
            # with auxiliary clause like 'stays like that + temporal information'
            self.eng_main_sentence_type2 = self.main_sentence_type2_process()

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

    def always_adverbial_prepare(self):
        adv_refine_dict = copy.deepcopy(copy.deepcopy(self.always_template['adverb_refine']))

        adv_list = copy.deepcopy(self.always_template['adverb_assemble']['adverb'])
        adv_phrase_list = copy.deepcopy(self.always_template['adverbial_phrase_assemble']['adverbial_phrase'])
        adv_assemble_list = [adv_list, adv_phrase_list]

        adverbial_dict = {
            'refine_dict': adv_refine_dict,
            'assemble_list': adv_assemble_list
        }

        return adverbial_dict

    def eventually_command_process(self):
        adverb_dict = copy.deepcopy(self.eventually_adverbial_dict['refine_dict'])
        pre_cmd = PreCmdEventually(adverb_dict)

        position = self.instruction_dict['position']
        tense = 'present'   # for temporal use

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

    def always_command_process(self):
        adverb_dict = copy.deepcopy(self.always_adverbial_dict['refine_dict'])
        pre_cmd = PreCmdAlways(adverb_dict)

        position = self.instruction_dict['position']
        tense = self.instruction_dict['nest_info_dict']['tense']

        if tense == 'present':
            if position == 'before_imply':
                main_type1_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_before_imply_main_type1_cmd_dict)
                main_type1_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_before_imply_main_type1_appositive_cmd_dict)

                main_type2_main_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_before_imply_main_type2_main_part_cmd_dict)
                main_type2_main_part_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_before_imply_main_type2_main_part_appositive_cmd_dict)

                main_type2_clause_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_before_imply_main_type2_clause_part_cmd_dict)

            else:  # position == 'after_imply'
                main_type1_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_after_imply_main_type1_cmd_dict)
                main_type1_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_after_imply_main_type1_appositive_cmd_dict)

                main_type2_main_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_after_imply_main_type2_main_part_cmd_dict)
                main_type2_main_part_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_after_imply_main_type2_main_part_appositive_cmd_dict)

                main_type2_clause_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.present_after_imply_main_type2_clause_part_cmd_dict)

        elif tense == 'future':
            if position == 'before_imply':
                main_type1_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_before_imply_main_type1_cmd_dict)
                main_type1_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_before_imply_main_type1_appositive_cmd_dict)

                main_type2_main_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_before_imply_main_type2_main_part_cmd_dict)
                main_type2_main_part_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_before_imply_main_type2_main_part_appositive_cmd_dict)

                main_type2_clause_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_before_imply_main_type2_clause_part_cmd_dict)

            else:  # position == 'after_imply'
                main_type1_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_after_imply_main_type1_cmd_dict)
                main_type1_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_after_imply_main_type1_appositive_cmd_dict)

                main_type2_main_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_after_imply_main_type2_main_part_cmd_dict)
                main_type2_main_part_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_after_imply_main_type2_main_part_appositive_cmd_dict)

                main_type2_clause_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.future_after_imply_main_type2_clause_part_cmd_dict)

        else:  # tense == 'past'
            if position == 'before_imply':
                main_type1_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_before_imply_main_type1_cmd_dict)
                main_type1_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_before_imply_main_type1_appositive_cmd_dict)

                main_type2_main_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_before_imply_main_type2_main_part_cmd_dict)
                main_type2_main_part_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_before_imply_main_type2_main_part_appositive_cmd_dict)

                main_type2_clause_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_before_imply_main_type2_clause_part_cmd_dict)

            else:  # position == 'after_imply'
                main_type1_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_after_imply_main_type1_cmd_dict)
                main_type1_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_after_imply_main_type1_appositive_cmd_dict)

                main_type2_main_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_after_imply_main_type2_main_part_cmd_dict)
                main_type2_main_part_appositive_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_after_imply_main_type2_main_part_appositive_cmd_dict)

                main_type2_clause_part_cmd_dict = \
                    copy.deepcopy(pre_cmd.past_after_imply_main_type2_clause_part_cmd_dict)

        main_type1 = {
            'main': main_type1_cmd_dict,
            'appositive': main_type1_appositive_cmd_dict
        }

        main_type2_main_part = {
            'main': main_type2_main_part_cmd_dict,
            'appositive': main_type2_main_part_appositive_cmd_dict
        }

        predicate_cmd_dict = {
            'main_type1': main_type1,
            'main_type2_main_part': main_type2_main_part,
            'main_type2_clause_part': main_type2_clause_part_cmd_dict
        }

        return predicate_cmd_dict

    def eventually_temporal_phrase_process(self):
        temporal_info_raw = copy.deepcopy(self.eventually_template['temporal_phrase'])
        temporal_info_refined = []

        if self.eventually_index == [0, 0]:  # eventually
            temporal_info_refined = temporal_info_raw

        elif self.eventually_index == [0, 1]:  # eventually [0:t] (0 < t)
            t_value = self.ntp_info_dict['ingredient'][1]
            for phrase in temporal_info_raw:
                phrase_modified = phrase.replace('t_value', t_value)
                temporal_info_refined.append(phrase_modified)

        else:  # eventually [a:b] (0 < a < b)
            t_value_a = self.ntp_info_dict['ingredient'][1]
            t_value_b = self.ntp_info_dict['ingredient'][2]
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
        # nest_info_dict = self.instruction_dict['nest_info_dict']

        point = random.randint(0, 1)
        for phrase_sometime in semantics_sometime:
            for phrase_temporal in temporal_info_refined:

                # if nest_info_dict['whetherNest'] and nest_info_dict['nestLayer'] > 1:
                #     if 'first' in phrase_temporal:
                #         continue

                flag = random.randint(0, 1)
                if flag == 0:  # do not add adverb
                    if point == 0:
                        phrase_at_sometime = 'at ' + phrase_sometime
                    else:
                        if 'after' not in phrase_temporal:
                            phrase_at_sometime = 'after ' + phrase_sometime
                        else:
                            phrase_at_sometime = 'at ' + phrase_sometime
                    eng = phrase_at_sometime + ' ' + phrase_temporal
                else:  # add adverb
                    adverb = random.choice(adv_list)
                    if point == 0:
                        phrase_at_sometime = 'at ' + phrase_sometime
                    else:
                        if 'after' not in phrase_temporal:
                            phrase_at_sometime = 'after ' + phrase_sometime
                        else:
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
        point = random.randint(0, 1)
        if point == 0:
            new_template['conjunction'] = ', at which'
        else:
            new_template['conjunction'] = ', after which'

        predicate_cmd_dict = copy.deepcopy(self.eventually_predicate_cmd_dict['main'])
        adverbial_list = copy.deepcopy(self.eventually_adverbial_dict['adv_general_list'])
        quick_refiner_assembler = EventuallyAtomQuickRefinerAssembler(new_template, predicate_cmd_dict, adverbial_list)
        self.eventually_eng_temporal_clause = quick_refiner_assembler.eng_list

        return self.eventually_eng_temporal_clause

    def always_temporal_phrase_process(self):
        temporal_info_raw = copy.deepcopy(self.always_template['temporal_phrase'])
        eng_temporal_phrase = []
        nest_info_dict = self.instruction_dict['nest_info_dict']

        if self.always_index == [1, 0]:  # always
            eng_temporal_phrase = temporal_info_raw

        elif self.always_index == [1, 1]:  # always [0:t] (0 < t)
            t_value = self.ntp_info_dict['ingredient'][-1]
            for phrase in temporal_info_raw:
                if nest_info_dict['whetherNest'] and nest_info_dict['nestLayer'] > 1:
                    if 'first' in phrase:
                        continue
                phrase_modified = phrase.replace('t_value', t_value)
                eng_temporal_phrase.append(phrase_modified)

        else:  # always [a:b] (0 < a < b)
            t_value_a = self.ntp_info_dict['ingredient'][-2]
            t_value_b = self.ntp_info_dict['ingredient'][-1]
            for phrase in temporal_info_raw:
                if nest_info_dict['whetherNest'] and nest_info_dict['nestLayer'] > 1:
                    if 'first' in phrase:
                        continue
                phrase_modified = phrase.replace('t_value_a', t_value_a)
                phrase_modified = phrase_modified.replace('t_value_b', t_value_b)
                eng_temporal_phrase.append(phrase_modified)

        return eng_temporal_phrase

    def main_sentence_type1_process(self):
        predicate_cmd_dict = self.always_predicate_cmd_dict['main_type1']
        positive_predicate_version = 'alwaysUseDuration'
        main_sentence_refiner = AlwaysAtomTemplateRefiner(self.sp_info_dict, predicate_cmd_dict,
                                                          positive_predicate_version)

        adverbial_query = self.instruction_dict['adverbial_query_main_type1']
        adverbial_para = copy.deepcopy(self.always_adverbial_dict['assemble_list'])
        main_sentence_assembler = AlwaysAtomAssembler(adverbial_query, main_sentence_refiner.assemble_guide,
                                                      adverbial_para)

        return main_sentence_assembler.eng_list

    def main_sentence_type2_process(self):
        eng_main_sentence_type2 = []

        # refine eng_main_sentence_type2_list_1
        predicate_cmd_dict = self.always_predicate_cmd_dict['main_type2_main_part']
        positive_predicate_version = 'alwaysUseLogic'
        main_sentence_refiner = AlwaysAtomTemplateRefiner(self.sp_info_dict, predicate_cmd_dict,
                                                          positive_predicate_version)

        # generate eng_main_sentence_type2_list_1 and generate eng_main_sentence_type2_list_2
        # at runtime according to different types of assemble guide of eng_main_sentence_type2_list_1
        assemble_guide = copy.deepcopy(main_sentence_refiner.assemble_guide)
        while len(assemble_guide) != 0:
            adverbial_query = self.instruction_dict['adverbial_query_main_type2_main_part']
            refined_template_dict = assemble_guide.pop()
            refined_template_list = [refined_template_dict]
            adverbial_para = []
            main_sentence_assembler = AlwaysAtomAssembler(adverbial_query, refined_template_list, adverbial_para)
            # obtain eng_main_sentence_list_1
            eng_main_sentence_list_1 = main_sentence_assembler.eng_list

            sp_category = self.sp_info_dict['index'][0]
            mood = refined_template_dict['mood']
            clause_type = refined_template_dict['clause_type']
            # generate ent_main_sentence_list_2 in the following function and combine it with eng_main_sentence_list_1
            eng_list = self.auxiliary_clause_processing(mood, sp_category, clause_type,
                                                        eng_main_sentence_list_1)

            eng_main_sentence_type2 = eng_main_sentence_type2 + eng_list

            return eng_main_sentence_type2

    def auxiliary_clause_processing(self, mood, sp_category, clause_type, eng_main_sentence_list_1):
        # store generated main sentences of type 2
        eng_list = []

        # preparation
        predicate_cmd_dict = self.always_predicate_cmd_dict['main_type2_clause_part']
        adverbial_para = self.always_adverbial_dict['assemble_list']

        # generate special_clause -- this will be used for all occasions
        new_template = dict()
        # kind
        new_template['kind'] = 'special_clause'
        # conjunction
        new_template['conjunction'] = copy.deepcopy(self.always_template['special_clause']['conjunction'])
        # subject
        new_template['subject'] = copy.deepcopy(self.always_template['special_clause']['subject'])
        # predicate
        new_template['predicate'] = copy.deepcopy(self.always_template['special_clause']['predicate'])

        # get eng_main_sentence_list_2
        quick_refiner_assembler = AlwaysAtomQuickRefinerAssembler(new_template, predicate_cmd_dict, adverbial_para)
        eng_main_sentence_list_2 = copy.deepcopy(quick_refiner_assembler.eng_list)

        eng_main_sentence = self.concatenate_special_clause(eng_main_sentence_list_1, eng_main_sentence_list_2)
        eng_list = eng_list + eng_main_sentence

        if mood == 'positive':
            # generate clause_general -- this will be used for all positive version of main_sentence_list_1
            new_template = dict()
            # kind
            new_template['kind'] = 'clause_general'
            # conjunction
            new_template['conjunction'] = copy.deepcopy(self.always_template['clause_general']['conjunction'])
            # predicate
            new_template['predicate'] = copy.deepcopy(self.always_template['clause_general']['predicate'])
            # object
            new_template['object'] = copy.deepcopy(self.always_template['clause_general']['object'])
            # get eng_main_sentence_list_2
            quick_refiner_assembler = AlwaysAtomQuickRefinerAssembler(new_template, predicate_cmd_dict, adverbial_para)
            eng_main_sentence_list_2 = copy.deepcopy(quick_refiner_assembler.eng_list)

            eng_main_sentence = self.concatenate_clause_general(eng_main_sentence_list_1,
                                                                eng_main_sentence_list_2,
                                                                mood)
            eng_list = eng_list + eng_main_sentence

            if not self.whether_from_not_eventually or \
                    (self.whether_from_not_eventually and self.sp_info_dict['type'] == 'SE'):
                # only accept 'SE' if the translation is triggered from 'not eventually'
                se_category = sp_category

                if se_category == 0:  # value
                    new_template = dict()
                    # kind
                    new_template['kind'] = 'clause_value'
                    # conjunction
                    new_template['conjunction'] = copy.deepcopy(self.always_template['clause_value']['conjunction'])
                    # predicate
                    new_template['predicate'] = copy.deepcopy(self.always_template['clause_value']['predicate'])
                    # object
                    new_template['object'] = copy.deepcopy(self.always_template['clause_value']['object'])
                    # get eng_main_sentence_list_2
                    quick_refiner_assembler = AlwaysAtomQuickRefinerAssembler(new_template, predicate_cmd_dict,
                                                                          adverbial_para)
                    eng_main_sentence_list_2 = copy.deepcopy(quick_refiner_assembler.eng_list)

                    eng_main_sentence = self.concatenate_clause_value(eng_main_sentence_list_1,
                                                                      eng_main_sentence_list_2)
                    eng_list = eng_list + eng_main_sentence

                if 1 <= se_category <= 3:  # range
                    new_template = dict()
                    # kind
                    new_template['kind'] = 'clause_range'
                    # conjunction
                    new_template['conjunction'] = copy.deepcopy(self.always_template['clause_range']['conjunction'])
                    # predicate
                    new_template['predicate'] = copy.deepcopy(self.always_template['clause_range']['predicate'])
                    # object
                    new_template['object'] = copy.deepcopy(self.always_template['clause_range']['object'])
                    # get eng_main_sentence_list_2
                    quick_refiner_assembler = AlwaysAtomQuickRefinerAssembler(new_template, predicate_cmd_dict,
                                                                          adverbial_para)
                    eng_main_sentence_list_2 = copy.deepcopy(quick_refiner_assembler.eng_list)

                    eng_main_sentence = self.concatenate_clause_range(eng_main_sentence_list_1,
                                                                      eng_main_sentence_list_2)
                    eng_list = eng_list + eng_main_sentence

                if 4 <= se_category <= 5:  # mode
                    new_template = dict()
                    # kind
                    new_template['kind'] = 'clause_mode'
                    # conjunction
                    new_template['conjunction'] = copy.deepcopy(self.always_template['clause_mode']['conjunction'])
                    # predicate
                    new_template['predicate'] = copy.deepcopy(self.always_template['clause_mode']['predicate'])
                    # object
                    new_template['object'] = copy.deepcopy(self.always_template['clause_mode']['object'])
                    # get eng_main_sentence_list_2
                    quick_refiner_assembler = AlwaysAtomQuickRefinerAssembler(new_template, predicate_cmd_dict,
                                                                          adverbial_para)
                    eng_main_sentence_list_2 = copy.deepcopy(quick_refiner_assembler.eng_list)

                    eng_main_sentence = self.concatenate_clause_mode(eng_main_sentence_list_1, eng_main_sentence_list_2)
                    eng_list = eng_list + eng_main_sentence

        else:  # mood == 'negative'
            if clause_type == 'NoPrefixNoSuffix':
                new_template = dict()
                # kind
                new_template['kind'] = 'clause_general'
                # conjunction
                new_template['conjunction'] = copy.deepcopy(self.always_template['clause_general']['conjunction'])
                # predicate
                new_template['predicate'] = copy.deepcopy(self.always_template['clause_general']['predicate'])
                # object
                new_template['object'] = copy.deepcopy(self.always_template['clause_general']['object'])
                # get eng_main_sentence_list_2
                quick_refiner_assembler = AlwaysAtomQuickRefinerAssembler(new_template, predicate_cmd_dict, adverbial_para)
                eng_main_sentence_list_2 = eng_main_sentence_list_2 + copy.deepcopy(quick_refiner_assembler.eng_list)

                eng_main_sentence = self.concatenate_clause_general(eng_main_sentence_list_1,
                                                                    eng_main_sentence_list_2,
                                                                    mood)
                eng_list = eng_list + eng_main_sentence

            if clause_type == 'PrefixSuffix':
                pass

        return eng_list

    @staticmethod
    def concatenate_special_clause(eng_main_sentence_list_1, eng_main_sentence_list_2):
        eng_main_sentence = []
        for main1 in eng_main_sentence_list_1:
            for main2 in eng_main_sentence_list_2:
                main = main1 + ' ' + main2
                eng_main_sentence.append(main)

        return eng_main_sentence

    def concatenate_clause_general(self, eng_main_sentence_list_1, eng_main_sentence_list_2, mood):
        eng_main_sentence = []
        main_sentence_1 = copy.deepcopy(eng_main_sentence_list_1)
        main_sentence_2 = copy.deepcopy(eng_main_sentence_list_2)

        if mood == 'positive':
            for main1 in main_sentence_1:
                for main2 in main_sentence_2:
                    # check whether the tense or modal type of main1 and main2 is the same and do modification
                    [main1_modified, main2_modified] = self.tense_modal_check_modify(main1, main2)
                    main = main1_modified + ' ' + main2_modified
                    # main = main1 + ' ' + main2
                    eng_main_sentence.append(main)
        else:  # mood == 'negative'
            for main1 in main_sentence_1:
                for main2 in main_sentence_2:
                    main = main1 + ' ' + main2
                    eng_main_sentence.append(main)

        return eng_main_sentence

    def concatenate_clause_value(self, eng_main_sentence_list_1, eng_main_sentence_list_2):
        eng_main_sentence = []
        main_sentence_1 = copy.deepcopy(eng_main_sentence_list_1)
        main_sentence_2 = copy.deepcopy(eng_main_sentence_list_2)

        for main1 in main_sentence_1:
            if 'the value of' in main1:
                continue
            else:
                for main2 in main_sentence_2:  # main2 always has word 'value' in it
                    # check whether the tense or modal type of main1 and main2 is the same and do modification
                    [main1_modified, main2_modified] = self.tense_modal_check_modify(main1, main2)
                    main = main1_modified + ' ' + main2_modified
                    eng_main_sentence.append(main)

        return eng_main_sentence

    def concatenate_clause_range(self, eng_main_sentence_list_1, eng_main_sentence_list_2):
        eng_main_sentence = []
        main_sentence_1 = copy.deepcopy(eng_main_sentence_list_1)
        main_sentence_2 = copy.deepcopy(eng_main_sentence_list_2)

        for main1 in main_sentence_1:
            if 'out' in main1 or 'outside' in main1:
                continue
            else:
                for main2 in main_sentence_2:  # main2 always has word 'value' in it
                    # check whether the tense or modal type of main1 and main2 is the same and do modification
                    [main1_modified, main2_modified] = self.tense_modal_check_modify(main1, main2)
                    main = main1_modified + ' ' + main2_modified
                    eng_main_sentence.append(main)

        return eng_main_sentence

    def concatenate_clause_mode(self, eng_main_sentence_list_1, eng_main_sentence_list_2):
        eng_main_sentence = []
        main_sentence_1 = copy.deepcopy(eng_main_sentence_list_1)
        main_sentence_2 = copy.deepcopy(eng_main_sentence_list_2)

        for main1 in main_sentence_1:
            if 'the state of' in main1 or 'the mode of' in main1 or 'neither' in main1:
                continue
            else:
                for main2 in main_sentence_2:  # main2 always has word 'state' or 'mode' in it
                    # check whether the tense or modal type of main1 and main2 is the same and do modification
                    [main1_modified, main2_modified] = self.tense_modal_check_modify(main1, main2)
                    main = main1_modified + ' ' + main2_modified
                    eng_main_sentence.append(main)

        return eng_main_sentence

    def tense_modal_check_modify(self, main1, main2):
        main_1 = copy.deepcopy(main1)
        main_2 = copy.deepcopy(main2)
        main_1_modified = main_1
        prob = 50  # probability that flag is equal to 1

        if 'will' in main_1 and 'will' in main_2:
            flag = self.random_function(prob)  # flag will be 1 with probability prob %
            if flag == 1:
                main_2_list = main_2.split(' ')
                main_2_list.remove('will')
                main_2_modified = ' '.join(main_2_list)
            else:
                main_2_modified = main_2

        elif 'would' in main_1 and 'would' in main_2:
            flag = self.random_function(prob)  # flag will be 1 with probability prob %
            if flag == 1:
                main_2_list = main_2.split(' ')
                main_2_list.remove('would')
                main_2_modified = ' '.join(main_2_list)
            else:
                main_2_modified = main_2

        elif 'should' in main_1 and 'should' in main_2:
            flag = self.random_function(prob)  # flag will be 1 with probability prob %
            if flag == 1:
                main_2_list = main_2.split(' ')
                main_2_list.remove('should')
                main_2_modified = ' '.join(main_2_list)
            else:
                main_2_modified = main_2

        elif 'ought to' in main_1 and 'ought to' in main_2:
            flag = self.random_function(prob)  # flag will be 1 with probability prob %
            if flag == 1:
                main_2_list = main_2.split(' ')
                main_2_list.remove('ought')
                main_2_list.remove('to')
                main_2_modified = ' '.join(main_2_list)
            else:
                main_2_modified = main_2

        elif 'must' in main_1 and 'must' in main_2:
            flag = self.random_function(prob)  # flag will be 1 with probability prob %
            if flag == 1:
                main_2_list = main_2.split(' ')
                main_2_list.remove('must')
                main_2_modified = ' '.join(main_2_list)
            else:
                main_2_modified = main_2

        elif 'shall' in main_1 and 'shall' in main_2:
            flag = self.random_function(prob)  # flag will be 1 with probability prob %
            if flag == 1:
                main_2_list = main_2.split(' ')
                main_2_list.remove('shall')
                main_2_modified = ' '.join(main_2_list)
            else:
                main_2_modified = main_2

        elif 'has to' in main_1 and 'has to' in main_2:
            flag = self.random_function(prob)  # flag will be 1 with probability prob %
            if flag == 1:
                main_2_list = main_2.split(' ')
                main_2_list.remove('has')
                main_2_list.remove('to')
                main_2_modified = ' '.join(main_2_list)
            else:
                main_2_modified = main_2

        elif 'had to' in main_1 and 'had to' in main_2:
            flag = self.random_function(prob)  # flag will be 1 with probability prob %
            if flag == 1:
                main_2_list = main_2.split(' ')
                main_2_list.remove('had')
                main_2_list.remove('to')
                main_2_modified = ' '.join(main_2_list)
            else:
                main_2_modified = main_2

        elif 'will have to' in main_1 and 'will have to' in main_2:
            flag = self.random_function(prob)  # flag will be 1 with probability prob %
            if flag == 1:
                main_2_list = main_2.split(' ')
                main_2_list.remove('will')
                main_2_list.remove('have')
                main_2_list.remove('to')
                main_2_modified = ' '.join(main_2_list)
            else:
                main_2_modified = main_2

        elif 'would have to' in main_1 and 'would have to' in main_2:
            flag = self.random_function(prob)  # flag will be 1 with probability prob %
            if flag == 1:
                main_2_list = main_2.split(' ')
                main_2_list.remove('would')
                main_2_list.remove('have')
                main_2_list.remove('to')
                main_2_modified = ' '.join(main_2_list)
            else:
                main_2_modified = main_2

        elif 'needs to' in main_1 and 'needs to' in main_2:
            flag = self.random_function(prob)  # flag will be 1 with probability prob %
            if flag == 1:
                main_2_list = main_2.split(' ')
                main_2_list.remove('needs')
                main_2_list.remove('to')
                main_2_modified = ' '.join(main_2_list)
            else:
                main_2_modified = main_2

        elif 'needed to' in main_1 and 'needed to' in main_2:
            flag = self.random_function(prob)  # flag will be 1 with probability prob %
            if flag == 1:
                main_2_list = main_2.split(' ')
                main_2_list.remove('needed')
                main_2_list.remove('to')
                main_2_modified = ' '.join(main_2_list)
            else:
                main_2_modified = main_2

        else:
            main_2_modified = main_2

        return [main_1_modified, main_2_modified]

    @staticmethod
    def random_function(prob):
        point = random.randint(1, 100)
        if point <= prob:
            flag = 1
        else:
            flag = 0
        return flag

    def display_key_list(self):
        count = 1
        for eng in self.always_eng_temporal_phrase:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

        count = 1
        for eng in self.eng_main_sentence_type1:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

        count = 1
        for eng in self.eng_main_sentence_type2:
            print('%d: %s' % (count, eng))
            count = count + 1

    def pack_key_list(self):
        return [self.eventually_eng_temporal_phrase,
                self.eventually_eng_temporal_clause,
                self.always_eng_temporal_phrase,
                self.eng_main_sentence_type1,
                self.eng_main_sentence_type2]
