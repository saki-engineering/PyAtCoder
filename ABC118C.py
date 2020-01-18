#coding: utf-8
import math
import heapq
import bisect
import numpy as np
import fractions
#from scipy.misc import comb

N = int(input())
A = list(map(int, input().split()))

ans = A[0]
for i in range(1,N):
    ans = fractions.gcd(ans, A[i])

print(ans)

#math.gcd()ではなくてAtCoderのPythonヴァージョンではfractions.gcd()が使用可能