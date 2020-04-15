#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
import itertools
#from scipy.misc import comb

N,x = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    sumc = A[i]+A[i+1]
    if sumc > x:
        ans += (sumc-x)
        A[i+1] = max(A[i+1]-(sumc-x), 0)

print(ans)