#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
#from scipy.misc import comb

N = int(input())
A = list(map(int, input().split()))

cnt = [0]*9
for a in A:
    for i in range(9):
        if i == 8: cnt[i] += 1
        else:
            if a < 400*(i+1):
                cnt[i] = 1
                break

Min = max(sum(cnt[:8]),1)
Max = sum(cnt[:8]) + cnt[8]

print(Min, Max)