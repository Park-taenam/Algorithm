import sys

N = int(sys.stdin.readline().strip())

people = []
for _ in range(N):
    [x,y] = map(int, sys.stdin.readline().strip().split(" "))
    people.append([x,y])

results = []
for i in range(N):
    cnt = 1
    for j in range(N):
        if i==j:
            continue
        else:
            if (people[i][0] < people[j][0]) and (people[i][1] < people[j][1]):
                cnt += 1
    results.append(cnt)

for result in results:
    print(result, end=" ")