# Nested Temporal Phrases
# category 0 - eventually always
NTP_0_0 = {'type': ['original_NTP', 'eventually_always'],
           'index': [0, 0],
           'TP_template_index': [[0, 0], [1, 0]],
           'ingredient': [{}],
           'expression': 'eventually (always (SP_expr))',
           'probability': 1 / 2 / 8}

NTP_0_1 = {'type': ['original_NTP', 'eventually_always'],
           'index': [0, 1],
           'TP_template_index': [[0, 0], [1, 1]],
           'ingredient': [{}, 't_value_21'],
           'expression': 'eventually (always [0:t_value_21] (SP_expr))',
           'probability': 1 / 2 / 8}

NTP_0_2 = {'type': ['original_TP', 'eventually_always'],
           'index': [0, 2],
           'TP_template_index': [[0, 0], [1, 2]],
           'ingredient': [{}, 't_value_21', 't_value_22'],
           'expression': 'eventually (always [t_value_21:t_value_22] (SP_expr))',
           'probability': 1 / 2 / 8}

NTP_0_3 = {'type': ['original_NTP', 'eventually_always'],
           'index': [0, 3],
           'TP_template_index': [[0, 1], [1, 0]],
           'ingredient': [{}, 't_value_11'],
           'expression': 'eventually [0:t_value_11] (always (SP_expr))',
           'probability': 1 / 2 / 8}

NTP_0_4 = {'type': ['original_NTP', 'eventually_always'],
           'index': [0, 4],
           'TP_template_index': [[0, 1], [1, 1]],
           'ingredient': [{}, 't_value_11', 't_value_21'],
           'expression': 'eventually [0:t_value_11] (always [0:t_value_21] (SP_expr))',
           'probability': 1 / 2}

NTP_0_5 = {'type': ['original_NTP', 'eventually_always'],
           'index': [0, 5],
           'TP_template_index': [[0, 1], [1, 2]],
           'ingredient': [{}, 't_value_11', 't_value_21', 't_value_22'],
           'expression': 'eventually [0:t_value_11] (always [t_value_21:t_value_22] (SP_expr))',
           'probability': 1 / 2 / 8}

NTP_0_6 = {'type': ['original_NTP', 'eventually_always'],
           'index': [0, 6],
           'TP_template_index': [[0, 2], [1, 0]],
           'ingredient': [{}, 't_value_11', 't_value_12'],
           'expression': 'eventually [t_value_11:t_value_12] (always (SP_expr))',
           'probability': 1 / 2 / 8}

NTP_0_7 = {'type': ['original_NTP', 'eventually_always'],
           'index': [0, 7],
           'TP_template_index': [[0, 2], [1, 1]],
           'ingredient': [{}, 't_value_11', 't_value_12', 't_value_21'],
           'expression': 'eventually [t_value_11:t_value_12] (always [0:t_value_21] (SP_expr))',
           'probability': 1 / 2 / 8}

NTP_0_8 = {'type': ['original_TP', 'eventually_always'],
           'index': [0, 8],
           'TP_template_index': [[0, 2], [1, 2]],
           'ingredient': [{}, 't_value_11', 't_value_12', 't_value_21', 't_value_22'],
           'expression': 'eventually [t_value_11:t_value_12] (always [t_value_21:t_value_22] (SP_expr))',
           'probability': 1 / 2 / 8}

# category 1 - always eventually
NTP_1_0 = {'type': ['original_NTP', 'always_eventually'],
           'index': [1, 0],
           'TP_template_index': [[1, 0], [0, 0]],
           'ingredient': [{}],
           'expression': 'always (eventually (SP_expr))',
           'probability': 1 / 2 / 8}

NTP_1_1 = {'type': ['original_NTP', 'always_eventually'],
           'index': [1, 1],
           'TP_template_index': [[1, 0], [0, 1]],
           'ingredient': [{}, 't_value_21'],
           'expression': 'always (eventually [0:t_value_21] (SP_expr))',
           'probability': 1 / 2 / 8}

NTP_1_2 = {'type': ['original_TP', 'always_eventually'],
           'index': [1, 2],
           'TP_template_index': [[1, 0], [0, 2]],
           'ingredient': [{}, 't_value_21', 't_value_22'],
           'expression': 'always (eventually [t_value_21:t_value_22] (SP_expr))',
           'probability': 1 / 2 / 8}

NTP_1_3 = {'type': ['original_NTP', 'always_eventually'],
           'index': [1, 3],
           'TP_template_index': [[1, 1], [0, 0]],
           'ingredient': [{}, 't_value_11'],
           'expression': 'always [0:t_value_11] (eventually (SP_expr))',
           'probability': 1 / 2 / 8}

NTP_1_4 = {'type': ['original_NTP', 'always_eventually'],
           'index': [1, 4],
           'TP_template_index': [[1, 1], [0, 1]],
           'ingredient': [{}, 't_value_11', 't_value_21'],
           'expression': 'always [0:t_value_11] (eventually [0:t_value_21] (SP_expr))',
           'probability': 1 / 2}

NTP_1_5 = {'type': ['original_NTP', 'always_eventually'],
           'index': [1, 5],
           'TP_template_index': [[1, 1], [0, 2]],
           'ingredient': [{}, 't_value_11', 't_value_21', 't_value_22'],
           'expression': 'always [0:t_value_11] (eventually [t_value_21:t_value_22] (SP_expr))',
           'probability': 1 / 2 / 8}

NTP_1_6 = {'type': ['original_NTP', 'always_eventually'],
           'index': [1, 6],
           'TP_template_index': [[1, 2], [0, 0]],
           'ingredient': [{}, 't_value_11', 't_value_12'],
           'expression': 'always [t_value_11:t_value_12] (eventually (SP_expr))',
           'probability': 1 / 2 / 8}

NTP_1_7 = {'type': ['original_NTP', 'always_eventually'],
           'index': [1, 7],
           'TP_template_index': [[1, 2], [0, 1]],
           'ingredient': [{}, 't_value_11', 't_value_12', 't_value_21'],
           'expression': 'always [t_value_11:t_value_12] (eventually [0:t_value_21] (SP_expr))',
           'probability': 1 / 2 / 8}

NTP_1_8 = {'type': ['original_TP', 'always_eventually'],
           'index': [1, 8],
           'TP_template_index': [[1, 2], [0, 2]],
           'ingredient': [{}, 't_value_11', 't_value_12', 't_value_21', 't_value_22'],
           'expression': 'always [t_value_11:t_value_12] (eventually [t_value_21:t_value_22] (SP_expr))',
           'probability': 1 / 2 / 8}

NTP = [[NTP_0_0, NTP_0_1, NTP_0_2,
        NTP_0_3, NTP_0_4, NTP_0_5,
        NTP_0_6, NTP_0_7, NTP_0_8],
       [NTP_1_0, NTP_1_1, NTP_1_2,
        NTP_1_3, NTP_1_4, NTP_1_5,
        NTP_1_6, NTP_1_7, NTP_1_8]
       ]
