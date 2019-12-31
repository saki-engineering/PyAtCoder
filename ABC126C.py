#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N,K = map(int, input().split())

ans = 0
if N >= K:
    ans += (N-K+1)/N
    M = K-1
else:
    M = N
cnt = 1

while K>1:
    K = math.ceil(K/2)
    if K <= M:
        ans += (M-K+1)/((2**cnt)*N)
        M = K-1
        cnt += 1
    else:
        cnt += 1

print(ans)