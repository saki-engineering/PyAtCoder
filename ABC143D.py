#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for a in range(N-2):
    for b in range(a+1,N-1):
        c = bisect.bisect_left(L,L[a]+L[b])
        ans += c-b-1
            
print(ans)