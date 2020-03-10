#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

S = input()
T = input()
 
for i in reversed(range(len(S)-len(T)+1)):
    flag = 1
    for j in range(len(T)) :
        if S[i+j] != T[j] and S[i+j] != "?":
            flag = 0
    if flag:
        ans = S[:i] + T + S[i+len(T):]
        print(ans.replace("?", "a"))
        exit()
 
print("UNRESTORABLE")