#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N,M = map(int, input().split())

city = []
for i in range(M):
    p,y = map(int, input().split())
    city.append([i,p,y,0])

city = sorted(city, key=lambda x:(x[1],x[2]))

city[0][3] = 1
no = 2
for i in range(1,M):
    if city[i][1] != city[i-1][1]:
        no = 1
    city[i][3] = no
    no += 1

city = sorted(city, key=lambda x:x[0])

for c in city:
    print('{0:06d}{1:06d}'.format(c[1],c[3]))