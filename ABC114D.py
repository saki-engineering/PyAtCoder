#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N = int(input())

prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
p_cnt = [0]*25

for i in range(2,N+1):
    p_index = 0
    while i > 1:
        if i%prime[p_index] == 0:
            p_cnt[p_index] += 1
            i /= prime[p_index]
        else:
            p_index += 1

ans = 0

for i in range(25):
    if p_cnt[i] >= 74:
        ans += 1

for i in range(25):
    for j in range(i+1,25):
        if p_cnt[i] >= 2 and p_cnt[j] >= 24:
            ans += 1
        if p_cnt[i] >= 24 and p_cnt[j] >= 2:
            ans += 1
        if p_cnt[i] >= 4 and p_cnt[j] >= 14:
            ans += 1
        if p_cnt[i] >= 14 and p_cnt[j] >= 4:
            ans += 1

for i in range(25):
    for j in range(i+1,25):
        for k in range(j+1,25):
            if p_cnt[i] >= 2 and p_cnt[j] >= 4 and p_cnt[k] >= 4:
                ans += 1
            if p_cnt[i] >= 4 and p_cnt[j] >= 2 and p_cnt[k] >= 4:
                ans += 1
            if p_cnt[i] >= 4 and p_cnt[j] >= 4 and p_cnt[k] >= 2:
                ans += 1

print(ans)
# 74, 2*24, 4*14, 2*4*4