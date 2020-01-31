#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb
 
N,K = map(int, input().split())
 
# 複数個の数値を、intの配列として取得
X = list(map(int, input().split()))
 
ans = 10**18
for i in range(N-K+1):
    if X[i]*X[i+K-1] >= 0:
        ans = min(ans,max(abs(X[i]),abs(X[i+K-1])))
    else:
        ans = min(ans, 2*abs(X[i])+abs(X[i+K-1]), abs(X[i])+2*abs(X[i+K-1]))
 
print(ans)