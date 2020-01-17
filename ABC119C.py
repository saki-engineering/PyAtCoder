#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N,A,B,C = map(int, input().split())

L = []
for i in range(N):
    l = int(input())
    L.append(l)

ans = 10**9

for i in range(1<<(2*N)):
    a = b = c = 0
    tmp = 0
    for j in range(N):
        flg = 0
        if i&(1<<(2*j)):
            flg += 1
        if i&(1<<(2*j+1)):
            flg += 2

        if flg == 1:
            if a:
                tmp += 10
            a += L[j]
        elif flg == 2:
            if b:
                tmp += 10
            b += L[j]
        elif flg == 3:
            if c:
                tmp += 10
            c += L[j]

    if a*b*c==0:
        continue

    tmp += abs(A-a)+abs(B-b)+abs(C-c)
    ans = min(ans,tmp)

print(ans)
