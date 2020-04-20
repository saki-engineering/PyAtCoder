#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
import itertools
#from scipy.misc import comb

S = input()
N = len(S)

ans = 0
for i in range(1<<(N-1)):
    func = S[0]
    for j in range(N-1):
        if (i>>j)&1:
            func += '+'
        func += S[j+1]
    ans += eval(func)

print(ans)