import sys

temp = [sys.stdin.readline().strip() for _ in range(2)]
S = temp[0]
i = temp[1]
print(S[int(i)-1])