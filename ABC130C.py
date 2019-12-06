#coding: utf-8
import math
import heapq
import bisect
#from scipy.misc import comb

MOD = 10**9+7

W,H,x,y = map(int, input().split())

print(W*H/2)

if x==W/2 and y==H/2:
    print(1)
else:
    print(0)