#coding: utf-8
import math
import heapq
import bisect
#from scipy.misc import comb

MOD = 10**9+7

def gcd(A,B):
    if B>A:
        A,B = B,A

    if(A%B==0):
        return B
    else:
        return gcd(B,A%B)

A,B,C,D = map(int, input().split())

L = (A-1)-((A-1)//C+(A-1)//D-(A-1)//(C*D//gcd(C,D)))
U = B-(B//C+B//D-B//(C*D//gcd(C,D)))

print(U-L)