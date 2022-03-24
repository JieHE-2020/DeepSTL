from commands.command_eventually import PreCmdEventually
from commands.command_until import PreCmdUntil
from translation.level_2.TP_atom.original_TP_atom.eventually.normal.eventually_atom_preprocessor \
    import EventuallyAtomPreprocessor
import copy
import random


class UntilAtomEventuallyType1Preprocessor(EventuallyAtomPreprocessor):

    def command_process(self):
        adverb_dict = copy.deepcopy(self.adverbial_dict['refine_dict'])
        pre_cmd = PreCmdEventually(adverb_dict)
        pre_cmd_until = PreCmdUntil(adverb_dict)

        position = self.instruction_dict['position']
        tense = self.instruction_dict['nest_info_dict']['tense']

        if tense == 'present':
            if position == 'before_imply':
                point = random.randint(0, 1)
                if point == 0:
                    # including future tense (with 50% probability)
                    main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_before_imply)
                else:
                    # without future tense (with 50% probability)
                    main_cmd_dict = copy.deepcopy(pre_cmd_until.eventually_present_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_after_imply)
            appositive_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_appositive)

        elif tense == 'future':
            if position == 'before_imply':
                point = random.randint(0, 1)
                if point == 0:
                    # including future tense (with 50% probability)
                    main_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_before_imply)
                else:
                    # without future tense (with 50% probability)
                    main_cmd_dict = copy.deepcopy(pre_cmd_until.eventually_future_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_after_imply)
            appositive_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_appositive)

        else:  # tense == 'past'
            if position == 'before_imply':
                point = random.randint(0, 1)
                if point == 0:
                    # including future tense (with 50% probability)
                    main_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_before_imply)
                else:
                    # without future tense (with 50% probability)
                    main_cmd_dict = copy.deepcopy(pre_cmd_until.eventually_past_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_after_imply)
            appositive_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_appositive)

        predicate_cmd_dict = {
            'main': main_cmd_dict,
            'appositive': appositive_cmd_dict
        }

        return predicate_cmd_dict

