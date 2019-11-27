#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N = int(input())

# 複数個の数値を、intの配列として取得
v = list(map(int, input().split()))

heapq.heapify(v)
ans = heapq.heappop(v)
for i in range(1,N):
    ans += heapq.heappop(v)
    ans /= 2

print(ans)