#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N = int(input())
time = []

for i in range(5):
    a = int(input())
    time.append(a)

ans = math.ceil(N/min(time))+4
print(ans)