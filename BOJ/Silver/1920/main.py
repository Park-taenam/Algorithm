import sys

n = int(sys.stdin.readline().strip())
N = sorted(list(map(int, sys.stdin.readline().strip().split(" "))))
m = int(sys.stdin.readline().strip())
M = list(map(int, sys.stdin.readline().strip().split(" ")))

# # 풀이 1: 시간 초과
# for num in M:
#     if num in N:
#         print(1)
#     else:
#         print(0)

# 풀이 2: 이진(이분) 탐색 
'''
1. 자료의 중앙에 있는 원소를 고른다
2. 중앙 원소의 값과 찾고자 하는 목표값을 비교한다
3. 목표값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로운 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
4. 찾고자 하는 값을 찾을 때까지 1~3의 과정을 반복한다.
'''
def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

for l in M:
    start = 0
    end = len(N)-1
    print(binary(l, N, start, end))