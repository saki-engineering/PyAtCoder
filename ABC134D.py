#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N = int(input())
A = [0] + list(map(int, input().split()))

B = [0]*(N+1)
for i in reversed(range(1,N+1)):
    k = i
    cnt = 0
    while k <= N:
        cnt += B[k]
        k += i
    
    if cnt%2 != A[i]:
        B[i] = 1

print(sum(B))
for i in range(1,N+1):
    if B[i] == 1:
        print(i)