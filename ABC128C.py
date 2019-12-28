#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N,M = map(int, input().split())

#S[i]は、電球iのスイッチ接続の様子
S = np.array([np.zeros(N,int) for _ in range(M)])
for i in range(M):
    L = list(map(int, input().split()))
    for j in range(L[0]):
        S[i][L[j+1]-1] = 1

P = list(map(int, input().split()))
ans = 0

for i in range(2**N):
    #Bはiの2進数表示
    B = np.zeros(N)
    for j in range(N):
        if (1<<j)&i != 0:
            B[j] = 1
    
    flg = 1
    for j in range(M):
        dot = np.dot(B,S[j])
        if dot%2 != P[j]:
            flg = 0
            break
    
    if flg:
        ans += 1

print(ans)