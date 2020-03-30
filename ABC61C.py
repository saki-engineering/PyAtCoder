#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
#from scipy.misc import comb

N,K = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
A.sort()

cnt = 0
for a,b in A:
    cnt += b
    if cnt >= K:
        print(a)
        break