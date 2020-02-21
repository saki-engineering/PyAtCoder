#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

C = [list(map(int, input().split())) for i in range(3)]
A = [0]*3
B = [0]*3

flg = 0
for i in range(C[0][0]+1):
    A[0] = i
    B[0] = C[0][0]-i
    for j in range(1,3):
        A[j] = C[j][0]-B[0]
        B[j] = C[0][j]-A[0]
    
    tmp = abs(C[1][1]-A[1]-B[1])+abs(C[1][2]-A[1]-B[2])+abs(C[2][1]-A[2]-B[1])+abs(C[2][2]-A[2]-B[2])
    if tmp==0:
        flg = 1

if flg:
    print("Yes")
else:
    print("No")