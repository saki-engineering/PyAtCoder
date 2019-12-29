#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N,M = map(int, input().split())

# (x,y)みたいな構造体をN個まとめてリストにするとき
L = []
R = []
for i in range(M):
    l,r = map(int, input().split())
    L.append(l)
    R.append(r)

print(max(min(R)-max(L)+1,0))