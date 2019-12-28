#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N,K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0

# iが左からとる回数、jが右からとる回数
for i in range(K+1):
  for j in range(K+1-i):
    if i+j > N:
      break
    now = sorted(V[:i]+V[N-j:])
    tmp = min(K-i-j,bisect.bisect_left(now, 0))
    ans = max(ans,sum(now[tmp:]))

print(ans)
