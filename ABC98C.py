#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
S = input()

left_W = [0]*N
right_E = [0]*N

for i in range(N-1):
    if S[i]=='W':
        left_W[i+1] = left_W[i]+1
    else:
        left_W[i+1] = left_W[i]

for i in range(N-1,0,-1):
    if S[i]=='E':
        right_E[i-1] = right_E[i]+1
    else:
        right_E[i-1] = right_E[i]

ans = N
for i in range(N):
    ans = min(ans, left_W[i]+right_E[i])

print(ans)