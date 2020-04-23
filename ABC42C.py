#coding: utf-8

N,K = map(int, input().split())
D = list(input().split())

while 1:
    flg = 1
    for d in D:
        if d in str(N): flg = 0
    if flg:
        print(N)
        break
    N += 1