from commands import command
from selection.atom_select import AtomSelector
from translation.PureSP.atom_template_refiner import AtomTemplateRefiner
from translation.PureSP.atom_assembler import AtomAssembler
from corpus import adverbial_modifiers
import random
#
# # SE
# # category 0
# # se_dic = {'index': [0, 0], 'ingredient': ['Spd_Act_Meas', '91'], 'expression': 'Spd_Act_Meas == 91'}
# # se_dic = {'index': [0, 1], 'ingredient': ['vt', '3.1'], 'expression': 'not (vt == 3.1)'}
# # se_dic = {'index': [0, 2], 'ingredient': ['V_PWM', '79'], 'expression': 'not rise (V_PWM == 79)'}
# se_dic = {'index': [0, 3], 'ingredient': ['T_DMOS', '60.6'], 'expression': 'not fall (T_DMOS == 60.6)'}
#
# category 1
# se_dic = {'index': [1, 0], 'ingredient': ['V_S(Rev)', '78'], 'expression': 'V_S(Rev) >= 78'}
# se_dic = {'index': [1, 1], 'ingredient': ['V_S(Rev)', '78'], 'expression': 'V_S(Rev) > 78'}
# se_dic = {'index': [1, 2], 'ingredient': ['bl', '29.0'], 'expression': 'not (bl >= 29.0)'}
# se_dic = {'index': [1, 3], 'ingredient': ['bl', '29.0'], 'expression': 'not (bl > 29.0)'}
# se_dic = {'index': [1, 4], 'ingredient': ['pw', '18.8'], 'expression': 'not rise (pw >= 18.8)'}
# se_dic = {'index': [1, 5], 'ingredient': ['pw', '18.8'], 'expression': 'not rise (pw > 18.8)'}
# se_dic = {'index': [1, 6], 'ingredient': ['Spd_Tgt', '39.4'], 'expression': 'not fall (Spd_Tgt >= 39.4)'}
# se_dic = {'index': [1, 7], 'ingredient': ['Spd_Tgt', '39.4'], 'expression': 'not fall (Spd_Tgt > 39.4)'}

#
# category 2
# se_dic = {'index': [2, 0], 'ingredient': ['V_Inv', '80'], 'expression': 'V_Inv <= 80'}
# se_dic = {'index': [2, 1], 'ingredient': ['V_Inv', '80'], 'expression': 'V_Inv < 80'}
# se_dic = {'index': [2, 2], 'ingredient': ['I_InX', '13'], 'expression': 'not (I_InX <= 13)'}
# se_dic = {'index': [2, 3], 'ingredient': ['I_InX', '13'], 'expression': 'not (I_InX < 13)'}
# se_dic = {'index': [2, 4], 'ingredient': ['S_In', '48.6'], 'expression': 'not rise (S_In <= 48.6)'}
# se_dic = {'index': [2, 5], 'ingredient': ['S_In', '48.6'], 'expression': 'not rise (S_In < 48.6)'}
# se_dic = {'index': [2, 6], 'ingredient': ['V_GND', '89.4'], 'expression': 'not fall (V_GND <= 89.4)'}
# se_dic = {'index': [2, 7], 'ingredient': ['V_GND', '89.4'], 'expression': 'not fall (V_GND < 89.4)'}
#
# category 3
# se_dic = {'index': [3, 0], 'ingredient': ['S_In', '60', '89'], 'expression': 'S_In >= 60 and S_In <= 89'}
# se_dic = {'index': [3, 1], 'ingredient': ['S_In', '60', '89'], 'expression': 'S_In > 60 and S_In <= 89'}
# se_dic = {'index': [3, 2], 'ingredient': ['S_In', '60', '89'], 'expression': 'S_In >= 60 and S_In < 89'}
# se_dic = {'index': [3, 3], 'ingredient': ['S_In', '60', '89'], 'expression': 'S_In > 60 and S_In < 89'}
# se_dic = {'index': [3, 4], 'ingredient': ['Spd_Act_Meas', '13', '40'], 'expression': 'not (Spd_Act_Meas >= 13 and Spd_Act_Meas <= 40)'}
# se_dic = {'index': [3, 5], 'ingredient': ['Spd_Act_Meas', '13', '40'], 'expression': 'not (Spd_Act_Meas > 13 and Spd_Act_Meas <= 40)'}
# se_dic = {'index': [3, 6], 'ingredient': ['Spd_Act_Meas', '13', '40'], 'expression': 'not (Spd_Act_Meas >= 13 and Spd_Act_Meas < 40)'}
# se_dic = {'index': [3, 7], 'ingredient': ['Spd_Act_Meas', '13', '40'], 'expression': 'not (Spd_Act_Meas > 13 and Spd_Act_Meas < 40)'}
# se_dic = {'index': [3, 8], 'ingredient': ['V_InGND', '66.0', '68.4'], 'expression': 'not rise (V_InGND >= 66.0 and V_InGND <= 68.4)'}
# se_dic = {'index': [3, 9], 'ingredient': ['V_InGND', '66.0', '68.4'], 'expression': 'not rise (V_InGND > 66.0 and V_InGND <= 68.4)'}
# se_dic = {'index': [3, 10], 'ingredient': ['V_InGND', '66.0', '68.4'], 'expression': 'not rise (V_InGND >= 66.0 and V_InGND < 68.4)'}
# se_dic = {'index': [3, 11], 'ingredient': ['V_InGND', '66.0', '68.4'], 'expression': 'not rise (V_InGND > 66.0 and V_InGND < 68.4)'}
# se_dic = {'index': [3, 12], 'ingredient': ['wl', '32', '86'], 'expression': 'not fall (wl >= 32 and wl <= 86)'}
# se_dic = {'index': [3, 13], 'ingredient': ['wl', '32', '86'], 'expression': 'not fall (wl > 32 and wl <= 86)'}
# se_dic = {'index': [3, 14], 'ingredient': ['wl', '32', '86'], 'expression': 'not fall (wl >= 32 and wl < 86)'}
# se_dic = {'index': [3, 15], 'ingredient': ['wl', '32', '86'], 'expression': 'not fall (wl > 32 and wl < 86)'}

# category 4
# se_dic = {'index': [4, 0], 'ingredient': ['OTsig', 'Passive'], 'expression': 'OTsig == Passive'}
# se_dic = {'index': [4, 1], 'ingredient': ['PowTrans', 'Default'], 'expression': 'not (PowTrans == Default)'}
# se_dic = {'index': [4, 2], 'ingredient': ['CH', 'Triggered'], 'expression': 'not rise (CH == Triggered)'}
# se_dic = {'index': [4, 3], 'ingredient': ['Dv', 'Running'], 'expression': 'not fall (Dv == Running)'}

# category 5
# se_dic = {'index': [5, 0], 'ingredient': ['V_Logic', 'Activated', 'OFF'], 'expression': 'V_Logic == Activated or V_Logic == OFF'}
# se_dic = {'index': [5, 1], 'ingredient': ['OutTrans', 'FAULT', 'Stable'], 'expression': 'not (OutTrans == FAULT or OutTrans == Stable)'}
# se_dic = {'index': [5, 2], 'ingredient': ['OutTrans', 'Running', 'Clamped'], 'expression': 'not rise (OutTrans == Running or OutTrans == Clamped)'}
# se_dic = {'index': [5, 3], 'ingredient': ['IN', 'Inhibited', 'ON'],'expression': 'not fall (IN == Inhibited or IN == ON)'}
#

# ERE
# category 0
# ere_dic = {'index': [0, 0], 'ingredient': ['I_DEN', '0.6'], 'expression': 'rise (I_DEN == 0.6)'}
# ere_dic = {'index': [0, 1], 'ingredient': ['S_In', '31'], 'expression': 'fall (S_In == 31)'}

# category 1
# ere_dic = {'index': [1, 0], 'ingredient': ['I_DEN', '18'], 'expression': 'rise (I_DEN >= 18)'}
# ere_dic = {'index': [1, 1], 'ingredient': ['V_S(Rev)', '11'], 'expression': 'rise (V_S(Rev) > 11)'}
# ere_dic = {'index': [1, 2], 'ingredient': ['id', '41.1'], 'expression': 'fall (id >= 41.1)'}
# ere_dic = {'index': [1, 3], 'ingredient': ['I_L(Inv)', '53'], 'expression': 'fall (I_L(Inv) > 53)'}
#
# category 2
# ere_dic = {'index': [2, 0], 'ingredient': ['vt', '75.9'], 'expression': 'rise (vt <= 75.9)'}
# ere_dic = {'index': [2, 1], 'ingredient': ['V_Sply', '25.3'], 'expression': 'rise (V_Sply < 25.3)'}
# ere_dic = {'index': [2, 2], 'ingredient': ['I_IS', '86'], 'expression': 'fall (I_IS <= 86)'}
# ere_dic = {'index': [2, 3], 'ingredient': ['I_L(Inv)', '59.7'], 'expression': 'fall (I_L(Inv) < 59.7)'}

# category 3
# ere_dic = {'index': [3, 0], 'ingredient': ['DQ', '89', '98'], 'expression': 'rise (DQ >= 89 and DQ <= 98)'}
# ere_dic = {'index': [3, 1], 'ingredient': ['angle', '25', '58'], 'expression': 'rise (angle > 25 and angle <= 58)'}
# ere_dic = {'index': [3, 2], 'ingredient': ['V_PWM', '3', '91'], 'expression': 'rise (V_PWM >= 3 and V_PWM < 91)'}
# ere_dic = {'index': [3, 3], 'ingredient': ['I_GND', '70', '80'], 'expression': 'rise (I_GND > 70 and I_GND < 80)'}
# ere_dic = {'index': [3, 4], 'ingredient': ['bl', '41.4', '95.4'], 'expression': 'fall (bl >= 41.4 and bl <= 95.4)'}
# ere_dic = {'index': [3, 5], 'ingredient': ['V_Sply', '45', '97'], 'expression': 'fall (V_Sply > 45 and V_Sply <= 97)'}
# ere_dic = {'index': [3, 6], 'ingredient': ['V_GND', '85.8', '96.0'], 'expression': 'fall (V_GND >= 85.8 and V_GND < 96.0)'}
# ere_dic = {'index': [3, 7], 'ingredient': ['pw', '61.0', '80.7'], 'expression': 'fall (pw > 61.0 and pw < 80.7)'}

# category 4
# ere_dic = {'index': [4, 0], 'ingredient': ['UM', 'Running'], 'expression': 'rise (UM == Running)'}
# ere_dic = {'index': [4, 1], 'ingredient': ['OTsig', 'OFF'], 'expression': 'fall (OTsig == OFF)'}

# category 5
# ere_dic = {'index': [5, 0], 'ingredient': ['BT', 'Activated', 'Default'], 'expression': 'rise (BT == Activated or BT == Default)'}
# ere_dic = {'index': [5, 1], 'ingredient': ['V_Logic', 'Running', 'OFF'], 'expression': 'fall (V_Logic == Running or V_Logic == OFF)'}


# for small testing
# cmd1_positive = [{'present': ['single']}]
# cmd1_negative = [{'present': ['single_not_without_abbreviation', 'single_not_with_abbreviation']}]
# predicate_cmd_none = {'positive': cmd1_positive,
#                       'negative': cmd1_negative,
#                       }
#
# adv_dic = {'adverb': ['immediately']}
# cmd2_positive = [{'present': ['single', adv_dic]}]
# cmd2_negative = [{'present': ['single_not_without_abbreviation', adv_dic, 'single_not_with_abbreviation']}]
# predicate_cmd_adv = {'positive': cmd2_positive,
#                      'negative': cmd2_negative,
#                      }
# predicate_cmd_dict_list = [predicate_cmd_none, predicate_cmd_adv]

adverbial_query = 'adverbialEnabled'

select_cmd = random.randint(0, 1)
if select_cmd == 0:
    atom_type = 'SE'
else:
    atom_type = 'ERE'
atom_selector = AtomSelector(atom_type)
info_dict = atom_selector.info_dict
# info_dict = {'type': 'ERE', 'index': [1, 1], 'ingredient': ['V_Logic', '100'], 'expression': 'rise (V_Logic > 100)'}
# info_dict = {'type': 'SE', 'index': [3, 8], 'ingredient': ['V_InGND', '66.0', '68.4'], 'expression': 'not rise (V_InGND >= 66.0 and V_InGND <= 68.4)'}
print(info_dict)

adverb_dict = adverbial_modifiers.adv_simultaneously
pre_cmd = command.PreCmdOverall(adverb_dict)
predicate_cmd_dict_list = [pre_cmd.cmd_dic_before_imply, pre_cmd.cmd_dic_after_imply]
print(pre_cmd.cmd_dic_after_imply)

option = {
    'adverbial_query': 'adverbialEnabled',
    # diversityReserved, diversityNotReserved
    'verb_format_query': 'diversityReserved',
    'temporal_operator': 'no',
    # randomUseDuration, alwaysUseDuration, alwaysUseLogic
    'positive_predicate_version': 'randomUseDuration'
}
refiner = AtomTemplateRefiner(info_dict, predicate_cmd_dict_list, option)
refiner.display_assemble_guide()

adv_list = adverbial_modifiers.adv_simultaneously['adverb']
adv_phrase_list = adverbial_modifiers.adv_phrase_simultaneously['adverbial_phrase']
adverbial_para = [adv_list, adv_phrase_list]

assembler = AtomAssembler(refiner.option, refiner.assemble_guide, adverbial_para)
assembler.display_translation()