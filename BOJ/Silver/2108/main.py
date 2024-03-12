import sys

n = int(sys.stdin.readline().strip())
data = [int(sys.stdin.readline().strip()) for _ in range(n)]
data.sort()

# 산술평균
print(round(sum(data)/n))
# 중앙값
print(data[n//2])
# 최빈값
cnt = {}
for i in data:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
freq = max(cnt.values())
numbers = []
for key, value in cnt.items():
    if value == freq:
        numbers.append(key)
if len(numbers) == 1:
    print(numbers[0])
else:
    print(sorted(numbers)[1])
# 범위
print(data[-1]-data[0])