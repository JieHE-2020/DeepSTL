from translation.level_2.TP_atom.original_TP_atom.eventually.simplest.simplest_eventually_atom_preprocessor \
    import SimplestEventuallyAtomPreprocessor
from commands.command_eventually import PreCmdEventually
from commands.command_until import PreCmdUntil
import copy


class SimplestUntilAtomEventuallyPreprocessor(SimplestEventuallyAtomPreprocessor):
    """
    functions:
    1. process the temporal information of 'eventually' operator in the form of phrase
       and assemble the ingredients into English expressions
    2. refine the templates of Atom expressions and assemble them into English translations
    """

    # override function 'command_process' in class SimplestEventuallyAtomPreprocessor
    # NOTE: this function is not the same as function 'command_process' in class UntilAtomEventuallyType1Preprocessor
    def command_process(self):
        adverb_dict = copy.deepcopy(self.adverbial_dict['refine_dict'])
        pre_cmd = PreCmdEventually(adverb_dict)
        pre_cmd_until = PreCmdUntil(adverb_dict)

        position = self.instruction_dict['position']
        tense = self.instruction_dict['nest_info_dict']['tense']

        if tense == 'present':
            if position == 'before_imply':
                # without future tense (with 100% probability)
                main_cmd_dict = copy.deepcopy(pre_cmd_until.eventually_present_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_after_imply)
            appositive_cmd_dict = copy.deepcopy(pre_cmd.present_cmd_dic_appositive)

        elif tense == 'future':
            if position == 'before_imply':
                # without future tense (with 100% probability)
                main_cmd_dict = copy.deepcopy(pre_cmd_until.eventually_future_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_after_imply)
            appositive_cmd_dict = copy.deepcopy(pre_cmd.future_cmd_dic_appositive)

        else:  # tense == 'past'
            if position == 'before_imply':
                # without future tense (with 100% probability)
                main_cmd_dict = copy.deepcopy(pre_cmd_until.eventually_past_cmd_dic_before_imply)
            else:  # position == 'after_imply'
                main_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_after_imply)
            appositive_cmd_dict = copy.deepcopy(pre_cmd.past_cmd_dic_appositive)

        predicate_cmd_dict = {
            'main': main_cmd_dict,
            'appositive': appositive_cmd_dict
        }

        return predicate_cmd_dict

