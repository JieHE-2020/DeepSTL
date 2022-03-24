import math

"""
Section 1: limit number
"""
# level 1
limit_num_atom = 1000
limit_num_bc_atom = 1000
# level 2
# tp - atom
limit_num_tp_atom_normal = 1000
# separation of 'until' and 'since' operator
# square root of limit_num_tp_atom_normal and round up to an integer
limit_num_tp_atom_until_since_first = limit_num_tp_atom_normal
limit_num_tp_atom_until_since_second = limit_num_tp_atom_normal
# for limit number of appositive and appendix
tp_atom_factor_simplest_normal = 2
limit_num_tp_atom_simplest_normal = limit_num_tp_atom_normal * tp_atom_factor_simplest_normal


"""
Section 2: probability in organization
"""
# when (limit number) / (overall number of combinations) is smaller than
# the below threshold probability, union operation is triggered. Otherwise,
# use for loop to organize translations.
union_operation_threshold_probability = 1/20


"""
Section 3: general probabilities
"""
# layer selection for TP
p_layer1 = 0.75
p_layer2 = 0.15
p_layer3 = 0.03
p_layer4 = 0.03
p_layer5 = 0.02
p_layer6 = 0.02
prob_tp_layer = [p_layer1, p_layer2, p_layer3, p_layer4, p_layer5, p_layer6]

"""
Section 4: hyper-parameters for generating signal names and mode names
"""
max_identifier_length = 10
alpha = 1.015

"""
Section 5: training sample generator
"""
max_try_times = 10

