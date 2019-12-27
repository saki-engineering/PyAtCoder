#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

MOD = 10**9+7

H,W = map(int, input().split())
M = np.array([list(input().rstrip("\n")) for _ in range(H)]) == "."

D = np.zeros((H,W),dtype=int)
U = np.zeros((H,W),dtype=int)
L = np.zeros((H,W),dtype=int)
R = np.zeros((H,W),dtype=int)

for i in range(H):
    U[i] = (U[i-1] + 1) * M[i]
    D[-i-1] = (D[-i] + 1) * M[-i-1]

for i in range(W):
    L[:,i] = (L[:,i-1] + 1) * M[:,i]
    R[:,-i-1] = (R[:,-i] + 1) * M[:,-i-1]

print(np.max(U+D+L+R)-3)