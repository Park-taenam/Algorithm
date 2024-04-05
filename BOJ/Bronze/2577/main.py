import sys

num = 1
for _ in range(3):
    num *= int(sys.stdin.readline().strip())

results = [0]*10
for i in str(num):
    results[int(i)] += 1

for result in results:
    print(result)