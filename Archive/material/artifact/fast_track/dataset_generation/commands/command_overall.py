class PreCmdOverall:
    def __init__(self, adv):
        self.adverb = adv

        self.cmd_pos_before_imply = [{'simple_present': ['singular']}]

        self.cmd_neg_before_imply = [{'simple_present': ['singular_not_without_abbreviation',
                                                         'singular_not_with_abbreviation']}]

        self.cmd_pos_after_imply = [
            {'simple_present': ['singular', self.adverb]},
            {'simple_past': ['singular', self.adverb]},
            {'simple_future': ['will', self.adverb]},
            {'past_future': ['would', self.adverb]},

            {'future_progressive': ['will_be', self.adverb]},
            {'past_future_progressive': ['would_be', self.adverb]},

            {'present_perfect': ['singular', self.adverb]},
            {'past_perfect': ['had', self.adverb]},
            {'future_perfect': ['will_have_done', self.adverb]},
            {'past_future_perfect': ['would_have_done', self.adverb]},

            {'present_perfect_continuous': ['singular', self.adverb]},
            {'past_perfect_continuous': ['had_been_doing', self.adverb]},
            {'future_perfect_continuous': ['will_have_been_doing', self.adverb]},
            {'past_future_perfect_continuous': ['would_have_been_doing', self.adverb]},

            {'modal': ['should', self.adverb,
                       'ought_to', self.adverb,
                       'must', self.adverb,
                       'shall', self.adverb,
                       'present_singular_have_to', self.adverb,
                       'future_have_to', self.adverb,
                       'present_singular_need_to', self.adverb,
                       'past_have_to', self.adverb,
                       'past_future_have_to', self.adverb,
                       'past_need_to', self.adverb
                       ]
             }]

        self.cmd_neg_after_imply = [
            {'simple_present': ['singular_not_without_abbreviation', self.adverb,
                                'singular_not_with_abbreviation',
                                'singular_never'
                                ]},
            {'simple_past': ['singular_not_without_abbreviation', self.adverb,
                             'singular_not_with_abbreviation',
                             'singular_never'
                             ]},
            {'simple_future': ['will_not_without_abbreviation', self.adverb,
                               'will_not_with_abbreviation',
                               'will_never'
                               ]},
            {'past_future': ['would_not_without_abbreviation', self.adverb,
                             'would_not_with_abbreviation',
                             'would_never'
                             ]},

            {'present_perfect': ['singular_not_without_abbreviation', self.adverb,
                                 'singular_not_with_abbreviation',
                                 'singular_never'
                                 ]},
            {'past_perfect': ['had_not_without_abbreviation', self.adverb,
                              'had_not_with_abbreviation',
                              'had_never'
                              ]},
            {'future_perfect': ['will_not_have_without_abbreviation', self.adverb,
                                'will_not_have_with_abbreviation',
                                'will_never_have'
                                ]},
            {'past_future_perfect': ['would_not_have_without_abbreviation', self.adverb,
                                     'would_not_have_with_abbreviation',
                                     'would_never_have'
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

        self.cmd_dic_before_imply = {'positive': self.cmd_pos_before_imply,
                                     'negative': self.cmd_neg_before_imply
                                     }

        self.cmd_dic_after_imply = {'positive': self.cmd_pos_after_imply,
                                    'negative': self.cmd_neg_after_imply
                                    }
