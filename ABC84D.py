#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = 10**5

Q = int(input())
L = [list(map(int, input().split())) for i in range(Q)]

prime = [1]*N
prime[0] = prime[1] = 0

for i in range(2,N):
    if prime[i]:
        tmp = i*2
        while tmp < N:
            prime[tmp] = 0
            tmp += i

r_sum = [0]*N
for i in range(3,N):
    if prime[i] and prime[(i+1)//2]:
        r_sum[i] = r_sum[i-1]+1
    else:
        r_sum[i] = r_sum[i-1]

for l in L:
    print(r_sum[l[1]]-r_sum[l[0]-1])