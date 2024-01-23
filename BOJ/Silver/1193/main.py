import sys

x = int(sys.stdin.readline().strip())

## 풀이 - 블로그
line = 1

while x > line:
    x -= line
    line += 1

''' num1 : 분자, num2: 분모'''
if line % 2 == 0:   # 분자 오름차순, 분모 내림차순
    num1 = x
    num2 = line - x + 1
elif line % 2 == 1: # 분자 내림차순, 분모 오름차순
    num1 = line - x +1
    num2 = x

print(num1, '/', num2, sep="")