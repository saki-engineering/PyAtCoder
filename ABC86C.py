#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
A = [(0,0,0)]
for i in range(N):
    a = tuple(map(int, input().split()))
    A.append(a)

flg = 1
for i in range(1,N+1):
    dist = abs(A[i][1]-A[i-1][1])+abs(A[i][2]-A[i-1][2])
    time = A[i][0]-A[i-1][0]
    if time < dist:
        flg = 0
    else:
        if dist%2 != time%2:
            flg = 0

if flg:
    print("Yes")
else:
    print("No")