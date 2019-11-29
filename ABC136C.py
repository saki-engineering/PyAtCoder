#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N = int(input())

# 複数個の数値を、intの配列として取得
H = list(map(int, input().split()))

for i in range(1,N-1):
  if H[-i-1]-H[-i]==1:
    H[-i-1] -= 1
  elif H[-i-1]-H[-i]>1:
    print('No')
    exit()
    
print('Yes')