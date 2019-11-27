#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N = int(input())

# 複数個の数値を、intの配列として取得
H = list(map(int, input().split()))

ans=0
tmp=0
for i in range(1,N):
    if H[i]<=H[i-1]:
        tmp+=1
    else:
        ans=max(ans,tmp)
        tmp=0
ans=max(ans,tmp)

print(ans)