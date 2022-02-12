

class PreCmdHistorically:
    def __init__(self, adv):
        self.adverb = adv
        # A. tense: present
        # I. before_imply
        # 1. main-type1
        # 1.1. main
        self.present_before_imply_main_type1_pos_cmd = [
            {'simple_present': ['singular', self.adverb]},
            {'simple_past': ['singular', self.adverb]},
            {'present_perfect': ['singular', self.adverb]},
            {'present_perfect_continuous': ['singular', self.adverb]}
        ]

        self.present_before_imply_main_type1_neg_cmd = [
            {'simple_present': ['singular_not_without_abbreviation', self.adverb,
                                'singular_not_with_abbreviation',
                                'singular_never'
                                ]},
            {'simple_past': ['singular_not_without_abbreviation', self.adverb,
                             'singular_not_with_abbreviation',
                             'singular_never'
                             ]},
            {'present_perfect': ['singular_not_without_abbreviation', self.adverb,
                                 'singular_not_with_abbreviation',
                                 'singular_never'
                                 ]}
        ]

        self.present_before_imply_main_type1_cmd_dict = {'positive': self.present_before_imply_main_type1_pos_cmd,
                                                         'negative': self.present_before_imply_main_type1_neg_cmd
                                                         }
        # 1.2. appositive
        self.present_before_imply_main_type1_appositive_cmd = [{'simple_present': ['singular']},
                                                               {'simple_past': ['singular']}]
        self.present_before_imply_main_type1_appositive_cmd_dict \
            = {'positive': self.present_before_imply_main_type1_appositive_cmd}

        # 2. main-type2
        # 2.1.1. main-part
        self.present_before_imply_main_type2_main_part_pos_cmd = [
            {'simple_present': ['singular']}
        ]

        self.present_before_imply_main_type2_main_part_neg_cmd = [
            {'simple_present': ['singular_not_without_abbreviation',
                                'singular_not_with_abbreviation'
                                ]}
        ]

        self.present_before_imply_main_type2_main_part_cmd_dict = \
            {'positive': self.present_before_imply_main_type2_main_part_pos_cmd,
             'negative': self.present_before_imply_main_type2_main_part_neg_cmd
             }

        # 2.1.2. appositive
        self.present_before_imply_main_type2_main_part_appositive_cmd = [{'simple_present': ['singular']}]
        self.present_before_imply_main_type2_main_part_appositive_cmd_dict \
            = {'positive': self.present_before_imply_main_type2_main_part_appositive_cmd}

        # 2.2. clause-part
        self.present_before_imply_main_type2_clause_part_cmd = self.present_before_imply_main_type1_pos_cmd
        self.present_before_imply_main_type2_clause_part_cmd_dict \
            = {'positive': self.present_before_imply_main_type2_clause_part_cmd}

        # II. after_imply
        # 1. main-type1
        # 1.1. main
        self.present_after_imply_main_type1_pos_cmd = [
            {'simple_present': ['singular', self.adverb]},
            {'simple_past': ['singular', self.adverb]},
            {'present_perfect': ['singular', self.adverb]},
            {'present_perfect_continuous': ['singular', self.adverb]},
            {'simple_future': ['will', self.adverb]},
            {'future_perfect': ['will_have_done', self.adverb]},
            {'future_perfect_continuous': ['will_have_been_doing', self.adverb]},
            {'modal': ['should', self.adverb,
                       'ought_to', self.adverb,
                       'must', self.adverb,
                       'shall', self.adverb,
                       'present_singular_have_to', self.adverb,
                       'future_have_to', self.adverb,
                       'present_singular_need_to', self.adverb]
             }
        ]

        self.present_after_imply_main_type1_neg_cmd = [
            {'simple_present': ['singular_not_without_abbreviation', self.adverb,
                                'singular_not_with_abbreviation',
                                'singular_never'
                                ]},
            {'simple_past': ['singular_not_without_abbreviation', self.adverb,
                             'singular_not_with_abbreviation',
                             'singular_never'
                             ]},
            {'present_perfect': ['singular_not_without_abbreviation', self.adverb,
                                 'singular_not_with_abbreviation',
                                 'singular_never'
                                 ]},
            {'simple_future': ['will_not_without_abbreviation', self.adverb,
                               'will_not_with_abbreviation',
                               'will_never'
                               ]},
            {'future_perfect': ['will_not_have_without_abbreviation', self.adverb,
                                'will_not_have_with_abbreviation',
                                'will_never_have'
                                ]},
            {'modal': ['should_not_without_abbreviation', self.adverb,
                       'should_not_with_abbreviation',
                       'should_never',
                       'ought_not_to_without_abbreviation',
                       'ought_not_to_with_abbreviation',
                       'ought_never_to',
                       'must_not_without_abbreviation', self.adverb,
                       'must_not_with_abbreviation',
                       'must_never',
                       'shall_not_without_abbreviation', self.adverb,
                       'shall_not_with_abbreviation',
                       'shall_never'
                       ]}
        ]

        self.present_after_imply_main_type1_cmd_dict = {'positive': self.present_after_imply_main_type1_pos_cmd,
                                                        'negative': self.present_after_imply_main_type1_neg_cmd
                                                        }
        # 1.2. appositive
        self.present_after_imply_main_type1_appositive_cmd = [{'simple_present': ['singular']},
                                                              {'simple_past': ['singular']}]
        self.present_after_imply_main_type1_appositive_cmd_dict \
            = {'positive': self.present_after_imply_main_type1_appositive_cmd}

        # 2. main-type2
        # 2.1.1. main-part
        self.present_after_imply_main_type2_main_part_pos_cmd = [
            {'simple_present': ['singular']},
            {'simple_future': ['will']},
            {'modal': ['should',
                       'ought_to',
                       'must',
                       'shall',
                       'present_singular_have_to',
                       'future_have_to',
                       'present_singular_need_to']
             }
        ]

        self.present_after_imply_main_type2_main_part_neg_cmd = [
            {'simple_present': ['singular_not_without_abbreviation',
                                'singular_not_with_abbreviation',
                                'singular_never'
                                ]},
            {'simple_future': ['will_not_without_abbreviation',
                               'will_not_with_abbreviation',
                               'will_never'
                               ]},
            {'modal': ['should_not_without_abbreviation',
                       'should_not_with_abbreviation',
                       'should_never',
                       'ought_not_to_without_abbreviation',
                       'ought_not_to_with_abbreviation',
                       'ought_never_to',
                       'must_not_without_abbreviation',
                       'must_not_with_abbreviation',
                       'must_never',
                       'shall_not_without_abbreviation',
                       'shall_not_with_abbreviation',
                       'shall_never'
                       ]}
        ]

        self.present_after_imply_main_type2_main_part_cmd_dict = \
            {'positive': self.present_after_imply_main_type2_main_part_pos_cmd,
             'negative': self.present_after_imply_main_type2_main_part_neg_cmd
             }

        # 2.1.2. appositive
        self.present_after_imply_main_type2_main_part_appositive_cmd = [{'simple_present': ['singular']}]
        self.present_after_imply_main_type2_main_part_appositive_cmd_dict \
            = {'positive': self.present_after_imply_main_type2_main_part_appositive_cmd}

        # 2.2. clause-part
        self.present_after_imply_main_type2_clause_part_cmd = self.present_after_imply_main_type1_pos_cmd
        self.present_after_imply_main_type2_clause_part_cmd_dict \
            = {'positive': self.present_after_imply_main_type2_clause_part_cmd}

        ################################################################################################################
        # B. tense: future
        # I. before_imply
        # 1. main-type1
        # 1.1. main
        self.future_before_imply_main_type1_pos_cmd = [
            {'simple_present': ['singular', self.adverb]},
            {'present_perfect': ['singular', self.adverb]},
            {'present_perfect_continuous': ['singular', self.adverb]},
            {'simple_future': ['will', self.adverb]},
            {'future_perfect': ['will_have_done', self.adverb]},
            {'future_perfect_continuous': ['will_have_been_doing', self.adverb]}
        ]

        self.future_before_imply_main_type1_neg_cmd = [
            {'simple_present': ['singular_not_without_abbreviation', self.adverb,
                                'singular_not_with_abbreviation',
                                'singular_never'
                                ]},
            {'present_perfect': ['singular_not_without_abbreviation', self.adverb,
                                 'singular_not_with_abbreviation',
                                 'singular_never'
                                 ]},
            {'simple_future': ['will_not_without_abbreviation', self.adverb,
                               'will_not_with_abbreviation',
                               'will_never'
                               ]},
            {'future_perfect': ['will_not_have_without_abbreviation', self.adverb,
                                'will_not_have_with_abbreviation',
                                'will_never_have'
                                ]}
        ]

        self.future_before_imply_main_type1_cmd_dict = {'positive': self.future_before_imply_main_type1_pos_cmd,
                                                        'negative': self.future_before_imply_main_type1_neg_cmd
                                                        }
        # 1.2. appositive
        self.future_before_imply_main_type1_appositive_cmd = [{'simple_present': ['singular']}]
        self.future_before_imply_main_type1_appositive_cmd_dict \
            = {'positive': self.future_before_imply_main_type1_appositive_cmd}

        # 2. main-type2
        # 2.1.1. main-part
        self.future_before_imply_main_type2_main_part_pos_cmd = [
            {'simple_present': ['singular']},
            {'simple_future': ['will']}
        ]

        self.future_before_imply_main_type2_main_part_neg_cmd = [
            {'simple_present': ['singular_not_without_abbreviation',
                                'singular_not_with_abbreviation'
                                ]},
            {'simple_future': ['will_not_without_abbreviation',
                               'will_not_with_abbreviation'
                               ]}
        ]

        self.future_before_imply_main_type2_main_part_cmd_dict = \
            {'positive': self.future_before_imply_main_type2_main_part_pos_cmd,
             'negative': self.future_before_imply_main_type2_main_part_neg_cmd
             }

        # 2.1.2. appositive
        self.future_before_imply_main_type2_main_part_appositive_cmd = [{'simple_present': ['singular']}]
        self.future_before_imply_main_type2_main_part_appositive_cmd_dict \
            = {'positive': self.future_before_imply_main_type2_main_part_appositive_cmd}

        # 2.2. clause-part
        self.future_before_imply_main_type2_clause_part_cmd = self.future_before_imply_main_type1_pos_cmd
        self.future_before_imply_main_type2_clause_part_cmd_dict \
            = {'positive': self.future_before_imply_main_type2_clause_part_cmd}

        # II. after_imply
        # 1. main-type1
        # 1.1. main
        self.future_after_imply_main_type1_pos_cmd = [
            {'simple_present': ['singular', self.adverb]},
            {'present_perfect': ['singular', self.adverb]},
            {'present_perfect_continuous': ['singular', self.adverb]},
            {'simple_future': ['will', self.adverb]},
            {'future_perfect': ['will_have_done', self.adverb]},
            {'future_perfect_continuous': ['will_have_been_doing', self.adverb]},
            {'modal': ['should', self.adverb,
                       'ought_to', self.adverb,
                       'must', self.adverb,
                       'shall', self.adverb,
                       'present_singular_have_to', self.adverb,
                       'future_have_to', self.adverb,
                       'present_singular_need_to', self.adverb]
             }
        ]

        self.future_after_imply_main_type1_neg_cmd = [
            {'simple_present': ['singular_not_without_abbreviation', self.adverb,
                                'singular_not_with_abbreviation',
                                'singular_never'
                                ]},
            {'present_perfect': ['singular_not_without_abbreviation', self.adverb,
                                 'singular_not_with_abbreviation',
                                 'singular_never'
                                 ]},
            {'simple_future': ['will_not_without_abbreviation', self.adverb,
                               'will_not_with_abbreviation',
                               'will_never'
                               ]},
            {'future_perfect': ['will_not_have_without_abbreviation', self.adverb,
                                'will_not_have_with_abbreviation',
                                'will_never_have'
                                ]},
            {'modal': ['should_not_without_abbreviation', self.adverb,
                       'should_not_with_abbreviation',
                       'should_never',
                       'ought_not_to_without_abbreviation',
                       'ought_not_to_with_abbreviation',
                       'ought_never_to',
                       'must_not_without_abbreviation', self.adverb,
                       'must_not_with_abbreviation',
                       'must_never',
                       'shall_not_without_abbreviation', self.adverb,
                       'shall_not_with_abbreviation',
                       'shall_never'
                       ]}
        ]

        self.future_after_imply_main_type1_cmd_dict = {'positive': self.future_after_imply_main_type1_pos_cmd,
                                                       'negative': self.future_after_imply_main_type1_neg_cmd
                                                       }
        # 1.2. appositive
        self.future_after_imply_main_type1_appositive_cmd = [{'simple_present': ['singular']}]
        self.future_after_imply_main_type1_appositive_cmd_dict \
            = {'positive': self.future_after_imply_main_type1_appositive_cmd}

        # 2. main-type2
        # 2.1.1. main-part
        self.future_after_imply_main_type2_main_part_pos_cmd = [
            {'simple_present': ['singular']},
            {'simple_future': ['will']},
            {'modal': ['should',
                       'ought_to',
                       'must',
                       'shall',
                       'present_singular_have_to',
                       'future_have_to',
                       'present_singular_need_to']
             }
        ]

        self.future_after_imply_main_type2_main_part_neg_cmd = [
            {'simple_present': ['singular_not_without_abbreviation',
                                'singular_not_with_abbreviation',
                                'singular_never'
                                ]},
            {'simple_future': ['will_not_without_abbreviation',
                               'will_not_with_abbreviation',
                               'will_never'
                               ]},
            {'modal': ['should_not_without_abbreviation',
                       'should_not_with_abbreviation',
                       'should_never',
                       'ought_not_to_without_abbreviation',
                       'ought_not_to_with_abbreviation',
                       'ought_never_to',
                       'must_not_without_abbreviation',
                       'must_not_with_abbreviation',
                       'must_never',
                       'shall_not_without_abbreviation',
                       'shall_not_with_abbreviation',
                       'shall_never'
                       ]}
        ]

        self.future_after_imply_main_type2_main_part_cmd_dict = \
            {'positive': self.future_after_imply_main_type2_main_part_pos_cmd,
             'negative': self.future_after_imply_main_type2_main_part_neg_cmd
             }

        # 2.1.2. appositive
        self.future_after_imply_main_type2_main_part_appositive_cmd = [{'simple_present': ['singular']}]
        self.future_after_imply_main_type2_main_part_appositive_cmd_dict \
            = {'positive': self.future_after_imply_main_type2_main_part_appositive_cmd}

        # 2.2. clause-part
        self.future_after_imply_main_type2_clause_part_cmd = self.future_after_imply_main_type1_pos_cmd
        self.future_after_imply_main_type2_clause_part_cmd_dict \
            = {'positive': self.future_after_imply_main_type2_clause_part_cmd}

        ################################################################################################################
        # C. tense: past
        # I. before_imply
        # 1. main-type1
        # 1.1. main
        self.past_before_imply_main_type1_pos_cmd = [
            {'simple_past': ['singular', self.adverb]},
            {'past_perfect': ['had', self.adverb]},
            {'past_perfect_continuous': ['had_been_doing', self.adverb]},
            {'present_perfect': ['singular', self.adverb]},  # not very proper but acceptable
            {'present_perfect_continuous': ['singular', self.adverb]}  # not very proper but acceptable
        ]

        self.past_before_imply_main_type1_neg_cmd = [
            {'simple_past': ['singular_not_without_abbreviation', self.adverb,
                             'singular_not_with_abbreviation',
                             'singular_never'
                             ]},
            {'past_perfect': ['had_not_without_abbreviation', self.adverb,
                              'had_not_with_abbreviation',
                              'had_never'
                              ]},
            # not very proper but acceptable
            {'present_perfect': ['singular_not_without_abbreviation', self.adverb,
                                 'singular_not_with_abbreviation',
                                 'singular_never'
                                 ]}
        ]

        self.past_before_imply_main_type1_cmd_dict = {'positive': self.past_before_imply_main_type1_pos_cmd,
                                                      'negative': self.past_before_imply_main_type1_neg_cmd
                                                      }
        # 1.2. appositive
        self.past_before_imply_main_type1_appositive_cmd = [{'simple_present': ['singular']},
                                                            {'simple_past': ['singular']}]
        self.past_before_imply_main_type1_appositive_cmd_dict \
            = {'positive': self.past_before_imply_main_type1_appositive_cmd}

        # 2. main-type2
        # 2.1.1. main-part
        self.past_before_imply_main_type2_main_part_pos_cmd = [
            {'simple_past': ['singular']}
        ]

        self.past_before_imply_main_type2_main_part_neg_cmd = [
            {'simple_past': ['singular_not_without_abbreviation',
                             'singular_not_with_abbreviation'
                             ]}
        ]

        self.past_before_imply_main_type2_main_part_cmd_dict = \
            {'positive': self.past_before_imply_main_type2_main_part_pos_cmd,
             'negative': self.past_before_imply_main_type2_main_part_neg_cmd
             }

        # 2.1.2. appositive
        self.past_before_imply_main_type2_main_part_appositive_cmd = [{'simple_present': ['singular']},
                                                                      {'simple_past': ['singular']}]
        self.past_before_imply_main_type2_main_part_appositive_cmd_dict \
            = {'positive': self.past_before_imply_main_type2_main_part_appositive_cmd}

        # 2.2. clause-part
        self.past_before_imply_main_type2_clause_part_cmd = self.past_before_imply_main_type1_pos_cmd
        self.past_before_imply_main_type2_clause_part_cmd_dict \
            = {'positive': self.past_before_imply_main_type2_clause_part_cmd}

        # II. after_imply
        # 1. main-type1
        # 1.1. main
        self.past_after_imply_main_type1_pos_cmd = [
            {'simple_past': ['singular', self.adverb]},
            {'past_perfect': ['had', self.adverb]},
            {'past_perfect_continuous': ['had_been_doing', self.adverb]},
            {'past_future': ['would', self.adverb]},
            {'past_future_perfect': ['would_have_done', self.adverb]},
            {'past_future_perfect_continuous': ['would_have_been_doing', self.adverb]},
            {'present_perfect': ['singular', self.adverb]},  # not very proper but acceptable
            {'present_perfect_continuous': ['singular', self.adverb]},  # not very proper but acceptable
            {'modal': ['should', self.adverb,
                       'ought_to', self.adverb,
                       'must', self.adverb,
                       'past_have_to', self.adverb,
                       'past_future_have_to', self.adverb,
                       'past_need_to', self.adverb]
             }
        ]

        self.past_after_imply_main_type1_neg_cmd = [
            {'simple_past': ['singular_not_without_abbreviation', self.adverb,
                             'singular_not_with_abbreviation',
                             'singular_never'
                             ]},
            {'past_perfect': ['had_not_without_abbreviation', self.adverb,
                              'had_not_with_abbreviation',
                              'had_never'
                              ]},
            {'past_future': ['would_not_without_abbreviation', self.adverb,
                             'would_not_with_abbreviation',
                             'would_never'
                             ]},
            {'past_future_perfect': ['would_not_have_without_abbreviation', self.adverb,
                                     'would_not_have_with_abbreviation',
                                     'would_never_have'
                                     ]},
            # not very proper but acceptable
            {'present_perfect': ['singular_not_without_abbreviation', self.adverb,
                                 'singular_not_with_abbreviation',
                                 'singular_never'
                                 ]},
            {'modal': ['should_not_without_abbreviation', self.adverb,
                       'should_not_with_abbreviation',
                       'should_never',
                       'ought_not_to_without_abbreviation',
                       'ought_not_to_with_abbreviation',
                       'ought_never_to',
                       'must_not_without_abbreviation', self.adverb,
                       'must_not_with_abbreviation',
                       'must_never'
                       ]}
        ]

        self.past_after_imply_main_type1_cmd_dict = {'positive': self.past_after_imply_main_type1_pos_cmd,
                                                     'negative': self.past_after_imply_main_type1_neg_cmd
                                                     }
        # 1.2. appositive
        self.past_after_imply_main_type1_appositive_cmd = [{'simple_present': ['singular']},
                                                           {'simple_past': ['singular']}]
        self.past_after_imply_main_type1_appositive_cmd_dict \
            = {'positive': self.past_after_imply_main_type1_appositive_cmd}

        # 2. main-type2
        # 2.1.1. main-part
        self.past_after_imply_main_type2_main_part_pos_cmd = [
            {'simple_past': ['singular']},
            {'past_future': ['would']},
            {'modal': ['should',
                       'ought_to',
                       'must',
                       'past_have_to',
                       'past_future_have_to',
                       'past_need_to']
             }
        ]

        self.past_after_imply_main_type2_main_part_neg_cmd = [
            {'simple_past': ['singular_not_without_abbreviation',
                             'singular_not_with_abbreviation',
                             'singular_never'
                             ]},
            {'past_future': ['would_not_without_abbreviation',
                             'would_not_with_abbreviation',
                             'would_never'
                             ]},
            {'modal': ['should_not_without_abbreviation',
                       'should_not_with_abbreviation',
                       'should_never',
                       'ought_not_to_without_abbreviation',
                       'ought_not_to_with_abbreviation',
                       'ought_never_to',
                       'must_not_without_abbreviation',
                       'must_not_with_abbreviation',
                       'must_never'
                       ]}
        ]

        self.past_after_imply_main_type2_main_part_cmd_dict = \
            {'positive': self.past_after_imply_main_type2_main_part_pos_cmd,
             'negative': self.past_after_imply_main_type2_main_part_neg_cmd
             }

        # 2.1.2. appositive
        self.past_after_imply_main_type2_main_part_appositive_cmd = [{'simple_present': ['singular']},
                                                                     {'simple_past': ['singular']}]
        self.past_after_imply_main_type2_main_part_appositive_cmd_dict \
            = {'positive': self.past_after_imply_main_type2_main_part_appositive_cmd}

        # 2.2. clause-part
        self.past_after_imply_main_type2_clause_part_cmd = self.past_after_imply_main_type1_pos_cmd
        self.past_after_imply_main_type2_clause_part_cmd_dict \
            = {'positive': self.past_after_imply_main_type2_clause_part_cmd}
