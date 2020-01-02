#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

S = input()

n1 = S[::2].count("0")+S[1::2].count("1")
n2 = S[::2].count("1")+S[1::2].count("0")

ans = len(S)-max(n1,n2)
print(ans)