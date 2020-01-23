#coding: utf-8
import math
import heapq
import bisect
import numpy as np
#from scipy.misc import comb

N = int(input())

def cnt_753(s):
    if int(s) > N:
        return 0
    # リスト内包表記　[式 for 任意の変数名 in イテラブルオブジェクト]
    # 組み込み関数all →全てTrueならTrueを返す
    ret = 1 if all(s.count(c) > 0 for c in '753') else 0
    for c in '753':
        ret += cnt_753(s + c)
    return ret

print(cnt_753('0'))