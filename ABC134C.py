#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N = int(input())
A = []
for i in range(N):
    a = int(input())
    A.append(a)
B = sorted(A)

for a in A:
    if B[N-1] == B[N-2]:
        print(B[N-1])
    else:
        if a == B[N-1]:
            print(B[N-2])
        else:
            print(B[N-1])

#Cのときみたいにforループ回してmax_1とmax_2を求めてもいいけど、sortしちゃうと短くかける