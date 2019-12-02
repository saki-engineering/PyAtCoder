#coding: utf-8
import math
import heapq
import bisect

MOD = 2019

L,R = map(int, input().split())

if R-L+1 >= MOD:
    ans=0
else:
    L = L%MOD
    R = R%MOD
    if R < L:
        ans=0
    else:
        ans=MOD
        for l in range(L,R):
            for r in range(l+1,R+1):
                ans=min(ans,l*r%MOD)

print(ans)