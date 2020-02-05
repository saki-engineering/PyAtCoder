#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    A[i] -= i
A.sort()

if(N%2):
    b = A[N//2]
else:
    b = (A[N//2]+A[N//2-1])//2

ans1 = 0
ans2 = 0
for a in A:
    ans1 += abs(a-b)
    ans2 += abs(a-(b+1))

print(min(ans1, ans2))