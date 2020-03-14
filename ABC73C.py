#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
A = []
for _ in range(N):
    a = int(input())
    A.append(a)
A.sort()

ans = 0
for v in Counter(A).values():
    if v%2: ans += 1

print(ans)