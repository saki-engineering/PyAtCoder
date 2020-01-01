#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

def gcd(A,B):
    if B>A:
        A,B = B,A

    if(A%B==0):
        return B
    else:
        return gcd(B,A%B)

N = int(input())
A = list(map(int, input().split()))

L = A[:]
for i in range(1,N):
    L[i] = gcd(L[i],L[i-1])

R = A[:]
for i in range(N-2,-1,-1):
    R[i] = gcd(R[i],R[i+1])

ans = max(L[N-2],R[1])
for i in range(1,N-1):
    ans = max(ans, gcd(L[i-1],R[i+1]))

print(ans)