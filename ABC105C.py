#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
ans = ""
while N:
    ans = str(N&1)+ans
    N = -(N>>1)
print(ans if ans else 0)

##数字じゃなくて、あえてansを文字列にすることで、桁を増やすのが簡単になる