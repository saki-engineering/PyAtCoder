#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N = int(input())
Map = []
for i in range(N):
    m = tuple(map(int, input().split()))
    Map.append(m)

for X in range(101):
    for Y in range(101):
        for m in Map:
            if m[2] != 0:
                H = abs(X-m[0])+abs(Y-m[1])+m[2]
                break
        flg = 1
        for m in Map:
            if m[2] != max(H-abs(X-m[0])-abs(Y-m[1]),0):
                flg = 0
                break
        if flg:
            print(X,Y,H)