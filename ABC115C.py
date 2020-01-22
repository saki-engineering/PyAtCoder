#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N,K = map(int, input().split())
H = []
for i in range(N):
    h = int(input())
    H.append(h)
H.sort()

ans = 10**9
for i in range(N-K+1):
    ans = min(ans,H[i+K-1]-H[i])

print(ans)