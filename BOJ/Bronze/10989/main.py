import sys

N = int(sys.stdin.readline().strip())

# # 풀이 1 - 메모리 초과
# results = []
# for _ in range(N):
#     results.append(sys.stdin.readline().strip())

# for i in sorted(results):
#     print(i)

# 풀이 2 - 계수 정렬
arr = [0 for _ in range(10000+1)]

for _ in range(N):
    arr[int(sys.stdin.readline().strip())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)