from translation.level_2.TP_atom.original_TP_atom.once.simplest.simplest_once_atom_preprocessor \
    import SimplestOnceAtomPreprocessor
from commands.command_once import PreCmdOnce
from commands.command_since import PreCmdSince
import copy
import random


class SimplestSinceAtomOncePreprocessor(SimplestOnceAtomPreprocessor):
    """
    functions:
    1. process the temporal information of 'once' operator in the form of phrase
       and assemble the ingredients into English expressions
    2. refine the templates of Atom expressions and assemble them into English translations
    """

    # override function 'command_process' in class SimplestOnceAtomPreprocessor
    # NOTE: this function is THE SAME AS function 'command_process' in class SinceAtomOnceType1Preprocessor
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
