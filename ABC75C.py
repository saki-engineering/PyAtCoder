#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N,M = map(int, input().split())
G = [[] for _ in range(N)]

E = []
for _ in range(M):
    a,b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
    E.append((a-1,b-1))

d = [0] + [-1]*(N-1)

def dfs(n):
    d[n] = 0
    for v in G[n]:
        if d[v] == -1:
            dfs(v)

ans = 0
for a,b in E:
    G[a].remove(b)
    G[b].remove(a)

    dfs(0)

    if -1 in d:
        ans += 1
    
    for i in range(1,N):
        d[i] = -1
    G[a].append(b)
    G[b].append(a)

print(ans)