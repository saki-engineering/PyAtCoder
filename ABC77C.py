#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))
B.sort()
C = list(map(int, input().split()))
C.sort()

ans = 0
for b in B:
    a_cnt = bisect.bisect_left(A,b)
    c_cnt = N-bisect.bisect_right(C,b)
    ans += a_cnt*c_cnt

print(ans)