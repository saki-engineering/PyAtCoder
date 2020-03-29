#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
#from scipy.misc import comb

H,W = map(int, input().split())

if H%3 == 0:
    print(0)
elif W%3 == 0:
    print(0)
else:
    ans = H*W
    A = [0]*3
    for i in range(1,H):
        A[0] = i*W
        A[1] = (H-i)*(W//2)
        A[2] = (H-i)*(W-W//2)
        A.sort()
        ans = min(ans,A[2]-A[0])
    
    for j in range(1,W):
        A[0] = H*j
        A[1] = (H//2)*(W-j)
        A[2] = (H-H//2)*(W-j)
        A.sort()
        ans = min(ans,A[2]-A[0])

    ans = min(ans, H, W)

    print(ans)