#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
#from scipy.misc import comb

N = int(input())

ans = 100
A = 1
while A * A <= N:
    if N % A == 0:
        B = N // A
        ans = min(ans, len(str(B)))
    A += 1

print(ans)