#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

H,W = map(int, input().split())

Map = []
for i in range(H):
    h = list(map(int, input().split()))
    Map.append(h)

N = 0
ans = []

for i in range(H):
    for j in range(W-1):
        if Map[i][j] % 2 == 1:
            N += 1
            Map[i][j] -= 1
            Map[i][j+1] += 1
            ans.append((i+1,j+1,i+1,j+2))

for i in range(H-1):
    if Map[i][W-1] % 2 == 1:
        N += 1
        Map[i][W-1] -= 1
        Map[i+1][W-1] += 1
        ans.append((i+1,W,i+2,W))

print(N)
for a in ans:
    print(' '.join(map(str, a)))