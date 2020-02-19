#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
S = []
for i in range(N):
    s = input()
    S.append(s)

cnt = [0]*5
M = 'MARCH'
for s in S:
    for i in range(5):
        if s[0] == M[i]:
            cnt[i] += 1

ans = 0
for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            ans += cnt[i]*cnt[j]*cnt[k]

print(ans)