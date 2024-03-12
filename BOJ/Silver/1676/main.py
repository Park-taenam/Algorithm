import sys

n = int(sys.stdin.readline().strip())

# 풀이 1
num = 1
result = 0
for i in range(1,n+1):
    num *= i
    print(num)
    while True:
        if num%10==0:
            num //= 10
            result += 1
        else:
            break
    print(num)
print(result)

# 풀이 2 - 5의 갯수
print(n//5 + n//25 + n//125)

# 풀이 3 - 팩토리얼 계산 후, 0 갯수
from math import factorial
result = 0
for x in str(factorial(n))[::-1]:
    if x!='0':
        break
    result+=1
print(result)