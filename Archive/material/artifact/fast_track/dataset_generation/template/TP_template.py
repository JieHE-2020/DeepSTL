from corpus import template_words
from corpus import adverbial_modifiers

# Translation template
# TP
# category = 0 => eventually
# subcategory = 0, eventually (SP_expr)
Eng_TP_0_0 = {
    'adverb': adverbial_modifiers.adv_eventually,

    'temporal_phrase': adverbial_modifiers.temporal_phrase_eventually_end,

    'semantics_sometime': template_words.semantics_sometime,

    # only used for direct negation
    'semantics_anytime': template_words.semantics_anytime,

    'clause': {
        'subject': template_words.there_be_subject,

        'predicate': template_words.there_be_predicate,

        'object': template_words.there_be_object
    },

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# subcategory = 1, eventually [0:t] (SP_expr)
Eng_TP_0_1 = {
    'adverb': adverbial_modifiers.adv_eventually,

    'temporal_phrase': adverbial_modifiers.temporal_phrase_eventually_0t,

    'semantics_sometime': template_words.semantics_sometime,

    # only used for direct negation
    'semantics_anytime': template_words.semantics_anytime,

    'clause': {
        'subject': template_words.there_be_subject,

        'predicate': template_words.there_be_predicate,

        'object': template_words.there_be_object
    },

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# subcategory = 2, eventually [a:b] (SP_expr)  (0 < a < b)
Eng_TP_0_2 = {
    'adverb': adverbial_modifiers.adv_eventually,

    'temporal_phrase': adverbial_modifiers.temporal_phrase_eventually_ab,

    'semantics_sometime': template_words.semantics_sometime,

    # only used for direct negation
    'semantics_anytime': template_words.semantics_anytime,

    'clause': {
        'subject': template_words.there_be_subject,

        'predicate': template_words.there_be_predicate,

        'object': template_words.there_be_object
    },

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# category = 1 => always
# subcategory = 0, always (CE_expr)
Eng_TP_1_0 = {
    'adverb_refine': adverbial_modifiers.adv_always_refine,

    'adverb_assemble': adverbial_modifiers.adv_always_assemble,

    'adverbial_phrase_assemble': adverbial_modifiers.adv_phrase_always_assemble,

    'temporal_phrase': adverbial_modifiers.temporal_phrase_always_end,

    'temporal_phrase_each_time': adverbial_modifiers.temporal_phrase_always_end_each_time,

    'clause_general': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_general,

        'object': template_words.clause_object_general
    },

    'clause_value': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_value,

        'object': template_words.clause_object_value
    },

    'clause_range': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_range,

        'object': template_words.clause_object_range
    },

    'clause_mode': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_mode,

        'object': template_words.clause_object_mode
    },

    'special_clause': {
        'conjunction': template_words.special_clause_conjunction,

        'subject': template_words.special_clause_subject,

        'predicate': template_words.special_clause_predicate
    },

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# subcategory = 1, always [0:t] (CE_expr)
Eng_TP_1_1 = {
    'adverb_refine': adverbial_modifiers.adv_always_refine,

    'adverb_assemble': adverbial_modifiers.adv_always_assemble,

    'adverbial_phrase_assemble': adverbial_modifiers.adv_phrase_always_assemble,

    'temporal_phrase': adverbial_modifiers.temporal_phrase_always_0t,

    'temporal_phrase_each_time': adverbial_modifiers.temporal_phrase_always_0t_each_time,

    'clause_general': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_general,

        'object': template_words.clause_object_general
    },

    'clause_value': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_value,

        'object': template_words.clause_object_value
    },

    'clause_range': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_range,

        'object': template_words.clause_object_range
    },

    'clause_mode': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_mode,

        'object': template_words.clause_object_mode
    },

    'special_clause': {
        'conjunction': template_words.special_clause_conjunction,

        'subject': template_words.special_clause_subject,

        'predicate': template_words.special_clause_predicate
    },

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# subcategory = 2, always [a:b] (CE_expr)  (0 < a < b)
Eng_TP_1_2 = {
    'adverb_refine': adverbial_modifiers.adv_always_refine,

    'adverb_assemble': adverbial_modifiers.adv_always_assemble,

    'adverbial_phrase_assemble': adverbial_modifiers.adv_phrase_always_assemble,

    'temporal_phrase': adverbial_modifiers.temporal_phrase_always_ab,

    'temporal_phrase_each_time': adverbial_modifiers.temporal_phrase_always_ab_each_time,

    'clause_general': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_general,

        'object': template_words.clause_object_general
    },

    'clause_value': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_value,

        'object': template_words.clause_object_value
    },

    'clause_range': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_range,

        'object': template_words.clause_object_range
    },

    'clause_mode': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_mode,

        'object': template_words.clause_object_mode
    },

    'special_clause': {
        'conjunction': template_words.special_clause_conjunction,

        'subject': template_words.special_clause_subject,

        'predicate': template_words.special_clause_predicate
    },

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# category = 2 => once
# subcategory = 0, once (SP_expr)
Eng_TP_2_0 = {
    'adverb': adverbial_modifiers.adv_once,

    'temporal_phrase': adverbial_modifiers.temporal_phrase_once_start,

    'semantics_sometime': template_words.semantics_sometime,

    # only used for direct negation
    'semantics_anytime': template_words.semantics_anytime,

    'clause': {
        'subject': template_words.there_be_subject,

        'predicate': template_words.there_be_predicate,

        'object': template_words.there_be_object
    },

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# subcategory = 1, once[0:t] (SP_expr)
Eng_TP_2_1 = {
    'adverb': adverbial_modifiers.adv_once,

    'temporal_phrase': adverbial_modifiers.temporal_phrase_once_0t,

    'semantics_sometime': template_words.semantics_sometime,

    # only used for direct negation
    'semantics_anytime': template_words.semantics_anytime,

    'clause': {
        'subject': template_words.there_be_subject,

        'predicate': template_words.there_be_predicate,

        'object': template_words.there_be_object
    },

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# subcategory = 2, once [a:b] (SP_expr)  (0 < a < b)
Eng_TP_2_2 = {
    'adverb': adverbial_modifiers.adv_once,

    'temporal_phrase': adverbial_modifiers.temporal_phrase_once_ab,

    'semantics_sometime': template_words.semantics_sometime,

    # only used for direct negation
    'semantics_anytime': template_words.semantics_anytime,

    'clause': {
        'subject': template_words.there_be_subject,

        'predicate': template_words.there_be_predicate,

        'object': template_words.there_be_object
    },

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# category = 3 => historically
# subcategory = 0, historically (CE_expr)
Eng_TP_3_0 = {
    'adverb_refine': adverbial_modifiers.adv_historically_refine,

    'adverb_assemble': adverbial_modifiers.adv_historically_assemble,

    'adverbial_phrase_assemble': adverbial_modifiers.adv_phrase_historically_assemble,

    'temporal_phrase': adverbial_modifiers.temporal_phrase_historically_start,

    'clause_general': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_general,

        'object': template_words.clause_object_general
    },

    'clause_value': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_value,

        'object': template_words.clause_object_value
    },

    'clause_range': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_range,

        'object': template_words.clause_object_range
    },

    'clause_mode': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_mode,

        'object': template_words.clause_object_mode
    },

    'special_clause': {
        'conjunction': template_words.special_clause_conjunction,

        'subject': template_words.special_clause_subject,

        'predicate': template_words.special_clause_predicate
    },

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# subcategory = 1, historically [0:t] (CE_expr)
Eng_TP_3_1 = {
    'adverb_refine': adverbial_modifiers.adv_historically_refine,

    'adverb_assemble': adverbial_modifiers.adv_historically_assemble,

    'adverbial_phrase_assemble': adverbial_modifiers.adv_phrase_historically_assemble,

    'temporal_phrase': adverbial_modifiers.temporal_phrase_historically_0t,

    'clause_general': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_general,

        'object': template_words.clause_object_general
    },

    'clause_value': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_value,

        'object': template_words.clause_object_value
    },

    'clause_range': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_range,

        'object': template_words.clause_object_range
    },

    'clause_mode': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_mode,

        'object': template_words.clause_object_mode
    },

    'special_clause': {
        'conjunction': template_words.special_clause_conjunction,

        'subject': template_words.special_clause_subject,

        'predicate': template_words.special_clause_predicate
    },

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# subcategory = 2, historically [a:b] (CE_expr)  (0 < a < b)
Eng_TP_3_2 = {
    'adverb_refine': adverbial_modifiers.adv_historically_refine,

    'adverb_assemble': adverbial_modifiers.adv_historically_assemble,

    'adverbial_phrase_assemble': adverbial_modifiers.adv_phrase_historically_assemble,

    'temporal_phrase': adverbial_modifiers.temporal_phrase_historically_ab,

    'clause_general': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_general,

        'object': template_words.clause_object_general
    },

    'clause_value': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_value,

        'object': template_words.clause_object_value
    },

    'clause_range': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_range,

        'object': template_words.clause_object_range
    },

    'clause_mode': {
        'conjunction': template_words.clause_conjunction,

        'predicate': template_words.clause_predicate_mode,

        'object': template_words.clause_object_mode
    },

    'special_clause': {
        'conjunction': template_words.special_clause_conjunction,

        'subject': template_words.special_clause_subject,

        'predicate': template_words.special_clause_predicate
    },

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# category = 4 => until
# subcategory = 0, (SP_expr_1) until (SP_expr_2)
Eng_TP_4_0 = {
    'attributive_clause': {
        'subject': template_words.attributive_clause_subject,

        'predicate_se': template_words.attributive_clause_predicate_se,

        'predicate_ere': template_words.attributive_clause_predicate_ere,

        'temporal_adverbial_part_1': template_words.attributive_clause_temporal_adverbial_part_1
    },

    'concatenation': template_words.concatenate_until,

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# subcategory = 1, (SP_expr_1) until [0:t] (SP_expr_2)
Eng_TP_4_1 = {
    'attributive_clause': {
        'subject': template_words.attributive_clause_subject,

        'predicate_se': template_words.attributive_clause_predicate_se,

        'predicate_ere': template_words.attributive_clause_predicate_ere,

        'temporal_adverbial_part_1': template_words.attributive_clause_temporal_adverbial_part_1
    },

    'concatenation': template_words.concatenate_until,

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# subcategory = 2, (SP_expr_1) until [a:b] (SP_expr_2)  (0 < a < b)
Eng_TP_4_2 = {
    'attributive_clause': {
        'subject': template_words.attributive_clause_subject,

        'predicate_se': template_words.attributive_clause_predicate_se,

        'predicate_ere': template_words.attributive_clause_predicate_ere,

        'temporal_adverbial_part_1': template_words.attributive_clause_temporal_adverbial_part_1
    },

    'concatenation': template_words.concatenate_until,

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# category = 5 => since
# subcategory = 0, (SP_expr_1) since (SP_expr_2)
Eng_TP_5_0 = {
    'attributive_clause': {
        'subject': template_words.attributive_clause_subject,

        'predicate_se': template_words.attributive_clause_predicate_se,

        'predicate_ere': template_words.attributive_clause_predicate_ere,

        'temporal_adverbial_part_1': template_words.attributive_clause_temporal_adverbial_part_1
    },

    'concatenation': template_words.concatenate_since,

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# subcategory = 1, (SP_expr_1) since [0:t] (SP_expr_2)
Eng_TP_5_1 = {
    'attributive_clause': {
        'subject': template_words.attributive_clause_subject,

        'predicate_se': template_words.attributive_clause_predicate_se,

        'predicate_ere': template_words.attributive_clause_predicate_ere,

        'temporal_adverbial_part_1': template_words.attributive_clause_temporal_adverbial_part_1
    },

    'concatenation': template_words.concatenate_since,

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

# subcategory = 2, (SP_expr_1) since [a:b] (SP_expr_2)  (0 < a < b)
Eng_TP_5_2 = {
    'attributive_clause': {
        'subject': template_words.attributive_clause_subject,

        'predicate_se': template_words.attributive_clause_predicate_se,

        'predicate_ere': template_words.attributive_clause_predicate_ere,

        'temporal_adverbial_part_1': template_words.attributive_clause_temporal_adverbial_part_1
    },

    'concatenation': template_words.concatenate_since,

    'negation': {
        'subject_with_appositive': template_words.not_until_since_subject_type1,

        'subject_without_appositive': template_words.not_until_since_subject_type2,

        'predicate': template_words.not_until_since_predicate,

        'object': template_words.not_until_since_object
    },

    'event_related': {
        'subject_with_appositive': template_words.tp_event_subject_type1,

        'subject_without_appositive': template_words.tp_event_subject_type2,

        'predicate': template_words.tp_event_predicate,

        'object_rise_related': template_words.tp_event_object_rise,

        'object_fall_related': template_words.tp_event_object_fall
    }
}

Eng_TP = [[Eng_TP_0_0, Eng_TP_0_1, Eng_TP_0_2],
          [Eng_TP_1_0, Eng_TP_1_1, Eng_TP_1_2],
          [Eng_TP_2_0, Eng_TP_2_1, Eng_TP_2_2],
          [Eng_TP_3_0, Eng_TP_3_1, Eng_TP_3_2],
          [Eng_TP_4_0, Eng_TP_4_1, Eng_TP_4_2],
          [Eng_TP_5_0, Eng_TP_5_1, Eng_TP_5_2]
          ]
