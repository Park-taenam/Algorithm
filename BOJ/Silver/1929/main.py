import sys

M, N = map(int, sys.stdin.readline().strip().split())

# # 풀이 1 - 시간초과
# result = []
# for i in range(2, N+1):
#     temp = True
#     if i == 2:
#         result.append(i)
#     else:
#         for num in result:
#             if i%num==0:
#                 temp = False
#                 break
#         if temp:
#             result.append(i)
# for num in result:
#     if num >= M and num <= N:
#         print(num)

# 풀이 2 - 에라토스테네스의 체
for i in range(M, N+1):
    if i == 1:
        continue
    
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            break
    else:
        print(i)