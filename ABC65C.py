#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
#from scipy.misc import comb

MOD = 10**9+7
N,M = map(int, input().split())

if abs(N-M) == 1:
    ans = (math.factorial(N)*math.factorial(M))%MOD
elif abs(N-M) == 0:
    ans = (2*math.factorial(N)*math.factorial(M))%MOD
else: ans = 0

print(ans)