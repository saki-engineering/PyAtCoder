#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

S = input()
T = input()

dict = {}
re_dict = {}
flg = 1
for i in range(len(S)):
    if S[i] in dict:
        if T[i] != dict[S[i]]:
            flg = 0
            break
    else:
        dict[S[i]] = T[i]
        if T[i] in re_dict:
            if re_dict[T[i]] != S[i]:
                flg = 0
                break
        else:
            re_dict[T[i]] = S[i]

if flg:
    print("Yes")
else:
    print("No")

#問題を「一対一の変換表が作れるか」と読み替えられるかどうか