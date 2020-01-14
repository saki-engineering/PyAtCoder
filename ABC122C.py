#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N,Q = map(int, input().split())
S = input()

L = []
R = []

for i in range(Q):
    l,r = map(int, input().split())
    L.append(l)
    R.append(r)

rs = [0,0]
cnt = 0
for i in range(1,N):
    # s[i-1:i+1] == 'AC'という書き方もあり
    if S[i-1]=='A' and S[i]=='C':
        cnt += 1
        rs.append(cnt)
    else:
        rs.append(cnt)

for i in range(Q):
    ans = rs[R[i]]-rs[L[i]]
    print(ans)