#coding: utf-8
import math
import heapq

N = int(input())

A = []
for i in range(N):
    a = tuple(map(int, input().split()))
    A.append(a)

ans = 0
for a1 in A:
    for a2 in A:
        ans += math.sqrt((a1[0]-a2[0])**2 + (a1[1]-a2[1])**2)

ans /= N
print(ans)