# Temporal Phrases
# category 0 - eventually
TP_0_0 = {'type': ['original_TP', 'eventually'],
          'index': [0, 0],
          'ingredient': [{}],
          'expression': 'eventually (SP_expr)',
          'probability': 0.25}

TP_0_1 = {'type': ['original_TP', 'eventually'],
          'index': [0, 1],
          'ingredient': [{}, 't_value'],
          'expression': 'eventually [0:t_value] (SP_expr)',
          'probability': 0.5}

TP_0_2 = {'type': ['original_TP', 'eventually'],
          'index': [0, 2],
          'ingredient': [{}, 't_value_a', 't_value_b'],
          'expression': 'eventually [t_value_a:t_value_b] (SP_expr)',
          'probability': 0.25}

# category 1 - always
TP_1_0 = {'type': ['original_TP', 'always'],
          'index': [1, 0],
          'ingredient': [{}],
          'expression': 'always (SP_expr)',
          'probability': 0.25}

TP_1_1 = {'type': ['original_TP', 'always'],
          'index': [1, 1],
          'ingredient': [{}, 't_value'],
          'expression': 'always [0:t_value] (SP_expr)',
          'probability': 0.5}

TP_1_2 = {'type': ['original_TP', 'always'],
          'index': [1, 2],
          'ingredient': [{}, 't_value_a', 't_value_b'],
          'expression': 'always [t_value_a:t_value_b] (SP_expr)',
          'probability': 0.25}

# category 2 - once
TP_2_0 = {'type': ['original_TP', 'once'],
          'index': [2, 0],
          'ingredient': [{}],
          'expression': 'once (SP_expr)',
          'probability': 0.25}

TP_2_1 = {'type': ['original_TP', 'once'],
          'index': [2, 1],
          'ingredient': [{}, 't_value'],
          'expression': 'once [0:t_value] (SP_expr)',
          'probability': 0.5}

TP_2_2 = {'type': ['original_TP', 'once'],
          'index': [2, 2],
          'ingredient': [{}, 't_value_a', 't_value_b'],
          'expression': 'once [t_value_a:t_value_b] (SP_expr)',
          'probability': 0.25}

# category 3 - historically
TP_3_0 = {'type': ['original_TP', 'historically'],
          'index': [3, 0],
          'ingredient': [{}],
          'expression': 'historically (SP_expr)',
          'probability': 0.25}

TP_3_1 = {'type': ['original_TP', 'historically'],
          'index': [3, 1],
          'ingredient': [{}, 't_value'],
          'expression': 'historically [0:t_value] (SP_expr)',
          'probability': 0.5}

TP_3_2 = {'type': ['original_TP', 'historically'],
          'index': [3, 2],
          'ingredient': [{}, 't_value_a', 't_value_b'],
          'expression': 'historically [t_value_a:t_value_b] (SP_expr)',
          'probability': 0.25}

# category 4 - until
TP_4_0 = {'type': ['original_TP', 'until'],
          'index': [4, 0],
          'ingredient': [{}, {}],
          'expression': '(SP_expr_1) until (SP_expr_2)',
          'probability': 0.25}

TP_4_1 = {'type': ['original_TP', 'until'],
          'index': [4, 1],
          'ingredient': [{}, {}, 't_value'],
          'expression': '(SP_expr_1) until [0:t_value] (SP_expr_2)',
          'probability': 0.5}

TP_4_2 = {'type': ['original_TP', 'until'],
          'index': [4, 2],
          'ingredient': [{}, {}, 't_value_a', 't_value_b'],
          'expression': '(SP_expr_1) until [t_value_a:t_value_b] (SP_expr_2)',
          'probability': 0.25}

# category 5 - since
TP_5_0 = {'type': ['original_TP', 'since'],
          'index': [5, 0],
          'ingredient': [{}, {}],
          'expression': '(SP_expr_1) since (SP_expr_2)',
          'probability': 0.25}

TP_5_1 = {'type': ['original_TP', 'since'],
          'index': [5, 1],
          'ingredient': [{}, {}, 't_value'],
          'expression': '(SP_expr_1) since [0:t_value] (SP_expr_2)',
          'probability': 0.5}

TP_5_2 = {'type': ['original_TP', 'since'],
          'index': [5, 2],
          'ingredient': [{}, {}, 't_value_a', 't_value_b'],
          'expression': '(SP_expr_1) since [t_value_a:t_value_b] (SP_expr_2)',
          'probability': 0.25}

TP = [[TP_0_0, TP_0_1, TP_0_2],
      [TP_1_0, TP_1_1, TP_1_2],
      [TP_2_0, TP_2_1, TP_2_2],
      [TP_3_0, TP_3_1, TP_3_2],
      [TP_4_0, TP_4_1, TP_4_2],
      [TP_5_0, TP_5_1, TP_5_2]
      ]
