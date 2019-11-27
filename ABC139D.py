#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N = int(input())
ans = N*(N-1)//2
print(ans)

#9行目をN*(N-1)/2にすると、float型になってしまう(WA)ので注意