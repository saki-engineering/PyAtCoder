#coding: utf-8
import math
import heapq
import bisect
#from scipy.misc import comb

MOD = 10**9+7

N,K = map(int, input().split())
A = list(map(int, input().split())) + [0]

ans = 0
sum = A[0]
l = 0
r = 0
while r < N:
    if sum < K:
        r += 1
        sum += A[r]
    else:
        ans += (N-r)
        l += 1
        sum -= A[l-1]

print(ans)