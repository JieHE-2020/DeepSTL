"""
Grammar:

F -> always (CLAUSE -> CLAUSE) | always [a:b] (CLAUSE -> CLAUSE)  | always [a:b] (CE) | eventually [a:b] (SP)

CLAUSE -> TP | SP

TP ->  eventually (SP) | eventually [0:t] (SP) | eventually [a:b] (SP) |
       always (CE) | always [0:t] (CE) | always [a:b] (CE) |
       eventually (always (CE)) | eventually [0:t1] always [0:t2] (CE) | eventually [a:b] always [c:d] (CE) |
       (CE) until (SP) | (CE) until [0:t] (SP) | (CE) until [a:b] (SP) |
       once (SP) | once [0:t] (SP) | once [a:b] (SP) |
       historically (CE) | historically [0:t] (CE) | historically [a:b] (CE) |
       once (historically (CE)) | once [0:t1] historically [0:t2] (CE) | once [a:b] historically [c:d] (CE) |
       (CE) since (SP) | (CE) since [0:t] (SP) | (CE) since [a:b] (SP)

SP -> CE | ERE

CE -> SE

SE -> obj == x | not (obj == x) | not rise (obj == x) | not fall (obj == x) |   # category 0
      obj >=/> x | not (obj >=/> x) | not rise (obj >=/> x) | not fall (obj >=/> x) |   # category 1
      obj <=/< x | not (obj <=/< x) | not rise (obj <=/< x) | not fall (obj <=/< x) |   # category 2
      obj >= / > a and obj <= / < b | not (obj >= / > a and obj <= / < b) | not rise (obj >= / > a and obj <= / < b) | not fall (obj >= / > a and obj <= / < b) |   # category 3
      obj == m | not (obj==m) | not rise (obj == m) | not fall (obj == m) |   # category 4
      obj == m1 or obj == m2 | not (obj == m1 or obj == m2) | not rise (obj == m1 or obj == m2) | not fall (obj == m1 or obj == m2)    # category 5

ERE -> rise (obj == x) | fall (obj == x) |    # category 0
       rise (obj >=/> x) | fall (obj >=/> x) |    # category 1
       rise (obj <=/< x) | fall (obj <=/< x) |    # category 2
       rise (obj >= / > a and obj <= / < b) | fall (obj >= / > a and obj <= / < b) |   # category 3
       rise (obj == m) | fall (obj == m) |    # category 4
       rise (obj == m1 or obj == m2) | fall (obj == m1 or obj == m2)     # category 5

"""
