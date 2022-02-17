from corpus import template_words

# Translation template
# SE
# category = 0
# subcategory = 0, obj == value
Eng_SE_0_0 = {
    'subject': template_words.subject_value_single,

    'predicate_logic': template_words.predicate_equalValue_logic,

    'predicate_duration': template_words.predicate_equalValue_duration,

    'object': template_words.object_value_single
}
#
# subcategory = 1, not (obj == value)
Eng_SE_0_1 = {
    'subject': template_words.subject_value_single,

    'predicate_negative_logic': template_words.predicate_equalValue_logic,

    'object': template_words.object_value_single
}

# subcategory = 2, not rise (obj == value)
Eng_SE_0_2 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_equalValue_riseEvent,

    'object': template_words.object_value_single,

    'suffix_negative': template_words.predicate_event_happen
}

# subcategory = 3, not fall (obj == value)
Eng_SE_0_3 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_equalValue_fallEvent,

    'object': template_words.object_value_single,

    'suffix_negative': template_words.predicate_event_happen
}

# category 1
# subcategory = 0, obj >= value
Eng_SE_1_0 = {
    'subject': template_words.subject_value_single,

    'predicate_logic': template_words.predicate_atLeast_logic,

    'predicate_duration': template_words.predicate_atLeast_duration,

    'object': template_words.object_value_single
}

# subcategory = 1, obj > value
Eng_SE_1_1 = {
    'subject': template_words.subject_value_single,

    'predicate_logic': template_words.predicate_larger_logic,

    'predicate_duration': template_words.predicate_larger_duration,

    'object': template_words.object_value_single
}

# subcategory = 2, not (obj >= value)
Eng_SE_1_2 = {
    'subject': template_words.subject_value_single,

    'predicate_negative_logic': template_words.predicate_atLeast_logic,

    'predicate_positive_logic': template_words.predicate_smaller_logic,

    'predicate_positive_duration': template_words.predicate_smaller_duration,

    'object': template_words.object_value_single
}

# subcategory = 3, not (obj > value)
Eng_SE_1_3 = {
    'subject': template_words.subject_value_single,

    'predicate_negative_logic': template_words.predicate_larger_logic,

    'predicate_positive_logic': template_words.predicate_atMost_logic,

    'predicate_positive_duration': template_words.predicate_atMost_duration,

    'object': template_words.object_value_single
}

# subcategory = 4, not rise (obj >= value)
Eng_SE_1_4 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_atLeast_riseEvent,

    'object': template_words.object_value_single,

    'suffix_negative': template_words.predicate_event_happen
}

# subcategory = 5, not rise (obj > value)
Eng_SE_1_5 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_larger_riseEvent,

    'object': template_words.object_value_single,

    'suffix_negative': template_words.predicate_event_happen
}

# subcategory = 6, not fall (obj >= value)
Eng_SE_1_6 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_atLeast_fallEvent,

    'object': template_words.object_value_single,

    'suffix_negative': template_words.predicate_event_happen
}

# subcategory = 7, not fall (obj > value)
Eng_SE_1_7 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_larger_fallEvent,

    'object': template_words.object_value_single,

    'suffix_negative': template_words.predicate_event_happen
}

# category 2
# subcategory = 0, obj <= value
Eng_SE_2_0 = {
    'subject': template_words.subject_value_single,

    'predicate_logic': template_words.predicate_atMost_logic,

    'predicate_duration': template_words.predicate_atMost_duration,

    'object': template_words.object_value_single
}

# subcategory = 1, obj < value
Eng_SE_2_1 = {
    'subject': template_words.subject_value_single,

    'predicate_logic': template_words.predicate_smaller_logic,

    'predicate_duration': template_words.predicate_smaller_duration,

    'object': template_words.object_value_single
}

# subcategory = 2, not (obj <= value)
Eng_SE_2_2 = {
    'subject': template_words.subject_value_single,

    'predicate_negative_logic': template_words.predicate_atMost_logic,

    'predicate_positive_logic': template_words.predicate_larger_logic,

    'predicate_positive_duration': template_words.predicate_larger_duration,

    'object': template_words.object_value_single
}

# subcategory = 3, not (obj < value)
Eng_SE_2_3 = {
    'subject': template_words.subject_value_single,

    'predicate_negative_logic': template_words.predicate_smaller_logic,

    'predicate_positive_logic': template_words.predicate_atLeast_logic,

    'predicate_positive_duration': template_words.predicate_atLeast_duration,

    'object': template_words.object_value_single
}

# subcategory = 4, not rise (obj <= value) = not fall (obj > value)
Eng_SE_2_4 = Eng_SE_1_7

# subcategory = 5, not rise (obj < value) = not fall (obj >= value)
Eng_SE_2_5 = Eng_SE_1_6

# subcategory = 6, not fall (obj <= value) = not rise (obj > value)
Eng_SE_2_6 = Eng_SE_1_5

# subcategory = 7, not fall (obj < value) = not rise (obj >= value)
Eng_SE_2_7 = Eng_SE_1_4

# category 3
# subcategory = 0, obj >= value1 and obj <= value2
Eng_SE_3_0 = {
    'subject': template_words.subject_value_single,

    'predicate_logic': template_words.predicate_range_logic,

    'predicate_duration': template_words.predicate_range_duration,

    # object 1 starts
    # >=
    'object_1_adj_1': template_words.object_range_adj_atLeast,

    # value1
    'object_1_noun_1': ['value1'],

    # and
    'object_1_conj': ['and'],

    # <=
    'object_1_adj_2': template_words.object_range_adj_atMost,

    # value2
    'object_1_noun_2': ['value2'],
    # object 1 ends

    # object 2 starts
    'object_2_prep': template_words.object_range_prep_general + template_words.object_range_prep_bothClosed,

    # [value1, value2]
    'object_2_noun': template_words.object_range_interval_CC_math,
    # object 2 ends

    # object 3 starts
    # between
    'object_3_prep': ['between'],

    # value1 (closed) and value2 (closed)
    'object_3_noun': template_words.object_range_interval_CC_eng,
    # object 3 ends
}

# subcategory = 1, obj > value1 and obj <= value2
Eng_SE_3_1 = {
    'subject': template_words.subject_value_single,

    'predicate_logic': template_words.predicate_range_logic,

    'predicate_duration': template_words.predicate_range_duration,

    # object 1 starts
    # >
    'object_1_adj_1': template_words.object_range_adj_larger,

    # value1
    'object_1_noun_1': ['value1'],

    # and
    'object_1_conj': ['and'],

    # <=
    'object_1_adj_2': template_words.object_range_adj_atMost,

    # value2
    'object_1_noun_2': ['value2'],
    # object 1 ends

    # object 2 starts
    'object_2_prep': template_words.object_range_prep_general,

    # (value1, value2]
    'object_2_noun': template_words.object_range_interval_OC_math,
    # object 2 ends

    # object 3 starts
    # between
    'object_3_prep': ['between'],

    # value1 (open) and value2 (closed)
    'object_3_noun': template_words.object_range_interval_OC_eng,
    # object 3 ends
}

# subcategory = 2, obj >= value1 and obj < value2
Eng_SE_3_2 = {
    'subject': template_words.subject_value_single,

    'predicate_logic': template_words.predicate_range_logic,

    'predicate_duration': template_words.predicate_range_duration,

    # object 1 starts
    # >=
    'object_1_adj_1': template_words.object_range_adj_atLeast,

    # value1
    'object_1_noun_1': ['value1'],

    # and
    'object_1_conj': ['and'],

    # <
    'object_1_adj_2': template_words.object_range_adj_smaller,

    # value2
    'object_1_noun_2': ['value2'],
    # object 1 ends

    # object 2 starts
    'object_2_prep': template_words.object_range_prep_general,

    # [value1, value2)
    'object_2_noun': template_words.object_range_interval_CO_math,
    # object 2 ends

    # object 3 starts
    # between
    'object_3_prep': ['between'],

    # value1 (closed) and value2 (open)
    'object_3_noun': template_words.object_range_interval_CO_eng,
    # object 3 ends
}

# subcategory = 3, obj > value1 and obj < value2
Eng_SE_3_3 = {
    'subject': template_words.subject_value_single,

    'predicate_logic': template_words.predicate_range_logic,

    'predicate_duration': template_words.predicate_range_duration,

    # object 1 starts
    # >
    'object_1_adj_1': template_words.object_range_adj_larger,

    # value1
    'object_1_noun_1': ['value1'],

    # and
    'object_1_conj': ['and'],

    # <
    'object_1_adj_2': template_words.object_range_adj_smaller,

    # value2
    'object_1_noun_2': ['value2'],
    # object 1 ends

    # object 2 starts
    'object_2_prep': template_words.object_range_prep_general + template_words.object_range_prep_bothOpen,

    # (value1, value2)
    'object_2_noun': template_words.object_range_interval_OO_math,
    # object 2 ends

    # object 3 starts
    # between
    'object_3_prep': ['between'],

    # value1 (open) and value2 (open)
    'object_3_noun': template_words.object_range_interval_OO_eng,
    # object 3 ends
}

# subcategory = 4, not (obj >= value1 and obj <= value2)
Eng_SE_3_4 = {
    'subject': template_words.subject_value_single,

    'predicate_negative_logic': template_words.predicate_range_logic,

    # object 1 starts
    # >=
    'object_1_adj_1': template_words.object_range_adj_atLeast,

    # value1
    'object_1_noun_1': ['value1'],

    # and
    'object_1_conj': ['and'],

    # <=
    'object_1_adj_2': template_words.object_range_adj_atMost,

    # value2
    'object_1_noun_2': ['value2'],
    # object 1 ends

    # object 2 starts
    'object_2_prep': template_words.object_range_prep_general + template_words.object_range_prep_bothClosed,

    # [value1, value2]
    'object_2_noun': template_words.object_range_interval_CC_math,
    # object 2 ends

    # object 3 starts
    # between
    'object_3_prep': ['between'],

    # value1 (closed) and value2 (closed)
    'object_3_noun': template_words.object_range_interval_CC_eng,
    # object 3 ends

    ########################################################################

    'predicate_positive_logic': template_words.predicate_range_notInsideRange_logic,

    'predicate_positive_duration': template_words.predicate_range_notInsideRange_duration,

    # [value1, value2]
    'object_4_noun': template_words.object_range_interval_CC_math,

}

# subcategory = 5, not (obj > value1 and obj <= value2)
Eng_SE_3_5 = {
    'subject': template_words.subject_value_single,

    'predicate_negative_logic': template_words.predicate_range_logic,

    # object 1 starts
    # >
    'object_1_adj_1': template_words.object_range_adj_larger,

    # value1
    'object_1_noun_1': ['value1'],

    # and
    'object_1_conj': ['and'],

    # <=
    'object_1_adj_2': template_words.object_range_adj_atMost,

    # value2
    'object_1_noun_2': ['value2'],
    # object 1 ends

    # object 2 starts
    'object_2_prep': template_words.object_range_prep_general,

    # (value1, value2]
    'object_2_noun': template_words.object_range_interval_OC_math,
    # object 2 ends

    # object 3 starts
    # between
    'object_3_prep': ['between'],

    # value1 (open) and value2 (closed)
    'object_3_noun': template_words.object_range_interval_OC_eng,
    # object 3 ends

    ########################################################################

    'predicate_positive_logic': template_words.predicate_range_notInsideRange_logic,

    'predicate_positive_duration': template_words.predicate_range_notInsideRange_duration,

    # (value1, value2]
    'object_4_noun': template_words.object_range_interval_OC_math,

}

# subcategory = 6, not (obj >= value1 and obj < value2)
Eng_SE_3_6 = {
    'subject': template_words.subject_value_single,

    'predicate_negative_logic': template_words.predicate_range_logic,

    # object 1 starts
    # >=
    'object_1_adj_1': template_words.object_range_adj_atLeast,

    # value1
    'object_1_noun_1': ['value1'],

    # and
    'object_1_conj': ['and'],

    # <
    'object_1_adj_2': template_words.object_range_adj_smaller,

    # value2
    'object_1_noun_2': ['value2'],
    # object 1 ends

    # object 2 starts
    'object_2_prep': template_words.object_range_prep_general,

    # [value1, value2)
    'object_2_noun': template_words.object_range_interval_CO_math,
    # object 2 ends

    # object 3 starts
    # between
    'object_3_prep': ['between'],

    # value1 (closed) and value2 (open)
    'object_3_noun': template_words.object_range_interval_CO_eng,
    # object 3 ends

    ########################################################################

    'predicate_positive_logic': template_words.predicate_range_notInsideRange_logic,

    'predicate_positive_duration': template_words.predicate_range_notInsideRange_duration,

    # [value1, value2)
    'object_4_noun': template_words.object_range_interval_CO_math,

}

# subcategory = 7, not (obj > value1 and obj < value2)
Eng_SE_3_7 = {
    'subject': template_words.subject_value_single,

    'predicate_negative_logic': template_words.predicate_range_logic,

    # object 1 starts
    # >
    'object_1_adj_1': template_words.object_range_adj_larger,

    # value1
    'object_1_noun_1': ['value1'],

    # and
    'object_1_conj': ['and'],

    # <
    'object_1_adj_2': template_words.object_range_adj_smaller,

    # value2
    'object_1_noun_2': ['value2'],
    # object 1 ends

    # object 2 starts
    'object_2_prep': template_words.object_range_prep_general + template_words.object_range_prep_bothOpen,

    # (value1, value2)
    'object_2_noun': template_words.object_range_interval_OO_math,
    # object 2 ends

    # object 3 starts
    # between
    'object_3_prep': ['between'],

    # value1 (open) and value2 (open)
    'object_3_noun': template_words.object_range_interval_OO_eng,
    # object 3 ends

    ########################################################################

    'predicate_positive_logic': template_words.predicate_range_notInsideRange_logic,

    'predicate_positive_duration': template_words.predicate_range_notInsideRange_duration,

    # (value1, value2)
    'object_4_noun': template_words.object_range_interval_OO_math

}

# subcategory = 8, not rise (obj >= value1 and obj <= value2)
Eng_SE_3_8 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_range_riseEvent,

    'object': template_words.object_range_interval_CC_math,

    'suffix_negative': template_words.predicate_event_happen
}

# subcategory = 9, not rise (obj > value1 and obj <= value2)
Eng_SE_3_9 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_range_riseEvent,

    'object': template_words.object_range_interval_OC_math,

    'suffix_negative': template_words.predicate_event_happen
}

# subcategory = 10, not rise (obj >= value1 and obj < value2)
Eng_SE_3_10 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_range_riseEvent,

    'object': template_words.object_range_interval_CO_math,

    'suffix_negative': template_words.predicate_event_happen
}

# subcategory = 11, not rise (obj > value1 and obj < value2)
Eng_SE_3_11 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_range_riseEvent,

    'object': template_words.object_range_interval_OO_math,

    'suffix_negative': template_words.predicate_event_happen
}

# subcategory = 12, not fall (obj >= value1 and obj <= value2)
Eng_SE_3_12 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_range_fallEvent,

    'object': template_words.object_range_interval_CC_math,

    'suffix_negative': template_words.predicate_event_happen
}

# subcategory = 13, not fall (obj > value1 and obj <= value2)
Eng_SE_3_13 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_range_fallEvent,

    'object': template_words.object_range_interval_OC_math,

    'suffix_negative': template_words.predicate_event_happen
}

# subcategory = 14, not fall (obj >= value1 and obj < value2)
Eng_SE_3_14 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_range_fallEvent,

    'object': template_words.object_range_interval_CO_math,

    'suffix_negative': template_words.predicate_event_happen
}

# subcategory = 15, not fall (obj > value1 and obj < value2)
Eng_SE_3_15 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_range_fallEvent,

    'object': template_words.object_range_interval_OO_math,

    'suffix_negative': template_words.predicate_event_happen
}

# category 4
# subcategory = 0, obj == mode
Eng_SE_4_0 = {
    'subject': template_words.subject_mode_single,

    'predicate_logic': template_words.predicate_equalMode_logic,

    'predicate_duration': template_words.predicate_equalMode_duration,

    'object': template_words.object_mode_single
}

# subcategory = 1, not (obj == mode)
Eng_SE_4_1 = {
    'subject': template_words.subject_mode_single,

    'predicate_negative_logic': template_words.predicate_equalMode_logic,

    'object': template_words.object_mode_single
}

# subcategory = 2, not rise (obj == mode)
Eng_SE_4_2 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_mode_single,

    'predicate_action': template_words.predicate_equalMode_riseEvent,

    'object': template_words.object_mode_single,

    'suffix_negative': template_words.predicate_event_happen
}

# subcategory = 3, not fall (obj == mode)
Eng_SE_4_3 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_mode_single,

    'predicate_action': template_words.predicate_equalMode_fallEvent,

    'object': template_words.object_mode_single,

    'suffix_negative': template_words.predicate_event_happen
}

# Eng_SE_4_4 = {
#     'subject': ['substitution'],
#
#     'predicate_not': [
#         'does not happen',
#         'does not occur'
#     ],
#
#     'predicate_never': [
#         'never happens',
#         'never occurs'
#     ]
# }


# category 5
# subcategory = 0, obj == mode1 or obj == mode2
Eng_SE_5_0 = {
    'subject': template_words.subject_mode_single,

    'predicate_logic': template_words.predicate_equalModes_logic,

    'predicate_duration': template_words.predicate_equalModes_duration,

    'object': template_words.object_mode_double
}

# subcategory = 1, not (obj == mode1 or obj == mode2)
Eng_SE_5_1 = {
    'subject': template_words.subject_mode_single,

    'predicate_negative_logic': template_words.predicate_equalModes_logic,

    'predicate_positive_logic': template_words.predicate_equalModes_logic,

    'predicate_positive_duration': template_words.predicate_equalModes_duration,

    'object': template_words.object_mode_double,

    'object_special': template_words.object_mode_double_special
}

# subcategory = 2, not rise (obj == mode1 or obj == mode2)
Eng_SE_5_2 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_mode_single,

    'predicate_action': template_words.predicate_equalModes_riseEvent,

    'object': template_words.object_mode_double,

    'suffix_negative': template_words.predicate_event_happen
}

# subcategory = 3, not fall (obj == mode1 or obj == mode2)
Eng_SE_5_3 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_mode_single,

    'predicate_action': template_words.predicate_equalModes_fallEvent,

    'object': template_words.object_mode_double,

    'suffix_negative': template_words.predicate_event_happen
}

# Eng_SE_5_4 = {
#     'subject': [
#         '{substitution1, substitution2}',
#         'none of substitution1 and substitution2',
#         'neither substitution1 nor substitution2'
#     ],
#
#     'predicate_not': [
#         'does not happen',
#         'does not occur'
#     ],
#
#     'predicate_never': [
#         'never happens',
#         'never occurs'
#     ],
#
#     'predicate_assertive': [
#         'happen',
#         'occur',
#         'happens',
#         'occurs'
#     ]
# }

Eng_SE = [[Eng_SE_0_0, Eng_SE_0_1, Eng_SE_0_2, Eng_SE_0_3],
          [Eng_SE_1_0, Eng_SE_1_1, Eng_SE_1_2, Eng_SE_1_3, Eng_SE_1_4, Eng_SE_1_5, Eng_SE_1_6, Eng_SE_1_7],
          [Eng_SE_2_0, Eng_SE_2_1, Eng_SE_2_2, Eng_SE_2_3, Eng_SE_2_4, Eng_SE_2_5, Eng_SE_2_6, Eng_SE_2_7],
          [Eng_SE_3_0, Eng_SE_3_1, Eng_SE_3_2, Eng_SE_3_3, Eng_SE_3_4, Eng_SE_3_5, Eng_SE_3_6, Eng_SE_3_7,
           Eng_SE_3_8, Eng_SE_3_9, Eng_SE_3_10, Eng_SE_3_11, Eng_SE_3_12, Eng_SE_3_13, Eng_SE_3_14, Eng_SE_3_15],
          [Eng_SE_4_0, Eng_SE_4_1, Eng_SE_4_2, Eng_SE_4_3],
          [Eng_SE_5_0, Eng_SE_5_1, Eng_SE_5_2, Eng_SE_5_3]
          ]


# ERE
# category = 0
# subcategory = 0, rise (obj == value)
Eng_ERE_0_0 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_equalValue_riseEvent,

    'object': template_words.object_value_single,

    'suffix_positive': template_words.predicate_event_happen
}

# subcategory = 1, fall (obj == value)
Eng_ERE_0_1 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_equalValue_fallEvent,

    'object': template_words.object_value_single,

    'suffix_positive': template_words.predicate_event_happen
}

# category = 1
# subcategory = 0, rise (obj >= value)
Eng_ERE_1_0 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_atLeast_riseEvent,

    'object': template_words.object_value_single,

    'suffix_positive': template_words.predicate_event_happen
}

# category = 1
# subcategory = 1, rise (obj > value)
Eng_ERE_1_1 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_larger_riseEvent,

    'object': template_words.object_value_single,

    'suffix_positive': template_words.predicate_event_happen
}

# subcategory = 2, fall (obj >= value)
Eng_ERE_1_2 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_atLeast_fallEvent,

    'object': template_words.object_value_single,

    'suffix_positive': template_words.predicate_event_happen
}

# subcategory = 3, fall (obj > value)
Eng_ERE_1_3 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_larger_fallEvent,

    'object': template_words.object_value_single,

    'suffix_positive': template_words.predicate_event_happen
}

# category = 2
# subcategory = 0, rise (obj <= value) = fall (obj > value)
Eng_ERE_2_0 = Eng_ERE_1_3

# subcategory = 1, rise (obj < value) = fall (obj >= value)
Eng_ERE_2_1 = Eng_ERE_1_2

# subcategory = 2, fall (obj <= value) = rise (obj > value)
Eng_ERE_2_2 = Eng_ERE_1_1

# subcategory = 3, fall (obj < value) = rise (obj >= value)
Eng_ERE_2_3 = Eng_ERE_1_0

# category = 3
# subcategory = 0, rise (obj >= value1 and obj <= value2)
Eng_ERE_3_0 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_range_riseEvent,

    'object': template_words.object_range_interval_CC_math,

    'suffix_positive': template_words.predicate_event_happen
}

# subcategory = 1, rise (obj > value1 and obj <= value2)
Eng_ERE_3_1 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_range_riseEvent,

    'object': template_words.object_range_interval_OC_math,

    'suffix_positive': template_words.predicate_event_happen
}

# subcategory = 2, rise (obj >= value1 and obj < value2)
Eng_ERE_3_2 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_range_riseEvent,

    'object': template_words.object_range_interval_CO_math,

    'suffix_positive': template_words.predicate_event_happen
}

# subcategory = 3, rise (obj > value1 and obj < value2)
Eng_ERE_3_3 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_range_riseEvent,

    'object': template_words.object_range_interval_OO_math,

    'suffix_positive': template_words.predicate_event_happen
}

# subcategory = 4, fall (obj >= value1 and obj <= value2)
Eng_ERE_3_4 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_range_fallEvent,

    'object': template_words.object_range_interval_CC_math,

    'suffix_positive': template_words.predicate_event_happen
}

# subcategory = 5, fall (obj > value1 and obj <= value2)
Eng_ERE_3_5 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_range_fallEvent,

    'object': template_words.object_range_interval_OC_math,

    'suffix_positive': template_words.predicate_event_happen
}

# subcategory = 6, fall (obj >= value1 and obj < value2)
Eng_ERE_3_6 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_range_fallEvent,

    'object': template_words.object_range_interval_CO_math,

    'suffix_positive': template_words.predicate_event_happen
}

# subcategory = 7, fall (obj > value1 and obj < value2)
Eng_ERE_3_7 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_value_single,

    'predicate_action': template_words.predicate_range_fallEvent,

    'object': template_words.object_range_interval_OO_math,

    'suffix_positive': template_words.predicate_event_happen
}

# category = 4
# subcategory = 0, rise (obj == mode)
Eng_ERE_4_0 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_mode_single,

    'predicate_action': template_words.predicate_equalMode_riseEvent,

    'object': template_words.object_mode_single,

    'suffix_positive': template_words.predicate_event_happen
}

# subcategory = 1, fall (obj == mode)
Eng_ERE_4_1 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_mode_single,

    'predicate_action': template_words.predicate_equalMode_fallEvent,

    'object': template_words.object_mode_single,

    'suffix_positive': template_words.predicate_event_happen
}

# category = 5
# subcategory = 0, rise (obj == mode1 or obj == mode2)
Eng_ERE_5_0 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_mode_single,

    'predicate_action': template_words.predicate_equalModes_riseEvent,

    'object': template_words.object_mode_double,

    'suffix_positive': template_words.predicate_event_happen
}

# subcategory = 1, fall (obj == mode1 or obj == mode2)
Eng_ERE_5_1 = {
    'prefix': template_words.prefix_event,

    'subject': template_words.subject_mode_single,

    'predicate_action': template_words.predicate_equalModes_fallEvent,

    'object': template_words.object_mode_double,

    'suffix_positive': template_words.predicate_event_happen
}
#
Eng_ERE = [[Eng_ERE_0_0, Eng_ERE_0_1],
           [Eng_ERE_1_0, Eng_ERE_1_1, Eng_ERE_1_2, Eng_ERE_1_3],
           [Eng_ERE_2_0, Eng_ERE_2_1, Eng_ERE_2_2, Eng_ERE_2_3],
           [Eng_ERE_3_0, Eng_ERE_3_1, Eng_ERE_3_2, Eng_ERE_3_3, Eng_ERE_3_4, Eng_ERE_3_5, Eng_ERE_3_6, Eng_ERE_3_7],
           [Eng_ERE_4_0, Eng_ERE_4_1],
           [Eng_ERE_5_0, Eng_ERE_5_1],
           ]



