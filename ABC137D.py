#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N,M = map(int, input().split())

A = []
for i in range(N):
    a,b = map(int, input().split())
    A.append((-b,a))
A = sorted(A,key=lambda x:(-x[1], -x[0]))
#この時点で、Aは(-報酬,日付)のタプルで、(-報酬)降順→日付降順になっている

H = []
heapq.heapify(H)
ans = 0

for i in range(1,M+1):
    while A and A[-1][1]<=i:
        data = A.pop()
        heapq.heappush(H,data)
    if H:
        ans += -(heapq.heappop(H)[0])

print(ans)