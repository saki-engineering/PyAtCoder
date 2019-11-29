#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

S = input()
N = len(S)

child = [1]*N

for i in range(N-1):
    if S[i]=='R' and S[i+1]=='R':
        child[i+2] += child[i]
        child[i] = 0

for i in range(N-1):
    if S[-(i+1)]=='L' and S[(-(i+2))]=='L':
        child[-(i+3)] += child[-(i+1)]
        child[-(i+1)] = 0

for c in child:
    print(c)