#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

S = input()

red = 0
ble = 0

for s in S:
    if s == '0':
        red += 1
    else:
        ble += 1

ans = min(red, ble)*2
print(ans)