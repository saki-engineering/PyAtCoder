#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N = int(input())
d = list(map(int, input().split()))

d.sort()
print(d[N//2]-d[N//2-1])