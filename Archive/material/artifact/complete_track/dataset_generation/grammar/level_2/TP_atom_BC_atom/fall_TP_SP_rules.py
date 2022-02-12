# Temporal phrases modified by keyword 'fall'
# category 0 - eventually
fall_TP_0_0 = {'type': ['fall_TP', 'eventually'],
               'index': [0, 0],
               'ingredient': [{}],
               'expression': 'fall (eventually (SP_expr))',
               'probability': 1/3}

fall_TP_0_1 = {'type': ['fall_TP', 'eventually'],
               'index': [0, 1],
               'ingredient': [{}, 't_value'],
               'expression': 'fall (eventually [0:t_value] (SP_expr))',
               'probability': 1/3}

fall_TP_0_2 = {'type': ['fall_TP', 'eventually'],
               'index': [0, 2],
               'ingredient': [{}, 't_value_a', 't_value_b'],
               'expression': 'fall (eventually [t_value_a:t_value_b] (SP_expr))',
               'probability': 1/3}

# category 1 - always
fall_TP_1_0 = {'type': ['fall_TP', 'always'],
               'index': [1, 0],
               'ingredient': [{}],
               'expression': 'fall (always (SP_expr))',
               'probability': 1/3}

fall_TP_1_1 = {'type': ['fall_TP', 'always'],
               'index': [1, 1],
               'ingredient': [{}, 't_value'],
               'expression': 'fall (always [0:t_value] (SP_expr))',
               'probability': 1/3}

fall_TP_1_2 = {'type': ['fall_TP', 'always'],
               'index': [1, 2],
               'ingredient': [{}, 't_value_a', 't_value_b'],
               'expression': 'fall (always [t_value_a:t_value_b] (SP_expr))',
               'probability': 1/3}

# category 2 - once
fall_TP_2_0 = {'type': ['fall_TP', 'once'],
               'index': [2, 0],
               'ingredient': [{}],
               'expression': 'fall (once (SP_expr))',
               'probability': 1/3}

fall_TP_2_1 = {'type': ['fall_TP', 'once'],
               'index': [2, 1],
               'ingredient': [{}, 't_value'],
               'expression': 'fall (once [0:t_value] (SP_expr))',
               'probability': 1/3}

fall_TP_2_2 = {'type': ['fall_TP', 'once'],
               'index': [2, 2],
               'ingredient': [{}, 't_value_a', 't_value_b'],
               'expression': 'fall (once [t_value_a:t_value_b] (SP_expr))',
               'probability': 1/3}

# category 3 - historically
fall_TP_3_0 = {'type': ['fall_TP', 'historically'],
               'index': [3, 0],
               'ingredient': [{}],
               'expression': 'fall (historically (SP_expr))',
               'probability': 1/3}

fall_TP_3_1 = {'type': ['fall_TP', 'historically'],
               'index': [3, 1],
               'ingredient': [{}, 't_value'],
               'expression': 'fall (historically [0:t_value] (SP_expr))',
               'probability': 1/3}

fall_TP_3_2 = {'type': ['fall_TP', 'historically'],
               'index': [3, 2],
               'ingredient': [{}, 't_value_a', 't_value_b'],
               'expression': 'fall (historically [t_value_a:t_value_b] (SP_expr))',
               'probability': 1/3}

# category 4 - until
fall_TP_4_0 = {'type': ['fall_TP', 'until'],
               'index': [4, 0],
               'ingredient': [{}, {}],
               'expression': 'fall ((SP_expr_1) until (SP_expr_2))',
               'probability': 1/3}

fall_TP_4_1 = {'type': ['fall_TP', 'until'],
               'index': [4, 1],
               'ingredient': [{}, {}, 't_value'],
               'expression': 'fall ((SP_expr_1) until [0:t_value] (SP_expr_2))',
               'probability': 1/3}

fall_TP_4_2 = {'type': ['fall_TP', 'until'],
               'index': [4, 2],
               'ingredient': [{}, {}, 't_value_a', 't_value_b'],
               'expression': 'fall ((SP_expr_1) until [t_value_a:t_value_b] (SP_expr_2))',
               'probability': 1/3}

# category 5 - since
fall_TP_5_0 = {'type': ['fall_TP', 'since'],
               'index': [5, 0],
               'ingredient': [{}, {}],
               'expression': 'fall ((SP_expr_1) since (SP_expr_2))',
               'probability': 1/3}

fall_TP_5_1 = {'type': ['fall_TP', 'since'],
               'index': [5, 1],
               'ingredient': [{}, {}, 't_value'],
               'expression': 'fall ((SP_expr_1) since [0:t_value] (SP_expr_2))',
               'probability': 1/3}

fall_TP_5_2 = {'type': ['fall_TP', 'since'],
               'index': [5, 2],
               'ingredient': [{}, {}, 't_value_a', 't_value_b'],
               'expression': 'fall ((SP_expr_1) since [t_value_a:t_value_b] (SP_expr_2))',
               'probability': 1/3}

fall_TP = [[fall_TP_0_0, fall_TP_0_1, fall_TP_0_2],
           [fall_TP_1_0, fall_TP_1_1, fall_TP_1_2],
           [fall_TP_2_0, fall_TP_2_1, fall_TP_2_2],
           [fall_TP_3_0, fall_TP_3_1, fall_TP_3_2],
           [fall_TP_4_0, fall_TP_4_1, fall_TP_4_2],
           [fall_TP_5_0, fall_TP_5_1, fall_TP_5_2]
           ]
