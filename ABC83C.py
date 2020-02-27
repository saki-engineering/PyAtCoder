#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

X,Y = map(int, input().split())
ans = 1

while X*2 <= Y:
    X *= 2
    ans += 1

print(ans)