#coding: utf-8
import math
import heapq

MOD = 10**9+7

def combination(n, r):
    r = min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n+1-i) % MOD
        denom = denom * i % MOD
    return numer * pow(denom, MOD-2, MOD) % MOD


X,Y = map(int, input().split())

if (X+Y)%3!=0:
    print(0)
else:
    a = (2*X-Y)//3
    b = (2*Y-X)//3
    if a<0 or b<0:
        print(0)
    else:
        print(combination(a+b, a))
