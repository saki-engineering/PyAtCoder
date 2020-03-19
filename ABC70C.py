#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
import fractions
#from scipy.misc import comb

N = int(input())
T = [int(input()) for i in range(N)]

ans = T[0]
for t in T:
    ans = ans*t//fractions.gcd(ans,t)

print(ans)