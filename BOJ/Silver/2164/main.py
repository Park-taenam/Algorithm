import sys

# # 풀이 1 - 시간초과
# N = int(sys.stdin.readline().strip())
# cards = [x for x in range(1, N+1)]
# while len(cards) > 1:
#     del cards[0]
#     temp = cards[0]
#     del cards[0]
#     cards.append(temp)
# print(cards[0])

# 풀이 2 - deque
'''시간초과 해결됨'''
from collections import deque

N = int(sys.stdin.readline().strip())
deque = deque([x for x in range(1, N+1)])
while(len(deque) >1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)
print(deque[0])

# 풀이 3 - 블로그
'''규칙 찾음'''
import math

def find_last_card(N):
    M = 2 ** math.floor(math.log2(N))
    last_card = 2 * (N - M)
    return last_card if last_card != 0 else N

N=int(input())
print(find_last_card(N))