import sys

number = []
for _ in range(9):
    number.append(int(sys.stdin.readline().strip()))

for i in range(9):
    if number[i] == max(number):
        print(max(number))
        print(i+1)