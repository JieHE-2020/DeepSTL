from commands.command_once import PreCmdOnce
from commands.command_since import PreCmdSince
from translation.level_2.TP_atom.original_TP_atom.once.normal.once_atom_preprocessor import OnceAtomPreprocessor
import copy
import random


class SinceAtomOnceType1Preprocessor(OnceAtomPreprocessor):

    def command_process(self):
        adverb_dict = copy.deepcopy(self.adverbial_dict['refine_dict'])
        pre_cmd = PreCmdOnce(adverb_dict)
        pre_cmd_since = PreCmdSince(adverb_dict)

        position = self.instruction_dict['position']
        tense = self.instruction_dict['nest_info_dict']['tense']

        if tense == 'present':
            flag = random.randint(1, 10)
            # from the perspective of present time
            if flag <= 2:  # choose with 20% probability
                if position == 'before_imply':
                    # without future tense
                    main_cmd_dict = copy.deepcopy(pre_cmd_since.once_present_cmd_dic_before_imply_present_version)
                else:  # position == 'after_imply'
                    main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_after_imply_present_version)
                appositive_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_appositive_present_version)

            # from the perspective of past time
            else:  # choose with 80% probability
                if position == 'before_imply':
                    # without future tense
                    main_cmd_dict = copy.deepcopy(pre_cmd_since.once_present_cmd_dic_before_imply_past_version)
                else:  # position == 'after_imply'
                    main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_after_imply_past_version)
                appositive_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_appositive_past_version)

        elif tense == 'future':
            if position == 'before_imply':
                # without future tense
                main_cmd_dict = copy.deepcopy(pre_cmd_since.once_future_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_after_imply)
            appositive_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_appositive)

        else:  # tense == 'past'
            if position == 'before_imply':
                # without future tense
                main_cmd_dict = copy.deepcopy(pre_cmd_since.once_past_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_after_imply)
            appositive_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_appositive)

        predicate_cmd_dict = {
            'main': main_cmd_dict,
            'appositive': appositive_cmd_dict
        }

        return predicate_cmd_dict
