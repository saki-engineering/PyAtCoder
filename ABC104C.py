#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

D,G = map(int, input().split())
Q = []
for i in range(D):
    p,c = map(int, input().split())
    Q.append(tuple([p,c,100*(i+1)*p+c]))

ans = 1000
for i in range(1<<D):
    point = 0
    comp = 0
    l_index = -1
    for j in range(D):
        if (i>>j)&1:
            comp += Q[j][0]
            point += Q[j][2]
        else:
            l_index = j
    
    if point >= G:
        ans = min(ans,comp)
    else:
        if l_index >= 0:
            for i in range(Q[l_index][0]):
                if point+(l_index+1)*100*i >= G:
                    ans = min(ans,comp+i)
                    break

print(ans)