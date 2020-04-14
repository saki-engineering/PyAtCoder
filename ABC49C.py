#coding: utf-8

S = input()
N = len(S)

A = ["dream", "erase", "eraser", "dreamer"]
dp = [1] + [0]*N
for i in range(5,N+1):
    if i >= 5 and S[i-5:i] == A[0]: dp[i] = dp[i-5]
    if i >= 5 and S[i-5:i] == A[1]: dp[i] = dp[i-5]
    if i >= 6 and S[i-6:i] == A[2]: dp[i] = dp[i-6]
    if i >= 7 and S[i-7:i] == A[3]: dp[i] = dp[i-7]

if dp[N]: print("YES")
else: print("NO")