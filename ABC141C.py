#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N,K,Q = map(int, input().split())

point = [K-Q]*N

for i in range(Q):
    a = int(input())
    point[a-1]+=1

for i in range(N):
    if point[i]>0:
        print("Yes")
    else:
        print("No")