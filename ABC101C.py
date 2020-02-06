#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N,K = map(int, input().split())
A = list(map(int, input().split()))

ans = math.ceil((N-1)/(K-1))
print(ans)