# signal name group 1
# the value of the signal in this group is continuous, i.e., in real value
# signal_continuous = [
#     'Spd_Act',
#     'Spd_Act_Meas',
#     'Spd_Tgt',
#     'V_Sply',
#     'V_Mot',
#     'V_PWM',
#     'V_Inv',
#     'V_S',
#     'V_Logic',
#     'V_GND',
#     'V_InGND',
#     'V_INx',
#     'V_DSEL',
#     'V_DEN',
#     'V_S(Rev)',
#     'I_Inv',
#     'I_L(Inv)',
#     'I_GND',
#     'I_IS',
#     'I_DSEL',
#     'I_DEN',
#     'I_InX',
#     'S_OutTrans',
#     'S_In',
#     'T_DMOS',
#     'Phi',
#     'angle',
#     'x',
#     'bl',
#     'pw',
#     'wl',
#     's',
#     'vt',
#     'id',
#     'DQS',
#     'DQ'
# ]
#
# # signal name group 2
# # the value of the signal in this group is discrete, i.e., in a certain mode
# signal_discrete = [
#     'Op_Cmd',
#     'Op_Ind',
#     'IN',
#     'OUT',
#     'CH',
#     'OL',
#     'OTsig',
#     'Dv',
#     'UM',
#     'PowTrans',
#     'OutTrans',
#     'V_Logic',
#     'BT'
# ]
#
# mode = [
#     'Passive',
#     'Running',
#     'ON',
#     'Activated',
#     'Triggered',
#     'OFF',
#     'Inhibited',
#     'Clamped',
#     'Stable',
#     'FAULT',
#     'Default'
# ]
#
# substitution = [
#     'Trq',
#     'Inverse',
#     'MG',
#     'LG',
#     'DG',
#     'IoutDMOS',
#     'Overvoltage',
#     'RP',
#     'not_pgm',
#     'erasing_cond',
#     'dqs_above_vihdcmin',
#     'dqs_above_vilacmax',
#     'dq_in_fsr',
#     'dqs_in_fsr',
#     'top_left_region'
# ]


verb_bank = {
    'be_singular': ['be', 'is', 'was', 'being', 'been'],
    'be_plural': ['be', 'are', 'were', 'being', 'been'],
    'do': ['do', 'does', 'did', 'doing', 'done'],
    'equal': ['equal', 'equals', 'equaled', 'equaling', 'equaled'],
    'stay': ['stay', 'stays', 'stayed', 'staying', 'stayed'],
    'remain': ['remain', 'remains', 'remained', 'remaining', 'remained'],
    'keep': ['keep', 'keeps', 'kept', 'keeping', 'kept'],
    'change': ['change', 'changes', 'changed', 'changing', 'changed'],
    'shift': ['shift', 'shifts', 'shifted', 'shifting', 'shifted'],
    'get': ['get', 'gets', 'got', 'getting', 'got'],
    'become': ['become', 'becomes', 'became', 'becoming', 'become'],
    'happen': ['happen', 'happens', 'happened', 'happening', 'happened'],
    'occur': ['occur', 'occurs', 'occurred', 'occurring', 'occurred'],
    'deviate': ['deviate', 'deviates', 'deviated', 'deviating', 'deviated'],
    'begin': ['begin', 'begins', 'began', 'beginning', 'begun'],
    'start': ['start', 'starts', 'started', 'starting', 'started'],
    'exceed': ['exceed', 'exceeds', 'exceeded', 'exceeding', 'exceeded'],
    'increase': ['increase', 'increases', 'increased', 'increasing', 'increased'],
    'go': ['go', 'goes', 'went', 'going', 'gone'],
    'jump': ['jump', 'jumps', 'jumped', 'jumping', 'jumped'],
    'cross': ['cross', 'crosses', 'crossed', 'crossing', 'crossed'],
    'decrease': ['decrease', 'decreases', 'decreased', 'decreasing', 'decreased'],
    'fall': ['fall', 'falls', 'fell', 'falling', 'fallen'],
    'lay': ['lay', 'lays', 'laid', 'laying', 'laid'],
    'linger': ['linger', 'lingers', 'lingered', 'lingering', 'lingered'],
    'enter': ['enter', 'enters', 'entered', 'entering', 'entered'],
    'leave': ['leave', 'leaves', 'left', 'leaving', 'left'],
    'rise': ['rise', 'rises', 'rose', 'rising', 'risen'],
    'raise': ['raise', 'raises', 'raised', 'raising', 'raised'],
    'take': ['take', 'takes', 'took', 'taking', 'taken'],
    'exist': ['exist', 'exists', 'existed', 'existing', 'existed'],
    'hold': ['hold', 'holds', 'held', 'holding', 'held'],
    'continue': ['continue', 'continues', 'continued', 'continuing', 'continued'],
    'sustain': ['sustain', 'sustains', 'sustained', 'sustaining', 'sustained'],
    'last': ['last', 'lasts', 'last', 'lasting', 'last'],
    'drop': ['drop', 'drops', 'dropped', 'dropping', 'dropped'],
    'reach': ['reach', 'reaches', 'reached', 'reaching', 'reached'],
    'settle': ['settle', 'settles', 'settled', 'settling', 'settled']

}
