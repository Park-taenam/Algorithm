import sys

K = int(sys.stdin.readline().strip())

results = []
for _ in range(K):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        results.pop()
    else:
        results.append(num)

print(sum(results))