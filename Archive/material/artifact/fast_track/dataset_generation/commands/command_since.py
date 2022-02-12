

class PreCmdSince:
    def __init__(self, adv):
        self.adverb = adv
        """
        I. replace commands for 'once' operator (before_imply version)
        """
        # A. tense: present
        # i. from the perspective of present time
        # 1. main: before_imply
        self.once_present_cmd_pos_before_imply_present_version = [
            {'simple_present': ['singular', self.adverb]}
        ]

        self.once_present_cmd_neg_before_imply_present_version = [
            {'simple_present': ['singular_not_without_abbreviation', self.adverb,
                                'singular_not_with_abbreviation'
                                ]}
        ]

        self.once_present_cmd_dic_before_imply_present_version = \
            {'positive': self.once_present_cmd_pos_before_imply_present_version,
             'negative': self.once_present_cmd_neg_before_imply_present_version
             }

        # ii. from the perspective of past time
        # 1. main: before_imply
        self.once_present_cmd_pos_before_imply_past_version = [
            {'simple_past': ['singular', self.adverb]}
        ]

        self.once_present_cmd_neg_before_imply_past_version = [
            {'simple_past': ['singular_not_without_abbreviation', self.adverb,
                             'singular_not_with_abbreviation'
                             ]}
        ]

        self.once_present_cmd_dic_before_imply_past_version = \
            {'positive': self.once_present_cmd_pos_before_imply_past_version,
             'negative': self.once_present_cmd_neg_before_imply_past_version
             }

        ################################################################################################################
        # B. tense: future
        # 1. main: before_imply
        self.once_future_cmd_pos_before_imply = [
            {'simple_present': ['singular', self.adverb]}
        ]

        self.once_future_cmd_neg_before_imply = [
            {'simple_present': ['singular_not_without_abbreviation', self.adverb,
                                'singular_not_with_abbreviation'
                                ]}
        ]

        self.once_future_cmd_dic_before_imply = {'positive': self.once_future_cmd_pos_before_imply,
                                                 'negative': self.once_future_cmd_neg_before_imply
                                                 }

        ################################################################################################################
        # C. tense: past
        # 1. main: before_imply
        self.once_past_cmd_pos_before_imply = [
            {'simple_past': ['singular', self.adverb]},
            {'past_perfect': ['had', self.adverb]}
        ]

        self.once_past_cmd_neg_before_imply = [
            {'simple_past': ['singular_not_without_abbreviation', self.adverb,
                             'singular_not_with_abbreviation'
                             ]},
            {'past_perfect': ['had_not_without_abbreviation', self.adverb,
                              'had_not_with_abbreviation'
                              ]}
        ]

        self.once_past_cmd_dic_before_imply = {'positive': self.once_past_cmd_pos_before_imply,
                                               'negative': self.once_past_cmd_neg_before_imply
                                               }
