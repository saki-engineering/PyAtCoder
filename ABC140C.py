#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N = int(input())

# 複数個の数値を、intの配列として取得
B = list(map(int, input().split()))

ans=B[0]+B[N-2]
for i in range(N-2):
    ans+=min(B[i],B[i+1])

print(ans)