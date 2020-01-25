#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N,M = map(int, input().split())

R = math.ceil(math.sqrt(M))
div = []
for i in range(1,R+1):
    if M % i == 0:
        div.append(M//i)
        div.append(i)

ans = 1
for d in div:
    if M//d >= N:
        ans = max(ans,d)

print(ans)