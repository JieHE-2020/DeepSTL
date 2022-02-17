

class PreCmdUntil:
    def __init__(self, adv):
        self.adverb = adv
        """
        I. replace commands for 'eventually' operator (before_imply version)
        """
        # A. tense: present
        # 1. main: before_imply
        self.eventually_present_cmd_pos_before_imply = [
            {'simple_present': ['singular', self.adverb]}
        ]

        self.eventually_present_cmd_neg_before_imply = [
            {'simple_present': ['singular_not_without_abbreviation', self.adverb,
                                'singular_not_with_abbreviation'
                                ]}
        ]

        self.eventually_present_cmd_dic_before_imply = {'positive': self.eventually_present_cmd_pos_before_imply,
                                                        'negative': self.eventually_present_cmd_neg_before_imply
                                                        }

        ################################################################################################################
        # B. tense: future
        # 1. main: before_imply
        self.eventually_future_cmd_pos_before_imply = self.eventually_present_cmd_pos_before_imply
        self.eventually_future_cmd_neg_before_imply = self.eventually_present_cmd_neg_before_imply
        self.eventually_future_cmd_dic_before_imply = {'positive': self.eventually_future_cmd_pos_before_imply,
                                                       'negative': self.eventually_future_cmd_neg_before_imply
                                                       }

        ################################################################################################################
        # C. tense: past
        # 1. main: before_imply
        self.eventually_past_cmd_pos_before_imply = [
            {'simple_present': ['singular', self.adverb]},
            {'simple_past': ['singular', self.adverb]}
        ]

        self.eventually_past_cmd_neg_before_imply = [
            {'simple_present': ['singular_not_without_abbreviation', self.adverb,
                                'singular_not_with_abbreviation'
                                ]},
            {'simple_past': ['singular_not_without_abbreviation', self.adverb,
                             'singular_not_with_abbreviation'
                             ]}
        ]

        self.eventually_past_cmd_dic_before_imply = {'positive': self.eventually_past_cmd_pos_before_imply,
                                                     'negative': self.eventually_past_cmd_neg_before_imply
                                                     }
