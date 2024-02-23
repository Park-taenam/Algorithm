import sys

N, M = map(int, sys.stdin.readline().strip().split(" "))

cards = list(map(int, sys.stdin.readline().strip().split(" ")))
result = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if (i != j) and (j != k) and (i != k):
                temp = cards[i] + cards[j] + cards[k]
                if (result < temp) and (temp <= M):
                    result = temp

print(result)