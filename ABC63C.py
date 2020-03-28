#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
#from scipy.misc import comb

N = int(input())
S = []

for _ in range(N):
    s = int(input())
    S.append(s)

S.sort()

A = sum(S)
B = 0
for s in S:
    if s%10:
        B = s
        break

if A%10:
    print(A)
else:
    if B:
        print(A-B)
    else:
        print(0)