#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N,K = map(int, input().split())
A = list(map(int, input().split()))

middle = -1
for i in range(N):
    if A[i] == 1:
        middle = i

left = i
right = N-i-1

if (left%(K-1))+(right%(K-1)+1) <= K:
    