#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

M = list(input())
N = [int(m) for m in M]

ans_list = [N[0],'+',N[1],'+',N[2],'+',N[3],'=',7]

for i in range(1<<3):
    tmp = N[0]
    for j in range(3):
        if i & (1<<j):
            tmp += N[j+1]
            ans_list[j*2+1] = '+'
        else:
            tmp -= N[j+1]
            ans_list[j*2+1] = '-'
    if tmp == 7:
        ans_maped = map(str,ans_list)
        ans = ''.join(ans_maped)
        print(ans)
        break