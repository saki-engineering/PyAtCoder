#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
import fractions
#from scipy.misc import comb

N,X = map(int, input().split())
x = list(map(int, input().split()))

x.append(X)
x.sort()

ans = abs(x[1]-x[0])
for i in range(1,N+1):
    ans = fractions.gcd(ans,abs(x[i]-x[i-1]))

print(ans)
