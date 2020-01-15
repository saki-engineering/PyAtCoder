#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N,M = map(int, input().split())

# (x,y)みたいな構造体をN個まとめてリストにするとき
A = []
for i in range(N):
    a = tuple(map(int, input().split()))
    A.append(a)

A = sorted(A)

index = 0
ans = 0
while M>0:
    if M >= A[index][1]:
        ans += A[index][0]*A[index][1]
        M -= A[index][1]
    else:
        ans += A[index][0]*M
        M = 0
    index += 1

print(ans)