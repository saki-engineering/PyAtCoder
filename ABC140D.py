#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

N,K = map(int, input().split())

# 複数個の数値を、intの配列として取得
S = input()

bck=0
for i in range(1,N):
    if(S[i]==S[i-1]):
        bck+=1

print(min(N-1,bck+K*2))

#Pythonだと、あまりコード中で処理をさせず、あらかじめわかっている数学的解答をコードでprintさせるような解答が多い