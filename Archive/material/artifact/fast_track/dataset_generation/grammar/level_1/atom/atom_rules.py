# SE
# category 0
SE_0_0 = {'type': 'SE',
          'index': [0, 0],
          'ingredient': ['sig', 'value'],
          'expression': 'sig == value',
          'probability': 0.84}

SE_0_1 = {'type': 'SE',
          'index': [0, 1],
          'ingredient': ['sig', 'value'],
          'expression': 'not (sig == value)',
          'probability': 0.1}

SE_0_2 = {'type': 'SE',
          'index': [0, 2],
          'ingredient': ['sig', 'value'],
          'expression': 'not rise (sig == value)',
          'probability': 0.01}

SE_0_3 = {'type': 'SE',
          'index': [0, 3],
          'ingredient': ['sig', 'value'],
          'expression': 'not fall (sig == value)',
          'probability': 0.05}

# category 1
SE_1_0 = {'type': 'SE',
          'index': [1, 0],
          'ingredient': ['sig', 'value'],
          'expression': 'sig >= value',
          'probability': 0.42}

SE_1_1 = {'type': 'SE',
          'index': [1, 1],
          'ingredient': ['sig', 'value'],
          'expression': 'sig > value',
          'probability': 0.42}

SE_1_2 = {'type': 'SE',
          'index': [1, 2],
          'ingredient': ['sig', 'value'],
          'expression': 'not (sig >= value)',
          'probability': 0.05}

SE_1_3 = {'type': 'SE',
          'index': [1, 3],
          'ingredient': ['sig', 'value'],
          'expression': 'not (sig > value)',
          'probability': 0.05}

SE_1_4 = {'type': 'SE',
          'index': [1, 4],
          'ingredient': ['sig', 'value'],
          'expression': 'not rise (sig >= value)',
          'probability': 0.01}

SE_1_5 = {'type': 'SE',
          'index': [1, 5],
          'ingredient': ['sig', 'value'],
          'expression': 'not rise (sig > value)',
          'probability': 0.01}

SE_1_6 = {'type': 'SE',
          'index': [1, 6],
          'ingredient': ['sig', 'value'],
          'expression': 'not fall (sig >= value)',
          'probability': 0.02}

SE_1_7 = {'type': 'SE',
          'index': [1, 7],
          'ingredient': ['sig', 'value'],
          'expression': 'not fall (sig > value)',
          'probability': 0.02}

# category 2
SE_2_0 = {'type': 'SE',
          'index': [2, 0],
          'ingredient': ['sig', 'value'],
          'expression': 'sig <= value',
          'probability': 0.42}

SE_2_1 = {'type': 'SE',
          'index': [2, 1],
          'ingredient': ['sig', 'value'],
          'expression': 'sig < value',
          'probability': 0.42}

SE_2_2 = {'type': 'SE',
          'index': [2, 2],
          'ingredient': ['sig', 'value'],
          'expression': 'not (sig <= value)',
          'probability': 0.08}

SE_2_3 = {'type': 'SE',
          'index': [2, 3],
          'ingredient': ['sig', 'value'],
          'expression': 'not (sig < value)',
          'probability': 0.08}

SE_2_4 = {'type': 'SE',
          'index': [2, 4],
          'ingredient': ['sig', 'value'],
          'expression': 'not rise (sig <= value)',
          'probability': 0}

SE_2_5 = {'type': 'SE',
          'index': [2, 5],
          'ingredient': ['sig', 'value'],
          'expression': 'not rise (sig < value)',
          'probability': 0}

SE_2_6 = {'type': 'SE',
          'index': [2, 6],
          'ingredient': ['sig', 'value'],
          'expression': 'not fall (sig <= value)',
          'probability': 0}

SE_2_7 = {'type': 'SE',
          'index': [2, 7],
          'ingredient': ['sig', 'value'],
          'expression': 'not fall (sig < value)',
          'probability': 0}

# category 3
SE_3_0 = {'type': 'SE',
          'index': [3, 0],
          'ingredient': ['sig', 'value1', 'value2'],
          'expression': 'sig >= value1 and sig <= value2',
          'probability': 0.36}

SE_3_1 = {'type': 'SE',
          'index': [3, 1],
          'ingredient': ['sig', 'value1', 'value2'],
          'expression': 'sig > value1 and sig <= value2',
          'probability': 0.05}

SE_3_2 = {'type': 'SE',
          'index': [3, 2],
          'ingredient': ['sig', 'value1', 'value2'],
          'expression': 'sig >= value1 and sig < value2',
          'probability': 0.05}

SE_3_3 = {'type': 'SE',
          'index': [3, 3],
          'ingredient': ['sig', 'value1', 'value2'],
          'expression': 'sig > value1 and sig < value2',
          'probability': 0.36}

SE_3_4 = {'type': 'SE',
          'index': [3, 4],
          'ingredient': ['sig', 'value1', 'value2'],
          'expression': 'not (sig >= value1 and sig <= value2)',
          'probability': 0.05}

SE_3_5 = {'type': 'SE',
          'index': [3, 5],
          'ingredient': ['sig', 'value1', 'value2'],
          'expression': 'not (sig > value1 and sig <= value2)',
          'probability': 0.01}

SE_3_6 = {'type': 'SE',
          'index': [3, 6],
          'ingredient': ['sig', 'value1', 'value2'],
          'expression': 'not (sig >= value1 and sig < value2)',
          'probability': 0.01}

SE_3_7 = {'type': 'SE',
          'index': [3, 7],
          'ingredient': ['sig', 'value1', 'value2'],
          'expression': 'not (sig > value1 and sig < value2)',
          'probability': 0.05}

SE_3_8 = {'type': 'SE',
          'index': [3, 8],
          'ingredient': ['sig', 'value1', 'value2'],
          'expression': 'not rise (sig >= value1 and sig <= value2)',
          'probability': 0.01}

SE_3_9 = {'type': 'SE',
          'index': [3, 9],
          'ingredient': ['sig', 'value1', 'value2'],
          'expression': 'not rise (sig > value1 and sig <= value2)',
          'probability': 0}

SE_3_10 = {'type': 'SE',
           'index': [3, 10],
           'ingredient': ['sig', 'value1', 'value2'],
           'expression': 'not rise (sig >= value1 and sig < value2)',
           'probability': 0}

SE_3_11 = {'type': 'SE',
           'index': [3, 11],
           'ingredient': ['sig', 'value1', 'value2'],
           'expression': 'not rise (sig > value1 and sig < value2)',
           'probability': 0.01}

SE_3_12 = {'type': 'SE',
           'index': [3, 12],
           'ingredient': ['sig', 'value1', 'value2'],
           'expression': 'not fall (sig >= value1 and sig <= value2)',
           'probability': 0.02}

SE_3_13 = {'type': 'SE',
           'index': [3, 13],
           'ingredient': ['sig', 'value1', 'value2'],
           'expression': 'not fall (sig > value1 and sig <= value2)',
           'probability': 0}

SE_3_14 = {'type': 'SE',
           'index': [3, 14],
           'ingredient': ['sig', 'value1', 'value2'],
           'expression': 'not fall (sig >= value1 and sig < value2)',
           'probability': 0}

SE_3_15 = {'type': 'SE',
           'index': [3, 15],
           'ingredient': ['sig', 'value1', 'value2'],
           'expression': 'not fall (sig > value1 and sig < value2)',
           'probability': 0.02}

# category 4
SE_4_0 = {'type': 'SE',
          'index': [4, 0],
          'ingredient': ['sig', 'mode'],
          'expression': 'sig == mode',
          'probability': 0.84}

SE_4_1 = {'type': 'SE',
          'index': [4, 1],
          'ingredient': ['sig', 'mode'],
          'expression': 'not (sig == mode)',
          'probability': 0.1}

SE_4_2 = {'type': 'SE',
          'index': [4, 2],
          'ingredient': ['sig', 'mode'],
          'expression': 'not rise (sig == mode)',
          'probability': 0.04}

SE_4_3 = {'type': 'SE',
          'index': [4, 3],
          'ingredient': ['sig', 'mode'],
          'expression': 'not fall (sig == mode)',
          'probability': 0.02}

# SE_4_4 = {'type': 'SE',
#           'index': [4, 4],
#           'ingredient': ['substitution'],
#           'expression': 'not substitution',
#           'probability': 0.14}

# # category 5
# SE_5_0 = {'type': 'SE',
#           'index': [5, 0],
#           'ingredient': ['sig', 'mode1', 'mode2'],
#           'expression': 'sig == mode1 or sig == mode2',
#           'probability': 0.25}
#
# SE_5_1 = {'type': 'SE',
#           'index': [5, 1],
#           'ingredient': ['sig', 'mode1', 'mode2'],
#           'expression': 'not (sig == mode1 or sig == mode2)',
#           'probability': 0.25}
#
# SE_5_2 = {'type': 'SE',
#           'index': [5, 2],
#           'ingredient': ['sig', 'mode1', 'mode2'],
#           'expression': 'not rise (sig == mode1 or sig == mode2)',
#           'probability': 0.25}
#
# SE_5_3 = {'type': 'SE',
#           'index': [5, 3],
#           'ingredient': ['sig', 'mode1', 'mode2'],
#           'expression': 'not fall (sig == mode1 or sig == mode2)',
#           'probability': 0.25}

# SE_5_4 = {'type': 'SE',
#           'index': [5, 4],
#           'ingredient': ['substitution1', 'substitution2'],
#           'expression': 'not (substitution1 or substitution2)',
#           'probability': 0.14}

# SE = [[SE_0_0, SE_0_1, SE_0_2, SE_0_3],
#       [SE_1_0, SE_1_1, SE_1_2, SE_1_3, SE_1_4, SE_1_5, SE_1_6, SE_1_7],
#       [SE_2_0, SE_2_1, SE_2_2, SE_2_3, SE_2_4, SE_2_5, SE_2_6, SE_2_7],
#       [SE_3_0, SE_3_1, SE_3_2, SE_3_3, SE_3_4, SE_3_5, SE_3_6, SE_3_7, SE_3_8, SE_3_9, SE_3_10, SE_3_11, SE_3_12,
#        SE_3_13, SE_3_14, SE_3_15],
#       [SE_4_0, SE_4_1, SE_4_2, SE_4_3, SE_4_4],
#       [SE_5_0, SE_5_1, SE_5_2, SE_5_3, SE_5_4],
#       ]

# SE = [[SE_0_0, SE_0_1, SE_0_2, SE_0_3],
#       [SE_1_0, SE_1_1, SE_1_2, SE_1_3, SE_1_4, SE_1_5, SE_1_6, SE_1_7],
#       [SE_2_0, SE_2_1, SE_2_2, SE_2_3, SE_2_4, SE_2_5, SE_2_6, SE_2_7],
#       [SE_3_0, SE_3_1, SE_3_2, SE_3_3, SE_3_4, SE_3_5, SE_3_6, SE_3_7, SE_3_8, SE_3_9, SE_3_10, SE_3_11, SE_3_12,
#        SE_3_13, SE_3_14, SE_3_15],
#       [SE_4_0, SE_4_1, SE_4_2, SE_4_3],
#       [SE_5_0, SE_5_1, SE_5_2, SE_5_3]
#       ]

SE = [[SE_0_0, SE_0_1, SE_0_2, SE_0_3],
      [SE_1_0, SE_1_1, SE_1_2, SE_1_3, SE_1_4, SE_1_5, SE_1_6, SE_1_7],
      [SE_2_0, SE_2_1, SE_2_2, SE_2_3, SE_2_4, SE_2_5, SE_2_6, SE_2_7],
      [SE_3_0, SE_3_1, SE_3_2, SE_3_3, SE_3_4, SE_3_5, SE_3_6, SE_3_7, SE_3_8, SE_3_9, SE_3_10, SE_3_11, SE_3_12,
       SE_3_13, SE_3_14, SE_3_15],
      [SE_4_0, SE_4_1, SE_4_2, SE_4_3]
      ]


# ERE
# category 0
ERE_0_0 = {'type': 'ERE',
           'index': [0, 0],
           'ingredient': ['sig', 'value'],
           'expression': 'rise (sig == value)',
           'probability': 0.6}

ERE_0_1 = {'type': 'ERE',
           'index': [0, 1],
           'ingredient': ['sig', 'value'],
           'expression': 'fall (sig == value)',
           'probability': 0.4}

# category 1
ERE_1_0 = {'type': 'ERE',
           'index': [1, 0],
           'ingredient': ['sig', 'value'],
           'expression': 'rise (sig >= value)',
           'probability': 0.5}

ERE_1_1 = {'type': 'ERE',
           'index': [1, 1],
           'ingredient': ['sig', 'value'],
           'expression': 'rise (sig > value)',
           'probability': 0.5}

ERE_1_2 = {'type': 'ERE',
           'index': [1, 2],
           'ingredient': ['sig', 'value'],
           'expression': 'fall (sig >= value)',
           'probability': 0}

ERE_1_3 = {'type': 'ERE',
           'index': [1, 3],
           'ingredient': ['sig', 'value'],
           'expression': 'fall (sig > value)',
           'probability': 0}


# category 2
ERE_2_0 = {'type': 'ERE',
           'index': [2, 0],
           'ingredient': ['sig', 'value'],
           'expression': 'rise (sig <= value)',
           'probability': 0.5}

ERE_2_1 = {'type': 'ERE',
           'index': [2, 1],
           'ingredient': ['sig', 'value'],
           'expression': 'rise (sig < value)',
           'probability': 0.5}

ERE_2_2 = {'type': 'ERE',
           'index': [2, 2],
           'ingredient': ['sig', 'value'],
           'expression': 'fall (sig <= value)',
           'probability': 0}

ERE_2_3 = {'type': 'ERE',
           'index': [2, 3],
           'ingredient': ['sig', 'value'],
           'expression': 'fall (sig < value)',
           'probability': 0}


# category 3
ERE_3_0 = {'type': 'ERE',
           'index': [3, 0],
           'ingredient': ['sig', 'value1', 'value2'],
           'expression': 'rise (sig >= value1 and sig <= value2)',
           'probability': 0.25}

ERE_3_1 = {'type': 'ERE',
           'index': [3, 1],
           'ingredient': ['sig', 'value1', 'value2'],
           'expression': 'rise (sig > value1 and sig <= value2)',
           'probability': 0.05}

ERE_3_2 = {'type': 'ERE',
           'index': [3, 2],
           'ingredient': ['sig', 'value1', 'value2'],
           'expression': 'rise (sig >= value1 and sig < value2)',
           'probability': 0.05}

ERE_3_3 = {'type': 'ERE',
           'index': [3, 3],
           'ingredient': ['sig', 'value1', 'value2'],
           'expression': 'rise (sig > value1 and sig < value2)',
           'probability': 0.25}

ERE_3_4 = {'type': 'ERE',
           'index': [3, 4],
           'ingredient': ['sig', 'value1', 'value2'],
           'expression': 'fall (sig >= value1 and sig <= value2)',
           'probability': 0.16}

ERE_3_5 = {'type': 'ERE',
           'index': [3, 5],
           'ingredient': ['sig', 'value1', 'value2'],
           'expression': 'fall (sig > value1 and sig <= value2)',
           'probability': 0.04}

ERE_3_6 = {'type': 'ERE',
           'index': [3, 6],
           'ingredient': ['sig', 'value1', 'value2'],
           'expression': 'fall (sig >= value1 and sig < value2)',
           'probability': 0.04}

ERE_3_7 = {'type': 'ERE',
           'index': [3, 7],
           'ingredient': ['sig', 'value1', 'value2'],
           'expression': 'fall (sig > value1 and sig < value2)',
           'probability': 0.16}

# category 4
ERE_4_0 = {'type': 'ERE',
           'index': [4, 0],
           'ingredient': ['sig', 'mode'],
           'expression': 'rise (sig == mode)',
           'probability': 0.6}

ERE_4_1 = {'type': 'ERE',
           'index': [4, 1],
           'ingredient': ['sig', 'mode'],
           'expression': 'fall (sig == mode)',
           'probability': 0.4}

# # category 5
# ERE_5_0 = {'type': 'ERE',
#            'index': [5, 0],
#            'ingredient': ['sig', 'mode1', 'mode2'],
#            'expression': 'rise (sig == mode1 or sig == mode2)',
#            'probability': 0.5}
#
# ERE_5_1 = {'type': 'ERE',
#            'index': [5, 1],
#            'ingredient': ['sig', 'mode1', 'mode2'],
#            'expression': 'fall (sig == mode1 or sig == mode2)',
#            'probability': 0.5}

# ERE = [[ERE_0_0, ERE_0_1],
#        [ERE_1_0, ERE_1_1, ERE_1_2, ERE_1_3],
#        [ERE_2_0, ERE_2_1, ERE_2_2, ERE_2_3],
#        [ERE_3_0, ERE_3_1, ERE_3_2, ERE_3_3, ERE_3_4, ERE_3_5, ERE_3_6, ERE_3_7],
#        [ERE_4_0, ERE_4_1],
#        [ERE_5_0, ERE_5_1]
#        ]

ERE = [[ERE_0_0, ERE_0_1],
       [ERE_1_0, ERE_1_1, ERE_1_2, ERE_1_3],
       [ERE_2_0, ERE_2_1, ERE_2_2, ERE_2_3],
       [ERE_3_0, ERE_3_1, ERE_3_2, ERE_3_3, ERE_3_4, ERE_3_5, ERE_3_6, ERE_3_7],
       [ERE_4_0, ERE_4_1]
       ]

# Negation of atom expressions
# 1. negation of SE expressions
# category 0
negate_SE_0 = [SE_0_1, SE_0_0, ERE_0_0, ERE_0_1]
# category 1
negate_SE_1 = [SE_1_2, SE_1_3, SE_1_0, SE_1_1, ERE_1_0, ERE_1_1, ERE_1_2, ERE_1_3]
# category 2
negate_SE_2 = [SE_2_2, SE_2_3, SE_2_0, SE_2_1, ERE_2_0, ERE_2_1, ERE_2_2, ERE_2_3]
# category 3
negate_SE_3 = [SE_3_4, SE_3_5, SE_3_6, SE_3_7, SE_3_0, SE_3_1, SE_3_2, SE_3_3,
               ERE_3_0, ERE_3_1, ERE_3_2, ERE_3_3, ERE_3_4, ERE_3_5, ERE_3_6, ERE_3_7]
# category 4
negate_SE_4 = [SE_4_1, SE_4_0, ERE_4_0, ERE_4_1]
# # category 5
# negate_SE_5 = [SE_5_1, SE_5_0, ERE_5_0, ERE_5_1]

# negate_SE_matrix = [negate_SE_0,
#                     negate_SE_1,
#                     negate_SE_2,
#                     negate_SE_3,
#                     negate_SE_4,
#                     negate_SE_5
#                     ]
negate_SE_matrix = [negate_SE_0,
                    negate_SE_1,
                    negate_SE_2,
                    negate_SE_3,
                    negate_SE_4
                    ]

# 2. negation of ERE expressions
# category 0
negate_ERE_0 = [SE_0_2, SE_0_3]
# category 1
negate_ERE_1 = [SE_1_4, SE_1_5, SE_1_6, SE_1_7]
# category 2
negate_ERE_2 = [SE_2_4, SE_2_5, SE_2_6, SE_2_7]
# category 3
negate_ERE_3 = [SE_3_8, SE_3_9, SE_3_10, SE_3_11, SE_3_12, SE_3_13, SE_3_14, SE_3_15]
# category 4
negate_ERE_4 = [SE_4_2, SE_4_3]
# # category 5
# negate_ERE_5 = [SE_5_2, SE_5_3]

# negate_ERE_matrix = [negate_ERE_0,
#                      negate_ERE_1,
#                      negate_ERE_2,
#                      negate_ERE_3,
#                      negate_ERE_4,
#                      negate_ERE_5
#                      ]

negate_ERE_matrix = [negate_ERE_0,
                     negate_ERE_1,
                     negate_ERE_2,
                     negate_ERE_3,
                     negate_ERE_4
                     ]