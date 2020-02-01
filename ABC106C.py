#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

S = input()
K = int(input())

cnt_1 = 0
for s in S:
    if s=="1":
        cnt_1 += 1
    else:
        break

if cnt_1>=K:
    print(1)
else:
    print(S[cnt_1])