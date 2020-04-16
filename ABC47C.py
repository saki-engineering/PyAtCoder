#coding: utf-8

S = input()
N = len(S)

ans = 0
for i in range(1,N):
    if S[i-1] != S[i]: ans += 1

print(ans)