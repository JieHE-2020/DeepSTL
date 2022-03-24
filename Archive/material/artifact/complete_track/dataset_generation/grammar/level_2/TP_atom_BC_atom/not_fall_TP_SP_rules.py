# Temporal phrases modified by keyword 'not fall'
# category 0 - eventually
not_fall_TP_0_0 = {'type': ['not_fall_TP', 'eventually'],
                   'index': [0, 0],
                   'ingredient': [{}],
                   'expression': 'not fall (eventually (SP_expr))',
                   'probability': 1/3}

not_fall_TP_0_1 = {'type': ['not_fall_TP', 'eventually'],
                   'index': [0, 1],
                   'ingredient': [{}, 't_value'],
                   'expression': 'not fall (eventually [0:t_value] (SP_expr))',
                   'probability': 1/3}

not_fall_TP_0_2 = {'type': ['not_fall_TP', 'eventually'],
                   'index': [0, 2],
                   'ingredient': [{}, 't_value_a', 't_value_b'],
                   'expression': 'not fall (eventually [t_value_a:t_value_b] (SP_expr))',
                   'probability': 1/3}

# category 1 - always
not_fall_TP_1_0 = {'type': ['not_fall_TP', 'always'],
                   'index': [1, 0],
                   'ingredient': [{}],
                   'expression': 'not fall (always (SP_expr))',
                   'probability': 1/3}

not_fall_TP_1_1 = {'type': ['not_fall_TP', 'always'],
                   'index': [1, 1],
                   'ingredient': [{}, 't_value'],
                   'expression': 'not fall (always [0:t_value] (SP_expr))',
                   'probability': 1/3}

not_fall_TP_1_2 = {'type': ['not_fall_TP', 'always'],
                   'index': [1, 2],
                   'ingredient': [{}, 't_value_a', 't_value_b'],
                   'expression': 'not fall (always [t_value_a:t_value_b] (SP_expr))',
                   'probability': 1/3}

# category 2 - once
not_fall_TP_2_0 = {'type': ['not_fall_TP', 'once'],
                   'index': [2, 0],
                   'ingredient': [{}],
                   'expression': 'not fall (once (SP_expr))',
                   'probability': 1/3}

not_fall_TP_2_1 = {'type': ['not_fall_TP', 'once'],
                   'index': [2, 1],
                   'ingredient': [{}, 't_value'],
                   'expression': 'not fall (once [0:t_value] (SP_expr))',
                   'probability': 1/3}

not_fall_TP_2_2 = {'type': ['not_fall_TP', 'once'],
                   'index': [2, 2],
                   'ingredient': [{}, 't_value_a', 't_value_b'],
                   'expression': 'not fall (once [t_value_a:t_value_b] (SP_expr))',
                   'probability': 1/3}

# category 3 - historically
not_fall_TP_3_0 = {'type': ['not_fall_TP', 'historically'],
                   'index': [3, 0],
                   'ingredient': [{}],
                   'expression': 'not fall (historically (SP_expr))',
                   'probability': 1/3}

not_fall_TP_3_1 = {'type': ['not_fall_TP', 'historically'],
                   'index': [3, 1],
                   'ingredient': [{}, 't_value'],
                   'expression': 'not fall (historically [0:t_value] (SP_expr))',
                   'probability': 1/3}

not_fall_TP_3_2 = {'type': ['not_fall_TP', 'historically'],
                   'index': [3, 2],
                   'ingredient': [{}, 't_value_a', 't_value_b'],
                   'expression': 'not fall (historically [t_value_a:t_value_b] (SP_expr))',
                   'probability': 1/3}

# category 4 - until
not_fall_TP_4_0 = {'type': ['not_fall_TP', 'until'],
                   'index': [4, 0],
                   'ingredient': [{}, {}],
                   'expression': 'not fall ((SP_expr_1) until (SP_expr_2))',
                   'probability': 1/3}

not_fall_TP_4_1 = {'type': ['not_fall_TP', 'until'],
                   'index': [4, 1],
                   'ingredient': [{}, {}, 't_value'],
                   'expression': 'not fall ((SP_expr_1) until [0:t_value] (SP_expr_2))',
                   'probability': 1/3}

not_fall_TP_4_2 = {'type': ['not_fall_TP', 'until'],
                   'index': [4, 2],
                   'ingredient': [{}, {}, 't_value_a', 't_value_b'],
                   'expression': 'not fall ((SP_expr_1) until [t_value_a:t_value_b] (SP_expr_2))',
                   'probability': 1/3}

# category 5 - since
not_fall_TP_5_0 = {'type': ['not_fall_TP', 'since'],
                   'index': [5, 0],
                   'ingredient': [{}, {}],
                   'expression': 'not fall ((SP_expr_1) since (SP_expr_2))',
                   'probability': 1/3}

not_fall_TP_5_1 = {'type': ['not_fall_TP', 'since'],
                   'index': [5, 1],
                   'ingredient': [{}, {}, 't_value'],
                   'expression': 'not fall ((SP_expr_1) since [0:t_value] (SP_expr_2))',
                   'probability': 1/3}

not_fall_TP_5_2 = {'type': ['not_fall_TP', 'since'],
                   'index': [5, 2],
                   'ingredient': [{}, {}, 't_value_a', 't_value_b'],
                   'expression': 'not fall ((SP_expr_1) since [t_value_a:t_value_b] (SP_expr_2))',
                   'probability': 1/3}

not_fall_TP = [[not_fall_TP_0_0, not_fall_TP_0_1, not_fall_TP_0_2],
               [not_fall_TP_1_0, not_fall_TP_1_1, not_fall_TP_1_2],
               [not_fall_TP_2_0, not_fall_TP_2_1, not_fall_TP_2_2],
               [not_fall_TP_3_0, not_fall_TP_3_1, not_fall_TP_3_2],
               [not_fall_TP_4_0, not_fall_TP_4_1, not_fall_TP_4_2],
               [not_fall_TP_5_0, not_fall_TP_5_1, not_fall_TP_5_2]
               ]
