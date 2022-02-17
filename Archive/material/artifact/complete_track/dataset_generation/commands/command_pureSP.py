

class PreCmdPureSP:
    def __init__(self, adv):
        self.adverb = adv

        self.cmd_pos_before_imply = [{'simple_present': ['singular']}]

        self.cmd_neg_before_imply = [{'simple_present': ['singular_not_without_abbreviation',
                                                         'singular_not_with_abbreviation']}]

        self.cmd_pos_after_imply = [
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

        self.cmd_neg_after_imply = [
            {'simple_present': ['singular_not_without_abbreviation', self.adverb,
                                'singular_not_with_abbreviation',
                                'singular_never'
                                ]},
            {'simple_future': ['will_not_without_abbreviation', self.adverb,
                               'will_not_with_abbreviation',
                               'will_never'
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

        self.cmd_appositive = [{'simple_present': ['singular']}]
        self.cmd_dic_appositive = {'positive': self.cmd_appositive}
