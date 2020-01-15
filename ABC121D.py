#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

A,B = map(int, input().split())

if A%2 == 0:
    grp = (B-A+1)//2
    ans = grp%2
    if B%2 == 0:
        ans = ans^B
else:
    grp = (B-A)//2
    ans = (grp%2)^A
    if B%2 == 0:
        ans = ans^B

print(ans)
