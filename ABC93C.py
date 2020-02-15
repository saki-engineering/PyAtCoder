#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

A = list(map(int, input().split()))
A.sort()

ans = (A[2]-A[1]) + (A[1]-A[0])//2 + ((A[1]-A[0])%2)*2
print(ans)