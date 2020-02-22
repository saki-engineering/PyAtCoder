#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

MOD = 10**9+7

N = int(input())
A = [list(map(int, input().split())) for i in range(2)]

ans = 0
for i in range(N):
    tmp = 0
    for j in range(i+1):
        tmp += A[0][j]
    for j in range(i,N):
        tmp += A[1][j]
    ans = max(ans,tmp)

print(ans)