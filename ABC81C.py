#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N,K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

B = list(Counter(A).values())
B.sort()

ans = 0
for i in range(len(B)-K):
    ans += B[i]

print(ans)