import sys
import math

read = sys.stdin.readline

a,b,v = [int(v) for v in read().split('\n')[0].split()]

# 풀이 1 - 시간초과
# cnt = 0
# while(True):
#     cnt += 1
    
#     if v-a<=0:
#         break

#     v -= (a-b)
#     if v == 0:
#         break

# 풀이 2 - 정답
cnt = math.ceil((v-a)/(a-b)) + 1

print(int(cnt))