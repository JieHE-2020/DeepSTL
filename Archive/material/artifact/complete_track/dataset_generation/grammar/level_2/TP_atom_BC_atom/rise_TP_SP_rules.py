# Temporal phrases modified by keyword 'rise'
# category 0 - eventually
rise_TP_0_0 = {'type': ['rise_TP', 'eventually'],
               'index': [0, 0],
               'ingredient': [{}],
               'expression': 'rise (eventually (SP_expr))',
               'probability': 1/3}

rise_TP_0_1 = {'type': ['rise_TP', 'eventually'],
               'index': [0, 1],
               'ingredient': [{}, 't_value'],
               'expression': 'rise (eventually [0:t_value] (SP_expr))',
               'probability': 1/3}

rise_TP_0_2 = {'type': ['rise_TP', 'eventually'],
               'index': [0, 2],
               'ingredient': [{}, 't_value_a', 't_value_b'],
               'expression': 'rise (eventually [t_value_a:t_value_b] (SP_expr))',
               'probability': 1/3}

# category 1 - always
rise_TP_1_0 = {'type': ['rise_TP', 'always'],
               'index': [1, 0],
               'ingredient': [{}],
               'expression': 'rise (always (SP_expr))',
               'probability': 1/3}

rise_TP_1_1 = {'type': ['rise_TP', 'always'],
               'index': [1, 1],
               'ingredient': [{}, 't_value'],
               'expression': 'rise (always [0:t_value] (SP_expr))',
               'probability': 1/3}

rise_TP_1_2 = {'type': ['rise_TP', 'always'],
               'index': [1, 2],
               'ingredient': [{}, 't_value_a', 't_value_b'],
               'expression': 'rise (always [t_value_a:t_value_b] (SP_expr))',
               'probability': 1/3}

# category 2 - once
rise_TP_2_0 = {'type': ['rise_TP', 'once'],
               'index': [2, 0],
               'ingredient': [{}],
               'expression': 'rise (once (SP_expr))',
               'probability': 1/3}

rise_TP_2_1 = {'type': ['rise_TP', 'once'],
               'index': [2, 1],
               'ingredient': [{}, 't_value'],
               'expression': 'rise (once [0:t_value] (SP_expr))',
               'probability': 1/3}

rise_TP_2_2 = {'type': ['rise_TP', 'once'],
               'index': [2, 2],
               'ingredient': [{}, 't_value_a', 't_value_b'],
               'expression': 'rise (once [t_value_a:t_value_b] (SP_expr))',
               'probability': 1/3}

# category 3 - historically
rise_TP_3_0 = {'type': ['rise_TP', 'historically'],
               'index': [3, 0],
               'ingredient': [{}],
               'expression': 'rise (historically (SP_expr))',
               'probability': 1/3}

rise_TP_3_1 = {'type': ['rise_TP', 'historically'],
               'index': [3, 1],
               'ingredient': [{}, 't_value'],
               'expression': 'rise (historically [0:t_value] (SP_expr))',
               'probability': 1/3}

rise_TP_3_2 = {'type': ['rise_TP', 'historically'],
               'index': [3, 2],
               'ingredient': [{}, 't_value_a', 't_value_b'],
               'expression': 'rise (historically [t_value_a:t_value_b] (SP_expr))',
               'probability': 1/3}

# category 4 - until
rise_TP_4_0 = {'type': ['rise_TP', 'until'],
               'index': [4, 0],
               'ingredient': [{}, {}],
               'expression': 'rise ((SP_expr_1) until (SP_expr_2))',
               'probability': 1/3}

rise_TP_4_1 = {'type': ['rise_TP', 'until'],
               'index': [4, 1],
               'ingredient': [{}, {}, 't_value'],
               'expression': 'rise ((SP_expr_1) until [0:t_value] (SP_expr_2))',
               'probability': 1/3}

rise_TP_4_2 = {'type': ['rise_TP', 'until'],
               'index': [4, 2],
               'ingredient': [{}, {}, 't_value_a', 't_value_b'],
               'expression': 'rise ((SP_expr_1) until [t_value_a:t_value_b] (SP_expr_2))',
               'probability': 1/3}

# category 5 - since
rise_TP_5_0 = {'type': ['rise_TP', 'since'],
               'index': [5, 0],
               'ingredient': [{}, {}],
               'expression': 'rise ((SP_expr_1) since (SP_expr_2))',
               'probability': 1/3}

rise_TP_5_1 = {'type': ['rise_TP', 'since'],
               'index': [5, 1],
               'ingredient': [{}, {}, 't_value'],
               'expression': 'rise ((SP_expr_1) since [0:t_value] (SP_expr_2))',
               'probability': 1/3}

rise_TP_5_2 = {'type': ['rise_TP', 'since'],
               'index': [5, 2],
               'ingredient': [{}, {}, 't_value_a', 't_value_b'],
               'expression': 'rise ((SP_expr_1) since [t_value_a:t_value_b] (SP_expr_2))',
               'probability': 1/3}

rise_TP = [[rise_TP_0_0, rise_TP_0_1, rise_TP_0_2],
           [rise_TP_1_0, rise_TP_1_1, rise_TP_1_2],
           [rise_TP_2_0, rise_TP_2_1, rise_TP_2_2],
           [rise_TP_3_0, rise_TP_3_1, rise_TP_3_2],
           [rise_TP_4_0, rise_TP_4_1, rise_TP_4_2],
           [rise_TP_5_0, rise_TP_5_1, rise_TP_5_2]
           ]
