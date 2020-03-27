#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
#from scipy.misc import comb

N = int(input())
S = input()

x = 0
d = 0
for s in S:
    if s == '(': d += 1
    else: d -= 1

    x = min(x,d)

ans = '('*(-x) + S + ')'*(d-x)
print(ans)