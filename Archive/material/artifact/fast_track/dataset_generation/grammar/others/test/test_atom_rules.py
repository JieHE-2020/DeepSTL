from grammar import atom_rules


# unit test of SE
class ProbError(ValueError):
    pass


for i in range(len(atom_rules.SE)):
    sum_prob = 0
    for j in range(len(atom_rules.SE[i])):
        sum_prob = sum_prob + atom_rules.SE[i][j]['probability']
    if abs(sum_prob - 1) > 1e-10:
        raise ProbError('Invalid probability in category %d' % i)
print('SE unit test passed.')


# unit test of ERE
class ProbError(ValueError):
    pass


for i in range(len(atom_rules.ERE)):
    sum_prob = 0
    for j in range(len(atom_rules.ERE[i])):
        sum_prob = sum_prob + atom_rules.ERE[i][j]['probability']
    if abs(sum_prob - 1) > 1e-10:
        raise ProbError('Invalid probability in category %d' % i)
print('ERE unit test passed.')