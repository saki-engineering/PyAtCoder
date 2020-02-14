#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
X = list(map(int, input().split()))
Y = sorted(X)

for x in X:
    if x <= Y[N//2-1]:
        print(Y[N//2])
    else:
        print(Y[N//2-1])