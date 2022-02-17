import copy

"""
Section 1: template words for atom expressions (SE and ERE)
"""

# I. Subject
# SE.0-3, ERE.0-3
subject_value_single = ['s#i#g', 'the s#i#g signal', 'the value of s#i#g', 'the value of signal s#i#g']
# SE.4-5, ERE.4-5
subject_mode_single = ['s#i#g', 'the s#i#g signal', 'the state of s#i#g', 'the state of signal s#i#g',
                       'the mode of s#i#g', 'the mode of signal s#i#g']

# prefix of "not rise (...)", "not fall (...)", "rise (...)", "fall (...)"
prefix_event = ['the event that', 'the scenario that', 'the transition action that']

# II. Predicate
# suffix for expressing event in "not rise (...)", "not fall (...)", "rise (...)", "fall (...)"
predicate_event_happen = ['happen', 'occur', 'take place', 'be detected', 'get detected', 'be observed', 'get observed']

############################################### KEY COMPONENT ###############################################

######################################## START 1 ########################################
# Verbs most commonly used in the predicate
# Once modified, they will influence the downstream lists assembled from them
verb_logic = ['be']
verb_duration = ['be', 'stay', 'remain', 'keep']
######################################### END 1 ##########################################

######################################## START 2 ########################################
# The following lists of words are used to assemble the predicates
# with semantics with "obj >= value", "obj > value", "obj <= value", "obj < value"
# and even "obj >=/> value1 and obj <=/< value2"
# Since a good majority of these predicates can be constructed in a unified way,
# they are processed at first

# STEP 1: preparation
# GROUP 1: Many downstream lists are assembled from the lists in this group
# The following four lists include the English semantics of ">=", ">", "<=" and "<"
semantics_atLeast = ['greater than or equal to', 'at least', 'no less than']
bias_semantics_atLeast = ['greater than or equal to', 'greater than or equal to']
semantics_atLeast = semantics_atLeast + bias_semantics_atLeast
# print(semantics_atLeast)

semantics_larger = ['above', 'over', 'more than', 'larger than', 'bigger than', 'higher than', 'greater than']
bias_semantics_larger = []
for i in range(3):
    bias_semantics_larger.append('above')
    bias_semantics_larger.append('larger than')
    bias_semantics_larger.append('higher than')
    bias_semantics_larger.append('greater than')
semantics_larger = semantics_larger + bias_semantics_larger
# print(semantics_larger)

semantics_atMost = ['less than or equal to', 'at most', 'no more than', 'no larger than']
bias_semantics_atMost = []
for i in range(5):
    bias_semantics_atMost.append('less than or equal to')
    if i <= 0:
        bias_semantics_atMost.append('at most')
semantics_atMost = semantics_atMost + bias_semantics_atMost
# print(semantics_atMost)

semantics_smaller = ['below', 'lower than', 'less than', 'smaller than']
bias_semantics_smaller = []
for i in range(5):
    bias_semantics_smaller.append('less than')
    if i <= 1:
        bias_semantics_smaller.append('smaller than')
        bias_semantics_smaller.append('below')
semantics_smaller = semantics_smaller + bias_semantics_smaller
# print(semantics_smaller)

# The following list is used to assemble the predicate of "rise (obj >= value)" or "fall (obj < value)"
# with semantics_atLeast in a unified way
verb_action_upAtLeast = ['increase to', 'rise to', 'go to', 'jump to', 'get to', 'get raised to', 'become']
# The following list is used to assemble the predicate of "rise (obj <= value)" or "fall (obj > value)"
# with semantics_atMost in a unified way
verb_action_downAtMost = ['decrease to', 'fall to', 'drop to', 'go to', 'get to', 'become']

# GROUP 2: Many downstream lists are direct copies of the lists in this group
# The following list is used as the predicate of "rise (obj < value)" or "fall (obj >= value)" in a manual way
# due to the flexibility of English expressions in this occasion
predicate_downSmaller = [
    'decrease below',
    'drop below',
    'fall below',
    'go below', 'go lower than',
    'go down to lower than', 'go down to less than', 'go down to smaller than',
    'get below', 'get lower than', 'get less than', 'get smaller than',
    'become below', 'become lower than', 'become less than', 'become smaller than']
# The following list is used as the predicate of "rise (obj > value)" or "fall (obj <= value)" in a manual way
# due to the flexibility of English expressions in this occasion
predicate_upLarger = [
    'increase above',
    'rise above',
    'go above', 'go over',
    'jump to above', 'jump to more than', 'jump to larger than',
    'jump to higher than', 'jump to over',
    'get above', 'get more than', 'get larger than', 'get bigger than',
    'get higher than', 'get over', 'get raised above',
    'become above', 'become more than', 'become larger than', 'become greater than',
    'become bigger than', 'become higher than', 'become over',
    'cross', 'cross the threshold of',
    'exceed', 'exceed the threshold of'
]
bias_predicate_upLarger = []
for i in range(4):
    bias_predicate_upLarger.append('increase above')
    bias_predicate_upLarger.append('become greater than')
predicate_upLarger = predicate_upLarger + bias_predicate_upLarger
# The following list is used to describe the value of an obj is not within a given range
predicate_notInsideRange_logic = [
    'be out of the range',
    'be in the outside of the range'
]

predicate_notInsideRange_duration = [
    'be out of the range',
    'be in the outside of the range',
    'linger in the outside of the range'
]
semantics_notInsideRange = ['in the outside of the range']
for verb in verb_duration:
    for item in semantics_notInsideRange:
        assembleWords = verb + ' ' + item
        predicate_notInsideRange_duration.append(assembleWords)

# The following list is used as the predicate of "rise (obj >=/> value1 and obj <=/< value2)" in a manual way
# due to the flexibility of English expressions in this occasion
predicate_enterRange = [
    'enter the range',
    'enter the region',
    'enter the bound',
    'get into the range',
    'settle inside the bound'
]
# The following list is used as the predicate of "fall (obj >=/> value1 and obj <=/< value2)" in a manual way
# due to the flexibility of English expressions in this occasion
predicate_leaveRange = [
    'leave the range',
    'get out of the range',
    'go out of the bound'
]

# STEP 2: assembling and copying
# A. obj >= value
# 1. Translate the predicate part of "obj >= value" in a purely logical way
predicate_atLeast_logic = []
for verb in verb_logic:
    for item in semantics_atLeast:
        assembleWords = verb + ' ' + item
        predicate_atLeast_logic.append(assembleWords)

# 2. Translate the predicate part of "obj >= value" with extra information
#    that the statement may last for some while
#    A unified translating method is supported. Other translations can be appended manually.
predicate_atLeast_duration = []
for verb in verb_duration:
    for item in semantics_atLeast:
        assembleWords = verb + ' ' + item
        predicate_atLeast_duration.append(assembleWords)

# 3. Translate the predicate part of "rise (obj >= value)",
#    which means an event that the value of an obj rises to no less than a threshold
#    A unified translating method is supported. Other translations can be appended manually.
predicate_atLeast_riseEvent = []
for verb in verb_action_upAtLeast:
    for item in semantics_atLeast:
        assembleWords = verb + ' ' + item
        predicate_atLeast_riseEvent.append(assembleWords)

# 4. Translate the predicate part of "fall (obj >= value)",
#    which means an event that the value of an obj falls below a threshold
#    A unified translating method is not supported due to the flexibility of English translation
predicate_atLeast_fallEvent = predicate_downSmaller

# B. obj > value
# 1. Translate the predicate part of "obj > value" in a purely logical way
predicate_larger_logic = []
for verb in verb_logic:
    for item in semantics_larger:
        assembleWords = verb + ' ' + item
        predicate_larger_logic.append(assembleWords)

# 2. Translate the predicate part of "obj > value" with extra information
#    that the statement may last for some while
#    A unified translating method is supported. Other translations can be appended manually.
predicate_larger_duration = []
for verb in verb_duration:
    for item in semantics_larger:
        assembleWords = verb + ' ' + item
        predicate_larger_duration.append(assembleWords)

# 3. Translate the predicate part of "rise (obj > value)",
#    which means an event that the value of an obj rises above a threshold
#    A unified translating method is not supported due to the flexibility of English translation
predicate_larger_riseEvent = predicate_upLarger

# 4. Translate the predicate part of "fall (obj > value)",
#    which means an event that the value of an obj falls to no more than a threshold
#    A unified translating method is supported. Other translations can be appended manually.
predicate_larger_fallEvent = []
for verb in verb_action_downAtMost:
    for item in semantics_atMost:
        assembleWords = verb + ' ' + item
        predicate_larger_fallEvent.append(assembleWords)

# C. obj <= value
# 1. Translate the predicate part of "obj <= value" in a purely logical way
predicate_atMost_logic = []
for verb in verb_logic:
    for item in semantics_atMost:
        assembleWords = verb + ' ' + item
        predicate_atMost_logic.append(assembleWords)

# 2. Translate the predicate part of "obj <= value" with extra information
#    that the statement may last for some while
#    A unified translating method is supported. Other translations can be appended manually.
predicate_atMost_duration = []
for verb in verb_duration:
    for item in semantics_atMost:
        assembleWords = verb + ' ' + item
        predicate_atMost_duration.append(assembleWords)

# 3. Translate the predicate part of "rise (obj <= value)",
#    which means an event that the value of an obj decreases to no more than a threshold
#    This is the same with the translation of "fall (obj > value)" in GROUP 3.4
predicate_atMost_riseEvent = predicate_larger_fallEvent

# 4. Translate the predicate part of "fall (obj <= value)",
#    which means an event that the value of an obj increases above a threshold
#    This is the same with the translation of "rise (obj > value)" in GROUP 3.3
predicate_atMost_fallEvent = predicate_larger_riseEvent

# D. obj < value
# 1. Translate the predicate part of "obj < value" in a purely logical way
predicate_smaller_logic = []
for verb in verb_logic:
    for item in semantics_smaller:
        assembleWords = verb + ' ' + item
        predicate_smaller_logic.append(assembleWords)

# 2. Translate the predicate part of "obj < value" with extra information
#    that the statement may last for some while
#    A unified translating method is supported. Other translations can be appended manually.
predicate_smaller_duration = []
for verb in verb_duration:
    for item in semantics_smaller:
        assembleWords = verb + ' ' + item
        predicate_smaller_duration.append(assembleWords)

# 3. Translate the predicate part of "rise (obj < value)",
#    which means an event that the value of an obj falls below a threshold
#    This is the same with the translation of "fall (obj >= value)" in GROUP 2.4
predicate_smaller_riseEvent = predicate_atLeast_fallEvent

# 4. Translate the predicate part of "fall (obj < value)",
#    which means an event that the value of an obj rises to no less than a threshold
#    This is the same with the translation of "rise (obj >= value)" in GROUP 2.3
predicate_smaller_fallEvent = predicate_atLeast_riseEvent

# obj >=/> value1 and obj <=/< value2
predicate_range_logic = verb_logic
predicate_range_duration = verb_duration
predicate_range_notInsideRange_logic = predicate_notInsideRange_logic
predicate_range_notInsideRange_duration = predicate_notInsideRange_duration
predicate_range_riseEvent = predicate_enterRange
predicate_range_fallEvent = predicate_leaveRange
######################################### END 2 ##########################################

######################################## START 3 ########################################
# The following lists of words are used to assemble the predicates
# with semantics with "obj == value", "obj == mode"
# and even "obj == mode1 or obj == mode2"
# Most translation in these parts cannot be constructed in a unified way,
# so attention should be paid to modify them if needed

# A. obj == value
# 1. Translate the predicate part of "obj == value" in a purely logical way
predicate_equalValue_logic = ['be', 'be equal to', 'be set to', 'equal to', 'settle to']
bias_predicate_equalValue_logic = []
for i in range(8):
    bias_predicate_equalValue_logic.append('be')
    bias_predicate_equalValue_logic.append('be equal to')
predicate_equalValue_logic = predicate_equalValue_logic + bias_predicate_equalValue_logic
# print(predicate_equalValue_logic)

# 2. Translate the predicate part of "obj == value" with extra information
#    that the statement may last for some while
# manual part
predicate_equalValue_duration = ['be', 'be set to', 'equal to'] + ['stay at', 'remain on']
# automatic part
semantics_equalValue = ['equal to']
for verb in verb_duration:
    for item in semantics_equalValue:
        assembleWords = verb + ' ' + item
        predicate_equalValue_duration.append(assembleWords)

# 3. Translate the predicate part of "rise (obj == value)",
#    which means an event that the value of an obj changes to a certain number
predicate_equalValue_riseEvent = ['change to', 'shift to', 'be changed to', 'be shifted to',
                                  'get changed to', 'get shifted to', 'get set to', 'get equal to',
                                  'become equal to']

# 4. Translate the predicate part of "fall (obj == value)",
#    which means an event that the value of an obj shifts from a certain number to others
predicate_equalValue_fallEvent = ['deviate from', 'begin deviating from', 'start deviating from',
                                  'start not equaling to', 'become not set to']

# B. obj == mode
# 1. Translate the predicate part of "obj == mode" in a purely logical way
predicate_equalMode_logic = ['be', 'be in', 'be set to']

# 2. Translate the predicate part of "obj == mode" with extra information
#    that the statement may last for some while
# manual part
predicate_equalMode_duration = ['be set to']
# automatic part
semantics_equalMode = ['in']
for verb in verb_duration:
    for item in semantics_equalMode:
        assembleWords = verb + ' ' + item
        predicate_equalMode_duration.append(assembleWords)

# 3. Translate the predicate part of "rise (obj == mode)",
#    which means an event that obj enters to a certain mode
predicate_equalMode_riseEvent = [
    'enter', 'become', 'change to', 'shift to',
    'be changed to', 'be shifted to',
    'get changed to', 'get shifted to', 'get set to'
]

# 4. Translate the predicate part of "fall (obj == mode)",
#    which means an event that obj leaves a certain mode for others
predicate_equalMode_fallEvent = ['leave', 'deviate from', 'begin deviating from',
                                 'start deviating from', 'become not set to']

# C. obj == mode1 or obj == mode2
# 1. Translate the predicate part of "obj == mode1 or obj == mode2" in a purely logical way
predicate_equalModes_logic = predicate_equalMode_logic

# 2. Translate the predicate part of "obj == mode1 or obj == mode2" with extra information
#    that the statement may last for some while
predicate_equalModes_duration = predicate_equalMode_duration

# 3. Translate the predicate part of "rise (obj == mode1 or obj == mode2)",
#    which means an event that obj enters to a certain mode
predicate_equalModes_riseEvent = predicate_equalMode_riseEvent

# 4. Translate the predicate part of "fall (obj == mode)",
#    which means an event that obj leaves a certain mode for others
predicate_equalModes_fallEvent = predicate_equalMode_fallEvent
######################################## END 3 ########################################


# III. Object
# SE.0-3, ERE.0-3
object_value_single = ['value']
# SE.4, ERE.4
object_mode_single = ['mode']
# SE.5, ERE.5
object_mode_double = ['{mode1, mode2}', 'one of {mode1, mode2}', 'mode1 or mode2', 'either mode1 or mode2']
object_mode_double_special = ['neither mode1 nor mode2']

# SE.3
object_range_adj_atLeast = semantics_atLeast
object_range_adj_larger = semantics_larger
object_range_adj_atMost = semantics_atMost
object_range_adj_smaller = semantics_smaller

object_range_prep_general = ['in', 'within', 'between',
                             'in the range', 'within the range', 'between the range',
                             'in the interval', 'within the interval', 'between the interval'
                             ]
object_range_prep_bothClosed = ['in the closed interval', 'within the closed interval', 'between the closed interval']
object_range_prep_bothOpen = ['in the open interval', 'within the open interval', 'between the open interval']

# SE.3, ERE.3 (ERE.3 only uses math format)
object_range_interval_CC_math = ['[value1, value2]']
object_range_interval_CC_eng = ['value1 (closed) and value2 (closed)']
object_range_interval_OC_math = ['(value1, value2]']
object_range_interval_OC_eng = ['value1 (open) and value2 (closed)']
object_range_interval_CO_math = ['[value1, value2)']
object_range_interval_CO_eng = ['value1 (closed) and value2 (open)']
object_range_interval_OO_math = ['(value1, value2)']
object_range_interval_OO_eng = ['value1 (open) and value2 (open)']

"""
Section 2.1: template words for temporal phrases of layer 1
"""
# 1. eventually and once operator
semantics_sometime = ['sometime', 'a certain moment', 'a certain time instant', 'a certain time point', 'a time']
there_be_subject = ['there']
there_be_predicate = ['be', 'exist']
there_be_object = semantics_sometime

# 2. always and historically operator
clause_conjunction = ['and', 'and then']
# general version
clause_predicate_general = copy.deepcopy(verb_duration)
clause_predicate_general.remove('be')
clause_predicate_general = clause_predicate_general + ['hold', 'continue']
clause_object_general = ['like this', 'like that']
# only used for SE.0
clause_predicate_value = ['stay at', 'remain on']
clause_object_value = ['this value']
# only used for SE.1-3
clause_predicate_range = ['stay in', 'remain in']
clause_object_range = ['this range', 'this interval']
# only used for SE.4-5
clause_predicate_mode = clause_predicate_value
clause_object_mode = ['this mode', 'this state']
# general version
special_clause_conjunction = ['and', 'and then', 'then']
special_clause_subject = ['this condition', 'this scenario']
special_clause_predicate = ['last', 'hold', 'continue', 'sustain', 'keep', 'remain']

# 3. until and since operator
attributive_clause_subject = ['which']
attributive_clause_predicate_se = ['be detected', 'get detected', 'be observed', 'get observed']
attributive_clause_predicate_ere = copy.deepcopy(predicate_event_happen)
attributive_clause_temporal_adverbial_part_1 = []
for item in semantics_sometime:
    assembleWords = 'at ' + item
    attributive_clause_temporal_adverbial_part_1.append(assembleWords)

# for 'until'
concatenate_until_1 = ['until then', 'till then', 'before this', 'before that']
concatenate_until_2 = []
for item in concatenate_until_1:
    assembleWords = 'and ' + item
    concatenate_until_2.append(assembleWords)
concatenate_until = concatenate_until_1 + concatenate_until_2

# for 'since'
concatenate_since_1 = ['since then', 'after this', 'after that']
concatenate_since_2 = []
for item in concatenate_since_1:
    assembleWords = 'and ' + item
    concatenate_since_2.append(assembleWords)
concatenate_since = concatenate_since_1 + concatenate_since_2

"""
Section 2.2: template words for temporal phrases of layer 2
"""
# for direct negate of 'eventually' and 'once' operator
semantics_anytime = ['anytime', 'any moment', 'any time instant', 'any time point']
# for 'not until' and 'not since'
not_until_since_subject_type1 = ['the condition that']
not_until_since_subject_type2 = ['the following condition',
                                 'the subsequent condition']
not_until_since_predicate = ['be']
not_until_since_object = ['true']

"""
Section 2.3: template words for temporal phrases of layer 3-6
"""
tp_event_subject_type1 = copy.deepcopy(not_until_since_subject_type1)
tp_event_subject_type2 = copy.deepcopy(not_until_since_subject_type2)
tp_event_predicate = ['change',
                      'be detected to change',
                      'be observed to change',
                      'shift',
                      'be detected to shift',
                      'be observed to shift',
                      ]
tp_event_object_rise = ['from false to true']
tp_event_object_fall = ['from true to false']
