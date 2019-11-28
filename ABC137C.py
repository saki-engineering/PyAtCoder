#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N = int(input())

D = dict()
for i in range(N):
    a = input()
    a = ''.join(sorted(a))
    if a in D:
        D[a] = D[a]+1
    else:
        D[a] = 1

ans = 0
for i in D:
    ans += D[i]*(D[i]-1)//2

print(ans)