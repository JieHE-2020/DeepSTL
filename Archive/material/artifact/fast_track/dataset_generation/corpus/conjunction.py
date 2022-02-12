"""
conjunctions for formula type of: Always (CLAUSE 1 -> CLAUSE 2)
"""
conj_clause1_general = ['Whenever ',
                        'In case that ',
                        'Everytime when ',
                        'When ',
                        'If ',
                        'Globally, whenever ',
                        'Globally, in case that ',
                        'Globally, everytime when ',
                        'Globally, when ',
                        'Globally, if ',
                        'It is always the case that whenever ',
                        'It is always the case that in case that ',
                        'It is always the case that everytime when ',
                        'It is always the case that when ',
                        'It is always the case that if ',
                        'In the case ',
                        'On condition that ',
                        'As soon as '
                        ]

# when SP is selected for clause 1, and there is no ERE expressions,
# use the following list
conj_clause1_special = ['Whenever ',
                        'In case that ',
                        'In the case ',
                        'Everytime when ',
                        'When ',
                        'If ',
                        'While ',
                        'During the interval that ',
                        'Globally, whenever ',
                        'Globally, in case that ',
                        'Globally, everytime when ',
                        'Globally, when ',
                        'Globally, if ',
                        'Globally, while ',
                        'Globally, during the interval that ',
                        'It is always the case that whenever ',
                        'It is always the case that in case that ',
                        'It is always the case that everytime when ',
                        'It is always the case that when ',
                        'It is always the case that if ',
                        'It is always the case that while ',
                        'In the case ',
                        'On condition that ',
                        'In the event that ',
                        'As soon as '
                        ]

# when clause 2 does not belong to TP (layer 2 - layer 6)
# use the following list
conj_clause2_general = [', then ',
                        ', then in response ',
                        ', then the following condition holds: ',
                        ', then the following condition is true: ',
                        ', then all of the following conditions hold: ',
                        ', then all of the following conditions are true: ',
                        ' then ',
                        ' then in response ',
                        ' then the following condition holds: ',
                        ' then the following condition is true: ',
                        ' then all of the following conditions hold: ',
                        ' then all of the following conditions are true: '
                        ]

# when clause 2 belongs TP (layer 2 - layer 6)
# use the following list
conj_clause2_special = [', then ',
                        ', then in response ',
                        ' then ',
                        ' then in response '
                        ]

# conj_clause1_se = conj_clause1_se[random.randint(0, len(conj_clause1_se)) - 1]
# print(conj_clause1_se)