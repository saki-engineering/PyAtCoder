#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
v = list(map(int, input().split()))

odd = v[::-2]
even = v[::2]
#一個飛ばしもこうすれば簡単に書ける

o_elm = Counter(odd).most_common(2)+[(0,0)]
e_elm = Counter(even).most_common(2)+[(0,0)]
if o_elm[0][0]==e_elm[0][0]:
  print(N -max(o_elm[0][1]+e_elm[1][1], o_elm[1][1]+e_elm[0][1]))
else:
  print(N -o_elm[0][1] -e_elm[0][1])