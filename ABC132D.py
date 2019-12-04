#coding: utf-8
import math
import heapq
import bisect
from scipy.misc import comb

MOD = 10**9+7

N,K = map(int, input().split())

for i in range(1,K+1):
    ans = (comb(K-1,i-1,exact=True)%MOD)*(comb(N-K+1,i,exact=True)%MOD)%MOD
    print(ans)