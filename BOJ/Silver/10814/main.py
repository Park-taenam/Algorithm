import sys

N = int(sys.stdin.readline().strip())

person_list = []
for _ in range(N):
    [age, name] = sys.stdin.readline().strip().split()
    person_list.append([age, name])

person_list.sort(key=lambda x: int(x[0]))

for person in person_list:
    print(f"{person[0]} {person[1]}")