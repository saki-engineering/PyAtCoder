#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N,Q = map(int, input().split())

node = [0]*N
edge = [[] for _ in range(N)]
color = [0]*N

for i in range(N-1):
    a,b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

for i in range(Q):
    p,x = map(int, input().split())
    node[p-1] += x

stack = [0]
while stack:
    s = stack.pop()
    color[s] = 1
    for t in edge[s]:
        if color[t]==0:
            stack.append(t)
            node[t] += node[s]
    color[s]=2

for n in node:
    print(n)

#DFSはLIFOのリスト構造を用いる