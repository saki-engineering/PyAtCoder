#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N,M = map(int, input().split())
R = []
for i in range(M):
    a = tuple(map(int, input().split()))
    R.append(a)
R = sorted(R, key=lambda x:(x[1]))

ans = 0
brid = -1
for a,b in R:
    if a >= brid:
        brid = b
        ans += 1

print(ans)