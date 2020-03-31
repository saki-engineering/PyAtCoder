#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
#from scipy.misc import comb

N,T = map(int, input().split())
t = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    if t[i+1] < t[i]+T: ans += (t[i+1]-t[i])
    else: ans += T
ans += T

print(ans)