#coding: utf-8
import math
import heapq
import bisect
#from scipy.misc import comb

MOD = 10**9+7

N = int(input())

A = []
for i in range(N):
    a = tuple(map(int, input().split()))
    A.append(a)
A = sorted(A,key=lambda x:x[1])

t = 0
for a in A:
    if a[0]+t <= a[1]:
        t += a[0]
    else:
        print("No")
        exit()

print("Yes")