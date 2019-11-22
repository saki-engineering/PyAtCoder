#coding: utf-8
import math
import heapq

MOD = 10**9+7

a,b,x = map(int, input().split())

V = (a**2)*b

if x>=(V/2):
    h = 2*b-2*x/(a*a)
    htan = h/a
else:
    h = 2*x/(a*b)
    htan = b/h

ans = math.atan(htan)*180/(math.atan(1.0)*4)
print(ans)