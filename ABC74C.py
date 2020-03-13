#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

A,B,C,D,E,F = map(int, input().split())

water = []
for a in range(30):
    for b in range(30):
        w = 100*A*a + 100*B*b
        if w == 0: continue
        if w <= F: water.append(w)
        else: break

sugar = []
for c in range(3000):
    for d in range(3000):
        s = c*C + d*D
        if s <= F: sugar.append(s)
        else: break

d = 0
anss = 0
answ = 100*A
for w in water:
    for s in sugar:
        if w+s > F or w*E < 100*s:
            continue
        tmpd = (100*s)/(w+s)
        if tmpd > d:
            d = tmpd
            anss = s
            answ = w

print(anss+answ, anss)