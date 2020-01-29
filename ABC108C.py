#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N,K = map(int, input().split())

ans = (N//K)**3
if K%2 == 0:
    if N%K >= K//2:
        c = N//K+1
    else:
        c = N//K
    ans += c**3

print(ans)