#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())

ans = [N]*(N+1)
ans[0] = 0

for i in range(1,N+1):
    c6 = 1
    while c6 <= i:
        ans[i] = min(ans[i], ans[i-c6]+1)
        c6 *= 6
    c9 = 1
    while c9 <= i:
        ans[i] = min(ans[i], ans[i-c9]+1)
        c9 *= 9

print(ans[N])