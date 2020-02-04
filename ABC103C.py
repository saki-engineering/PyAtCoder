#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
import fractions
#from scipy.misc import comb

N = int(input())
A = list(map(int, input().split()))

m = A[0]
for a in A:
    m = (m*a)//fractions.gcd(m,a)

ans = 0
for a in A:
    ans += (m-1)%a

print(ans)