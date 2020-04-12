#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
import itertools
#from scipy.misc import comb

sx,sy,tx,ty = map(int, input().split())
ans = 'U'*(ty-sy) + 'R'*(tx-sx) + 'D'*(ty-sy) + 'L'*(tx-sx+1) + 'U'*(ty-sy+1) + 'R'*(tx-sx+1) + "DR" + 'D'*(ty-sy+1) + 'L'*(tx-sx+1) + 'U'
print(ans)