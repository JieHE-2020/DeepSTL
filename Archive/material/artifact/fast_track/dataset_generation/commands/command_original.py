from corpus import adverbial_modifiers


class PredicateCommandPresent:
    def __init__(self, adv):
        self.adverb = adv

        self.cmd_pos_none = [{'present': ['single']}]
        self.cmd_pos_adv = [{'present': ['single', self.adverb]},
                            {'future': ['will', self.adverb]},
                            {'modal': ['should', self.adverb,
                                       'must', self.adverb,
                                       'shall', self.adverb,
                                       'TPS_have_to', self.adverb,
                                       'FT_have_to', self.adverb,
                                       'TPS_need_to', self.adverb]
                             }]
        self.cmd_neg_none = [{'present': ['single_not_without_abbreviation',
                                          'single_not_with_abbreviation']}]
        self.cmd_neg_adv = [
            {'present': ['single_not_without_abbreviation', self.adverb,
                         'single_not_with_abbreviation',
                         'single_never'
                         ]},
            {'future': ['will_not_without_abbreviation', self.adverb,
                        'will_not_with_abbreviation',
                        'will_never']},
            {'modal': ['should_not_without_abbreviation', self.adverb,
                       'should_not_with_abbreviation',
                       'should_never',
                       'must_not_without_abbreviation', self.adverb,
                       'must_not_with_abbreviation',
                       'must_never',
                       'shall_not_without_abbreviation', self.adverb,
                       'shall_not_with_abbreviation',
                       'shall_never'
                       ]}
        ]

        self.cmd_dic_none = {'positive': self.cmd_pos_none,
                             'negative': self.cmd_neg_none,
                             }
        self.cmd_dic_adv = {'positive': self.cmd_pos_adv,
                            'negative': self.cmd_neg_adv,
                            }


class PreCmdPureSP(PredicateCommandPresent):
    def __init__(self, adv):
        super().__init__(adv)


class PreCmdEventually(PredicateCommandPresent):
    def __init__(self, adv):
        super().__init__(adv)
        self.delete_neverTerm()
        self.assembleDict()

    # delete command whose contents include 'never'
    def delete_neverTerm(self):
        for item in self.cmd_neg_adv:
            for value in item.values():
                # print(value)
                for element in value:
                    if isinstance(element, str):
                        if 'never' in element:
                            index = value.index(element)
                            del value[index]
        # print('\nafter deletion:')
        # for item in self.cmd_neg_adv:
        #     for value in item.values():
        #         print(value)

    def assembleDict(self):
        self.cmd_dic_none = {'positive': self.cmd_pos_none,
                             'negative': self.cmd_neg_none,
                             }
        self.cmd_dic_adv = {'positive': self.cmd_pos_adv,
                            'negative': self.cmd_neg_adv,
                            }


# adverb = adverbial_modifiers.adv_eventually
# pre_cmd_eventually = PreCmdEventually(adverb)

class PreCmdAlways(PredicateCommandPresent):
    def __init__(self, adv):
        super().__init__(adv)


class PreCmdOnce:
    def __init__(self, adv):
        self.adverb = adv

        self.cmd_pos_none = [{'past': ['single_plural']}]
        self.cmd_pos_adv = [{'past': ['single_plural', self.adverb]},
                            {'past_future': ['would', self.adverb]},
                            {'modal': ['should', self.adverb,
                                       'must', self.adverb,
                                       'PT_have_to', self.adverb,
                                       'PFT_have_to', self.adverb,
                                       'PT_need_to', self.adverb]
                             }]
        self.cmd_neg_none = [{'past': ['not_without_abbreviation',
                                       'not_with_abbreviation']}]
        self.cmd_neg_adv = [
            {'past': ['not_without_abbreviation', self.adverb,
                      'not_with_abbreviation',
                      'never'
                      ]},
            {'past_future': ['would_not_without_abbreviation', self.adverb,
                             'would_not_with_abbreviation',
                             'would_never']},
            {'modal': ['should_not_without_abbreviation', self.adverb,
                       'should_not_with_abbreviation',
                       'should_never',
                       'must_not_without_abbreviation', self.adverb,
                       'must_not_with_abbreviation',
                       'must_never'
                       ]}
        ]

        self.cmd_dic_none = {'positive': self.cmd_pos_none,
                             'negative': self.cmd_neg_none,
                             }
        self.cmd_dic_adv = {'positive': self.cmd_pos_adv,
                            'negative': self.cmd_neg_adv,
                            }


class PreCmdHistorically:
    def __init__(self, adv):
        self.adverb = adv

        self.cmd_pos_none = [{'present': ['single']},
                             {'past': ['single_plural']},
                             {'present_perfect': ['single']},
                             {'present_perfect_continuous': ['single']}]

        self.cmd_pos_adv = [{'present': ['single', self.adverb]},
                            {'past': ['single_plural', self.adverb]},
                            {'present_perfect': ['single', self.adverb]},
                            {'present_perfect_continuous': ['single', self.adverb]},
                            {'future': ['will', self.adverb]},
                            {'modal': ['should', self.adverb,
                                       'must', self.adverb,
                                       'shall', self.adverb,
                                       'TPS_have_to', self.adverb,
                                       'FT_have_to', self.adverb,
                                       'TPS_need_to', self.adverb]
                             }]
        self.cmd_neg_none = [{'past': ['not_without_abbreviation',
                                       'not_with_abbreviation']}]
        self.cmd_neg_adv = [
            {'past': ['not_without_abbreviation', self.adverb,
                      'not_with_abbreviation',
                      'never'
                      ]},
            {'past_future': ['would_not_without_abbreviation', self.adverb,
                             'would_not_with_abbreviation',
                             'would_never']},
            {'modal': ['should_not_without_abbreviation', self.adverb,
                       'should_not_with_abbreviation',
                       'should_never',
                       'must_not_without_abbreviation', self.adverb,
                       'must_not_with_abbreviation',
                       'must_never'
                       ]}
        ]

        self.cmd_dic_none = {'positive': self.cmd_pos_none,
                             'negative': self.cmd_neg_none,
                             }
        self.cmd_dic_adv = {'positive': self.cmd_pos_adv,
                            'negative': self.cmd_neg_adv,
                            }
