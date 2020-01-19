#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N,M = map(int, input().split())
X = list(map(int, input().split()))
X.sort()

Y = []
for i in range(M-1):
    Y.append(X[i+1]-X[i])
Y.sort()

ans = 0
if N < M:
    ans = sum(Y[:M-N])

print(ans)