#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N = int(input())
h = list(map(int, input().split()))

ans = h[0]
base = h[0]
for i in range(1,N):
    ans += max(h[i]-base,0)
    base = h[i]

print(ans)