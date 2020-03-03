#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

INF = 10**9

N = int(input())

F = [list(map(int, input().split())) for i in range(N)]
P = [list(map(int, input().split())) for i in range(N)]

ans = -INF
for i in range(1,1<<10):
    tmp = 0
    for j in range(N):
        b_hours = 0
        for k in range(10):
            if i&(1<<k) and F[j][k]:
                b_hours += 1
        tmp += P[j][b_hours]
    ans = max(ans, tmp)

print(ans)