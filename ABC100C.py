#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    while a%2==0:
        a = a//2
        ans += 1

print(ans)