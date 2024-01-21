import sys
from itertools import permutations
import math

N = int(sys.stdin.readline())

for _ in range(N):
    # print(sys.stdin.readline())
    n,m = [int(v) for v in sys.stdin.readline().split()]
    
    # # 풀이 1 - 시간 초과
    # print(len(list(permutations(list(range(m)),n))))

    # # 풀이 2 - 겹치면 안되서 perm 아님
    # print(math.perm(m,n))   

    # 풀이 3 - 정답
    print(math.comb(m,n))