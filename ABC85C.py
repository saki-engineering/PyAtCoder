#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N,Y = map(int, input().split())

a = b = c = -1
for i in range((Y//10000)+1):
    for j in range((Y-10000*i)//5000+1):
        s = 10000*i + 5000*j + 1000*(N-i-j)
        if s == Y:
            a,b,c = i,j,N-i-j
            
print(a,b,c)