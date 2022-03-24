# Temporal phrases modified by keyword 'not rise'
# category 0 - eventually
not_rise_TP_0_0 = {'type': ['not_rise_TP', 'eventually'],
                   'index': [0, 0],
                   'ingredient': [{}],
                   'expression': 'not rise (eventually (SP_expr))',
                   'probability': 1/3}

not_rise_TP_0_1 = {'type': ['not_rise_TP', 'eventually'],
                   'index': [0, 1],
                   'ingredient': [{}, 't_value'],
                   'expression': 'not rise (eventually [0:t_value] (SP_expr))',
                   'probability': 1/3}

not_rise_TP_0_2 = {'type': ['not_rise_TP', 'eventually'],
                   'index': [0, 2],
                   'ingredient': [{}, 't_value_a', 't_value_b'],
                   'expression': 'not rise (eventually [t_value_a:t_value_b] (SP_expr))',
                   'probability': 1/3}

# category 1 - always
not_rise_TP_1_0 = {'type': ['not_rise_TP', 'always'],
                   'index': [1, 0],
                   'ingredient': [{}],
                   'expression': 'not rise (always (SP_expr))',
                   'probability': 1/3}

not_rise_TP_1_1 = {'type': ['not_rise_TP', 'always'],
                   'index': [1, 1],
                   'ingredient': [{}, 't_value'],
                   'expression': 'not rise (always [0:t_value] (SP_expr))',
                   'probability': 1/3}

not_rise_TP_1_2 = {'type': ['not_rise_TP', 'always'],
                   'index': [1, 2],
                   'ingredient': [{}, 't_value_a', 't_value_b'],
                   'expression': 'not rise (always [t_value_a:t_value_b] (SP_expr))',
                   'probability': 1/3}

# category 2 - once
not_rise_TP_2_0 = {'type': ['not_rise_TP', 'once'],
                   'index': [2, 0],
                   'ingredient': [{}],
                   'expression': 'not rise (once (SP_expr))',
                   'probability': 1/3}

not_rise_TP_2_1 = {'type': ['not_rise_TP', 'once'],
                   'index': [2, 1],
                   'ingredient': [{}, 't_value'],
                   'expression': 'not rise (once [0:t_value] (SP_expr))',
                   'probability': 1/3}

not_rise_TP_2_2 = {'type': ['not_rise_TP', 'once'],
                   'index': [2, 2],
                   'ingredient': [{}, 't_value_a', 't_value_b'],
                   'expression': 'not rise (once [t_value_a:t_value_b] (SP_expr))',
                   'probability': 1/3}

# category 3 - historically
not_rise_TP_3_0 = {'type': ['not_rise_TP', 'historically'],
                   'index': [3, 0],
                   'ingredient': [{}],
                   'expression': 'not rise (historically (SP_expr))',
                   'probability': 1/3}

not_rise_TP_3_1 = {'type': ['not_rise_TP', 'historically'],
                   'index': [3, 1],
                   'ingredient': [{}, 't_value'],
                   'expression': 'not rise (historically [0:t_value] (SP_expr))',
                   'probability': 1/3}

not_rise_TP_3_2 = {'type': ['not_rise_TP', 'historically'],
                   'index': [3, 2],
                   'ingredient': [{}, 't_value_a', 't_value_b'],
                   'expression': 'not rise (historically [t_value_a:t_value_b] (SP_expr))',
                   'probability': 1/3}

# category 4 - until
not_rise_TP_4_0 = {'type': ['not_rise_TP', 'until'],
                   'index': [4, 0],
                   'ingredient': [{}, {}],
                   'expression': 'not rise ((SP_expr_1) until (SP_expr_2))',
                   'probability': 1/3}

not_rise_TP_4_1 = {'type': ['not_rise_TP', 'until'],
                   'index': [4, 1],
                   'ingredient': [{}, {}, 't_value'],
                   'expression': 'not rise ((SP_expr_1) until [0:t_value] (SP_expr_2))',
                   'probability': 1/3}

not_rise_TP_4_2 = {'type': ['not_rise_TP', 'until'],
                   'index': [4, 2],
                   'ingredient': [{}, {}, 't_value_a', 't_value_b'],
                   'expression': 'not rise ((SP_expr_1) until [t_value_a:t_value_b] (SP_expr_2))',
                   'probability': 1/3}

# category 5 - since
not_rise_TP_5_0 = {'type': ['not_rise_TP', 'since'],
                   'index': [5, 0],
                   'ingredient': [{}, {}],
                   'expression': 'not rise ((SP_expr_1) since (SP_expr_2))',
                   'probability': 1/3}

not_rise_TP_5_1 = {'type': ['not_rise_TP', 'since'],
                   'index': [5, 1],
                   'ingredient': [{}, {}, 't_value'],
                   'expression': 'not rise ((SP_expr_1) since [0:t_value] (SP_expr_2))',
                   'probability': 1/3}

not_rise_TP_5_2 = {'type': ['not_rise_TP', 'since'],
                   'index': [5, 2],
                   'ingredient': [{}, {}, 't_value_a', 't_value_b'],
                   'expression': 'not rise ((SP_expr_1) since [t_value_a:t_value_b] (SP_expr_2))',
                   'probability': 1/3}

not_rise_TP = [[not_rise_TP_0_0, not_rise_TP_0_1, not_rise_TP_0_2],
               [not_rise_TP_1_0, not_rise_TP_1_1, not_rise_TP_1_2],
               [not_rise_TP_2_0, not_rise_TP_2_1, not_rise_TP_2_2],
               [not_rise_TP_3_0, not_rise_TP_3_1, not_rise_TP_3_2],
               [not_rise_TP_4_0, not_rise_TP_4_1, not_rise_TP_4_2],
               [not_rise_TP_5_0, not_rise_TP_5_1, not_rise_TP_5_2]
               ]
