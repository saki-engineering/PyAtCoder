#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

def gcd(A,B):
    if B>A:
        A,B = B,A

    if(A%B==0):
        return B
    else:
        return gcd(B,A%B)

A,B = map(int, input().split())
G = gcd(A,B)

ans = 1
for i in range(2,math.ceil(math.sqrt(G))+1):
    if G%i==0:
        ans+=1
        while G%i==0:
            G/=i
if G!=1:
    ans+=1

print(ans)
