import numpy as np
import matplotlib
import pandas
import torch
import d2l
import tokenizers

import sys
print(sys.version)
for module in np, matplotlib, pandas, torch, d2l, tokenizers:
    print(module.__name__, module.__version__)