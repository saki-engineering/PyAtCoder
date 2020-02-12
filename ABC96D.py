#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
THS = 55555

sieve = [0]*(THS+1)
prime_list = []
for i in range(2,THS+1):
    if sieve[i] == 0:
        prime_list.append(i)
        j = i
        while j <= THS:
            sieve[j] = 1
            j += i

ans = [[] for _ in range(4)]
for p in prime_list:
    ans[p%5-1].append(p)

for a in ans:
    if len(a) >= N:
        print(*a[:N])
        break