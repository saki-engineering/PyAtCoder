#coding: utf-8
import math
import heapq
import bisect
#from scipy.misc import comb

MOD = 10**9+7

N,M = map(int, input().split())
A = []
for i in range(M):
    a = int(input())
    A.append(a)    

ans = [1,1]+[0]*(N-1)
for a in A:
    ans[a]=-1

for i in range(2,N+1):
    if ans[i]!=-1:
        if ans[i-2]!=-1:
            ans[i]=(ans[i]+ans[i-2])%MOD
        if ans[i-1]!=-1:
            ans[i]=(ans[i]+ans[i-1])%MOD

print(ans[N])
