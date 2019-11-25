#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N,M = map(int, input().split())

# 複数個の数値を、intの配列として取得
A = list(map(int, input().split()))
A = list(map(lambda x: x * (-1),A))

heapq.heapify(A)
for i in range(M):
    x = heapq.heappop(A)
    heapq.heappush(A,x/2)

ans=0
for a in A:
    ans+=math.floor(-a)

print(ans)