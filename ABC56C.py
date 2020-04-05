#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
#from scipy.misc import comb

X = int(input())
ans = 0
i = 1
while 1:
    ans += i
    if X <= ans:
        print(i)
        break
    i += 1