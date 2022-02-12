import random
import numpy as np

seed = 100
np.random.seed(seed)
random.seed(seed)

import time
from console.training_sample_generator import TrainingSampleGenerator

# number of formulas
formula_num = 24000
# number of different translations for a single formula
limit_num_formula = 5
# number of different translations for a single clause
limit_num_clause = 100

if __name__ == '__main__':
    tic = time.time()
    for i in range(formula_num):
        training_sample_generator = TrainingSampleGenerator(limit_num_formula, limit_num_clause)
        print('%d: %s' % (i + 1, training_sample_generator.formula_expression))
        # count = 1
        # for eng in training_sample_generator.formula_translations:
        #     print('%d: %s' % (count, eng))
        #     count = count + 1

    toc = time.time()
    print('Time:' + str((toc - tic)) + 's')
