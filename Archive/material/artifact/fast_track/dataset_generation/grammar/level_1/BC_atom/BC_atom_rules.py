# Boolean Operation of Atom Expressions
# BC_Atom means Boolean Combination of Atom expressions
BC_Atom_0 = {
    'type': ['BC_Atom', 'A and B'],
    'index': 0,
    'ingredient': [{}, {}],
    'expression': 'SP_expr_1 and SP_expr_2',
    'probability': 0.6
}

BC_Atom_1 = {
    'type': ['BC_Atom', 'A or B'],
    'index': 1,
    'ingredient': [{}, {}],
    'expression': 'SP_expr_1 or SP_expr_2',
    'probability': 0.4
}

# BC_Atom_2 = {
#     'type': ['BC_Atom', 'A and B and C'],
#     'index': 2,
#     'ingredient': [{}, {}, {}],
#     'expression': 'SP_expr_1 and SP_expr_2 and SP_expr_3',
#     'probability': 0
# }
#
# BC_Atom_3 = {
#     'type': ['BC_Atom', 'A or B or C'],
#     'index': 3,
#     'ingredient': [{}, {}, {}],
#     'expression': 'SP_expr_1 or SP_expr_2 or SP_expr_3',
#     'probability': 0
# }

# BC_Atom = [BC_Atom_0, BC_Atom_1, BC_Atom_2, BC_Atom_3]
BC_Atom = [BC_Atom_0, BC_Atom_1]