#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 0
for key, value in Counter(A).items():
    if key <= value:
        ans += (value - key)
    else:
        ans += value

print(ans)