#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N = int(input())

# 複数個の数値を、intの配列として取得
A = list(map(int, input().split()))

# (A[i],i)のタプルリストを作って、昇順ソート
L = []
for i,v in enumerate(A):
    a = tuple([i+1,A[i]])
    L.append(a)
L = sorted(L, key=lambda x:x[1])

for i in range(N):
    print(L[i][0])