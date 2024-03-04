import sys

N = int(sys.stdin.readline().strip())

# # 풀이 1 - 런타임 에러
# ''' 한자리 들어오면 안되는 듯'''
# ''' 나름대로 계산량 줄이려 했는데, 그냥 가장 간단한 거 먼저 해보자'''
# N_digits = len(str(N))

# for i in range(N-9*int(N_digits), N+1):
#     M = i + sum(list(map(int, list(str(i)))))
#     if M == N:
#         print(i)
#         break
#     if i == N:
#         print(0)

# 풀이 2
for i in range(1, N+1):
    num = sum(map(int, str(i)))
    num_sum = i + num
    if num_sum == N:
        print(i)
        break
else:
    print(0)