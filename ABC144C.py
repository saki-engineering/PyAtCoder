#coding: utf-8
import math
import heapq

MOD = 10**9+7

N = int(input())
r = math.ceil(math.sqrt(N))

ans = N-1
for i in range(1,r+1):
    if(N%i==0):
        q = N//i
        ans = min(ans, i+q-2)

print(ans)