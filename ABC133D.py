#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N = int(input())

# 複数個の数値を、intの配列として取得
A = list(map(int, input().split()))

B = [0]*N
for i in range(N):
    if i%2 == 0:
        B[0] += A[i]
    else:
        B[0] -= A[i]

for i in range(1,N):
    B[i] = 2*(A[i-1]-B[i-1]//2)

for b in B:
    print(b)