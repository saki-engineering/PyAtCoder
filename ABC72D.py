#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
A = [0] + list(map(int, input().split()))

ans = 0
for i in range(1,N):
    if A[i] == i:
        ans += 1
        A[i] = A[i+1]
        A[i+1] = i

if A[N] == N:
    ans += 1

print(ans) 