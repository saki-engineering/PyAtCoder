#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
A = list(map(int, input().split()))

ans = 2*(10**9)
S = sum(A)

x = 0
for i in range(N-1):
    x += A[i]
    y = S - x
    ans = min(ans, abs(x-y))

print(ans)