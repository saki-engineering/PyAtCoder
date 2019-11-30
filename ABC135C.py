#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N = int(input())

# 複数個の数値を、intの配列として取得
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans+=min(A[i],B[i])
    B[i]=max(0,B[i]-A[i])
    ans+=min(A[i+1],B[i])
    A[i+1]=max(0,A[i+1]-B[i])

print(ans)