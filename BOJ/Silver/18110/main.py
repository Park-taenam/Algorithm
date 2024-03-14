'''
round는 오사오입으로 처리함
5 미만의 숫자는 내림, 5 초과의 숫자는 올림
만약 반올림할 자릿수가 5일 경우 5의 앞자리가 홀수인 경우 올림, 짝수인 경우 내림
-> 사사오입(4 이하의 숫자는 내림, 5 이상의 숫자는 올림)을 위해 직접 함수 구현해야 함()
'''
import sys

n = int(sys.stdin.readline().strip())
level = [int(sys.stdin.readline().strip()) for _ in range(n)]

def my_round(num):
    return int(num) + (1 if num-int(num) >= 0.5 else 0)

if n:
    idx = my_round(len(level)*0.15)
    level = sorted(level)[idx:-idx] if idx else level
    print(my_round(sum(level)/len(level)))
else:
    print(0)