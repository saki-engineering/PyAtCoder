#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

M = 10**5

N = int(input())
A = list(map(int, input().split()))

cnt = [0]*(M+2)
for a in A:
    cnt[a] += 1

ans = 0
for i in range(1,M):
    ans = max(ans, cnt[i-1]+cnt[i]+cnt[i+1])

print(ans)