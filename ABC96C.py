#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

H,W = map(int, input().split())

s = ['.'*(W+2)]
for i in range(H):
    row = input()
    s.append('.' + row + '.')
s.append('.'*(W+2))

flg = 1
for i in range(1,H+1):
    for j in range(1,W+1):
        if s[i][j] == "#":
            if s[i-1][j] == "." and s[i+1][j] == "." and s[i][j-1] == "." and s[i][j+1] == ".":
                flg = 0

if flg:
    print("Yes")
else:
    print("No")