#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

INF = 10*10

H,W = map(int, input().split())
C = [list(map(int, input().split())) for i in range(10)]
A = [list(map(int, input().split())) for i in range(H)]

N = 100

# mp[i][j]..i→1にj回でする時の最小魔力
mp = [[INF]*N for _ in range(11)]
mp[0][1] = 0
for i in range(10):
    mp[i][1] = C[i][1]

for j in range(2,N):
    for i in range(10):
        mp[i][j] = min((C[i][k] + mp[k][j-1]) for k in range(10))

cnt = [0]*10
for a in A:
    for i in range(10):
        cnt[i] += a.count(i)

ans = 0
for i in range(10):
    ans += cnt[i] * mp[i][N-1]

print(ans)