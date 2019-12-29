#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N,M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

L = []
for i in range(M):
    l = list(map(int, input().split()))
    L.append(l)
L = sorted(L, key=lambda x:-x[1])

ans = 0
index = 0
for i in range(N):
    if index >= M:
        ans += A[i]
    else:
        if A[i] >= L[index][1]:
            ans += A[i]
        else:
            ans += L[index][1]
            L[index][0] -= 1
            if L[index][0] == 0:
                index += 1

print(ans)