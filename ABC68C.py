#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N,M = map(int, input().split())

A = []
B = []

for _ in range(M):
    a,b = map(int, input().split())
    if a == 1: A.append(b)
    elif b == N: B.append(a)

B.sort()
for a in A:
    if bisect.bisect_left(B, a) < len(B) and B[bisect.bisect_left(B, a)]==a:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")