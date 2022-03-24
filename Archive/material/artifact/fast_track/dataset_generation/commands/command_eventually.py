

class PreCmdEventually:
    def __init__(self, adv):
        self.adverb = adv
        # A. tense: present
        # 1. main: before_imply
        self.present_cmd_pos_before_imply = [
            {'simple_present': ['singular', self.adverb]},
            {'simple_future': ['will', self.adverb]}
        ]

        self.present_cmd_neg_before_imply = [
            {'simple_present': ['singular_not_without_abbreviation', self.adverb,
                                'singular_not_with_abbreviation'
                                ]},
            {'simple_future': ['will_not_without_abbreviation', self.adverb,
                               'will_not_with_abbreviation'
                               ]}
        ]

        self.present_cmd_dic_before_imply = {'positive': self.present_cmd_pos_before_imply,
                                             'negative': self.present_cmd_neg_before_imply
                                             }
        # 2. main: after_imply
        self.present_cmd_pos_after_imply = [
            {'simple_present': ['singular', self.adverb]},
            {'simple_future': ['will', self.adverb]},
            {'modal': ['should', self.adverb,
                       'ought_to', self.adverb,
                       'must', self.adverb,
                       'shall', self.adverb,
                       'present_singular_have_to', self.adverb,
                       'future_have_to', self.adverb,
                       'present_singular_need_to', self.adverb]
             }]

        self.present_cmd_neg_after_imply = [
            {'simple_present': ['singular_not_without_abbreviation', self.adverb,
                                'singular_not_with_abbreviation'
                                ]},
            {'simple_future': ['will_not_without_abbreviation', self.adverb,
                               'will_not_with_abbreviation'
                               ]},
            {'modal': ['should_not_without_abbreviation', self.adverb,
                       'should_not_with_abbreviation',
                       'ought_not_to_without_abbreviation',
                       'ought_not_to_with_abbreviation',
                       'must_not_without_abbreviation', self.adverb,
                       'must_not_with_abbreviation',
                       'shall_not_without_abbreviation', self.adverb,
                       'shall_not_with_abbreviation'
                       ]}
        ]

        self.present_cmd_dic_after_imply = {'positive': self.present_cmd_pos_after_imply,
                                            'negative': self.present_cmd_neg_after_imply
                                            }

        # 3. appositive
        self.present_cmd_appositive = [{'simple_present': ['singular']}]
        self.present_cmd_dic_appositive = {'positive': self.present_cmd_appositive}

        ################################################################################################################
        # B. tense: future
        # 1. main: before_imply
        self.future_cmd_pos_before_imply = [
            {'simple_present': ['singular', self.adverb]},
            {'simple_future': ['will', self.adverb]}
        ]

        self.future_cmd_neg_before_imply = [
            {'simple_present': ['singular_not_without_abbreviation', self.adverb,
                                'singular_not_with_abbreviation'
                                ]},
            {'simple_future': ['will_not_without_abbreviation', self.adverb,
                               'will_not_with_abbreviation'
                               ]}
        ]

        self.future_cmd_dic_before_imply = {'positive': self.future_cmd_pos_before_imply,
                                            'negative': self.future_cmd_neg_before_imply
                                            }
        # 2. main: after_imply
        self.future_cmd_pos_after_imply = [
            {'simple_present': ['singular', self.adverb]},
            {'simple_future': ['will', self.adverb]},
            {'modal': ['should', self.adverb,
                       'ought_to', self.adverb,
                       'must', self.adverb,
                       'shall', self.adverb,
                       'present_singular_have_to', self.adverb,
                       'future_have_to', self.adverb,
                       'present_singular_need_to', self.adverb]
             }]

        self.future_cmd_neg_after_imply = [
            {'simple_present': ['singular_not_without_abbreviation', self.adverb,
                                'singular_not_with_abbreviation'
                                ]},
            {'simple_future': ['will_not_without_abbreviation', self.adverb,
                               'will_not_with_abbreviation'
                               ]},
            {'modal': ['should_not_without_abbreviation', self.adverb,
                       'should_not_with_abbreviation',
                       'ought_not_to_without_abbreviation',
                       'ought_not_to_with_abbreviation',
                       'must_not_without_abbreviation', self.adverb,
                       'must_not_with_abbreviation',
                       'shall_not_without_abbreviation', self.adverb,
                       'shall_not_with_abbreviation'
                       ]}
        ]

        self.future_cmd_dic_after_imply = {'positive': self.future_cmd_pos_after_imply,
                                           'negative': self.future_cmd_neg_after_imply
                                           }

        # 3. appositive
        self.future_cmd_appositive = [{'simple_present': ['singular']}]
        self.future_cmd_dic_appositive = {'positive': self.future_cmd_appositive}

        ################################################################################################################
        # C. tense: past
        # 1. main: before_imply
        self.past_cmd_pos_before_imply = [
            {'simple_present': ['singular', self.adverb]},
            {'simple_past': ['singular', self.adverb]},
            {'past_future': ['would', self.adverb]}
        ]

        self.past_cmd_neg_before_imply = [
            {'simple_present': ['singular_not_without_abbreviation', self.adverb,
                                'singular_not_with_abbreviation'
                                ]},
            {'simple_past': ['singular_not_without_abbreviation', self.adverb,
                             'singular_not_with_abbreviation'
                             ]},
            {'past_future': ['would_not_without_abbreviation', self.adverb,
                             'would_not_with_abbreviation'
                             ]}
        ]

        self.past_cmd_dic_before_imply = {'positive': self.past_cmd_pos_before_imply,
                                          'negative': self.past_cmd_neg_before_imply
                                          }
        # 2. main: after_imply
        self.past_cmd_pos_after_imply = [
            {'simple_present': ['singular', self.adverb]},
            {'simple_past': ['singular', self.adverb]},
            {'past_future': ['would', self.adverb]},
            {'modal': ['should', self.adverb,
                       'ought_to', self.adverb,
                       'must', self.adverb,
                       'present_singular_have_to', self.adverb,
                       'present_singular_need_to', self.adverb,
                       'past_have_to', self.adverb,
                       'past_future_have_to', self.adverb,
                       'past_need_to', self.adverb
                       ]
             }]

        self.past_cmd_neg_after_imply = [
            {'simple_present': ['singular_not_without_abbreviation', self.adverb,
                                'singular_not_with_abbreviation'
                                ]},
            {'simple_past': ['singular_not_without_abbreviation', self.adverb,
                             'singular_not_with_abbreviation'
                             ]},
            {'past_future': ['would_not_without_abbreviation', self.adverb,
                             'would_not_with_abbreviation'
                             ]},
            {'modal': ['should_not_without_abbreviation', self.adverb,
                       'should_not_with_abbreviation',
                       'ought_not_to_without_abbreviation',
                       'ought_not_to_with_abbreviation',
                       'must_not_without_abbreviation', self.adverb,
                       'must_not_with_abbreviation'
                       ]}
        ]

        self.past_cmd_dic_after_imply = {'positive': self.past_cmd_pos_after_imply,
                                         'negative': self.past_cmd_neg_after_imply
                                         }

        # 3. appositive
        self.past_cmd_appositive = [{'simple_present': ['singular']},
                                    {'simple_past': ['singular']}]
        self.past_cmd_dic_appositive = {'positive': self.past_cmd_appositive}
