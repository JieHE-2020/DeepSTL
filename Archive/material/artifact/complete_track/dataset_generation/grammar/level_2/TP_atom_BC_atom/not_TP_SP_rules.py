from grammar.level_2.TP_atom_BC_atom import original_TP_SP_rules

# Negation of temporal phrases
# category 0 - eventually
not_TP_0_0 = {'type': ['not_TP', 'eventually'],
              'index': [0, 0],
              'ingredient': [{}],
              'expression': 'not (eventually (SP_expr))',
              'probability': 0.25}

not_TP_0_1 = {'type': ['not_TP', 'eventually'],
              'index': [0, 1],
              'ingredient': [{}, 't_value'],
              'expression': 'not (eventually [0:t_value] (SP_expr))',
              'probability': 0.5}

not_TP_0_2 = {'type': ['not_TP', 'eventually'],
              'index': [0, 2],
              'ingredient': [{}, 't_value_a', 't_value_b'],
              'expression': 'not (eventually [t_value_a:t_value_b] (SP_expr))',
              'probability': 0.25}

# category 1 - always
not_TP_1_0 = {'type': ['not_TP', 'always'],
              'index': [1, 0],
              'ingredient': [{}],
              'expression': 'not (always (SP_expr))',
              'probability': 0.25}

not_TP_1_1 = {'type': ['not_TP', 'always'],
              'index': [1, 1],
              'ingredient': [{}, 't_value'],
              'expression': 'not (always [0:t_value] (SP_expr))',
              'probability': 0.5}

not_TP_1_2 = {'type': ['not_TP', 'always'],
              'index': [1, 2],
              'ingredient': [{}, 't_value_a', 't_value_b'],
              'expression': 'not (always [t_value_a:t_value_b] (SP_expr))',
              'probability': 0.25}

# category 2 - once
not_TP_2_0 = {'type': ['not_TP', 'once'],
              'index': [2, 0],
              'ingredient': [{}],
              'expression': 'not (once (SP_expr))',
              'probability': 0.25}

not_TP_2_1 = {'type': ['not_TP', 'once'],
              'index': [2, 1],
              'ingredient': [{}, 't_value'],
              'expression': 'not (once [0:t_value] (SP_expr))',
              'probability': 0.5}

not_TP_2_2 = {'type': ['not_TP', 'once'],
              'index': [2, 2],
              'ingredient': [{}, 't_value_a', 't_value_b'],
              'expression': 'not (once [t_value_a:t_value_b] (SP_expr))',
              'probability': 0.25}

# category 3 - historically
not_TP_3_0 = {'type': ['not_TP', 'historically'],
              'index': [3, 0],
              'ingredient': [{}],
              'expression': 'not (historically (SP_expr))',
              'probability': 0.25}

not_TP_3_1 = {'type': ['not_TP', 'historically'],
              'index': [3, 1],
              'ingredient': [{}, 't_value'],
              'expression': 'not (historically [0:t_value] (SP_expr))',
              'probability': 0.5}

not_TP_3_2 = {'type': ['not_TP', 'historically'],
              'index': [3, 2],
              'ingredient': [{}, 't_value_a', 't_value_b'],
              'expression': 'not (historically [t_value_a:t_value_b] (SP_expr))',
              'probability': 0.25}

# category 4 - until
not_TP_4_0 = {'type': ['not_TP', 'until'],
              'index': [4, 0],
              'ingredient': [{}, {}],
              'expression': 'not ((SP_expr_1) until (SP_expr_2))',
              'probability': 1/3}

not_TP_4_1 = {'type': ['not_TP', 'until'],
              'index': [4, 1],
              'ingredient': [{}, {}, 't_value'],
              'expression': 'not ((SP_expr_1) until [0:t_value] (SP_expr_2))',
              'probability': 1/3}

not_TP_4_2 = {'type': ['not_TP', 'until'],
              'index': [4, 2],
              'ingredient': [{}, {}, 't_value_a', 't_value_b'],
              'expression': 'not ((SP_expr_1) until [t_value_a:t_value_b] (SP_expr_2))',
              'probability': 1/3}

# category 5 - since
not_TP_5_0 = {'type': ['not_TP', 'since'],
              'index': [5, 0],
              'ingredient': [{}, {}],
              'expression': 'not ((SP_expr_1) since (SP_expr_2))',
              'probability': 1/3}

not_TP_5_1 = {'type': ['not_TP', 'since'],
              'index': [5, 1],
              'ingredient': [{}, {}, 't_value'],
              'expression': 'not ((SP_expr_1) since [0:t_value] (SP_expr_2))',
              'probability': 1/3}

not_TP_5_2 = {'type': ['not_TP', 'since'],
              'index': [5, 2],
              'ingredient': [{}, {}, 't_value_a', 't_value_b'],
              'expression': 'not ((SP_expr_1) since [t_value_a:t_value_b] (SP_expr_2))',
              'probability': 1/3}

not_TP = [[not_TP_0_0, not_TP_0_1, not_TP_0_2],
          [not_TP_1_0, not_TP_1_1, not_TP_1_2],
          [not_TP_2_0, not_TP_2_1, not_TP_2_2],
          [not_TP_3_0, not_TP_3_1, not_TP_3_2],
          [not_TP_4_0, not_TP_4_1, not_TP_4_2],
          [not_TP_5_0, not_TP_5_1, not_TP_5_2]
          ]


# Group 1: negation of 'eventually' operator
negate_eventually = [original_TP_SP_rules.TP_1_0, original_TP_SP_rules.TP_1_1, original_TP_SP_rules.TP_1_2]
# Group 2: negation of 'always' operator
negate_always = [original_TP_SP_rules.TP_0_0, original_TP_SP_rules.TP_0_1, original_TP_SP_rules.TP_0_2]
# Group 3: negation of 'once' operator
negate_once = [original_TP_SP_rules.TP_3_0, original_TP_SP_rules.TP_3_1, original_TP_SP_rules.TP_3_2]
# Group 4: negation of 'historically' operator
negate_historically = [original_TP_SP_rules.TP_2_0, original_TP_SP_rules.TP_2_1, original_TP_SP_rules.TP_2_2]

negate_TP_matrix = [negate_eventually,
                    negate_always,
                    negate_once,
                    negate_historically
                    ]

# print(negate_TP_matrix[0][1])
