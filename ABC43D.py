#coding: utf-8

s = input()
N = len(s)

for i in range(N-1):
    if s[i] == s[i+1]:
        print(i+1,i+2)
        exit()

for i in range(N-2):
    if s[i] == s[i+2]:
        print(i+1,i+3)
        exit()

print(-1, -1)