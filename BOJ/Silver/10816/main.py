'''https://hongcoding.tistory.com/12'''
'''이진탐색으로 우선 시도 해보는 게 맞긴함'''
import sys

N = int(sys.stdin.readline().strip())
N_list = list(map(int, sys.stdin.readline().strip().split(" ")))

M = int(sys.stdin.readline().strip())
M_list = list(map(int, sys.stdin.readline().strip().split(" ")))

# # 풀이 1 - 시간초과
# for m in M_list:
#     print(sum([True if x == m else False for x in N_list]), end=" ")

# 풀이 2 - 파이썬 내장 몯류 Counter
from collections import Counter

count = Counter(N_list)

for m in M_list:
    if m in count:
        print(count[m], end = " ")
    else:
        print(0, end = " ")

# 풀이 3 - 딕셔너리 
count_dict = {}
for n in N_list:
    if n in count_dict:
        count_dict[n] += 1
    else:
        count_dict[n] = 1

for m in M_list:
    if m in count_dict:
        print(count_dict[m], end = " ")
    else:
        print(0, end = " ")