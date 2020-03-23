#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
A = list(map(int, input().split()))

ans = A[N-1::-2] + A[N%2::2]

print(' '.join(map(str, ans)))