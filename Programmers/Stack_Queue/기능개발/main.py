'''
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42586
'''
from collections import deque
import math

def solution(progresses, speeds):
    days = deque()
    
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    
    answer = []
    while len(days) != 0:
        cnt = 0
        day = days[0]

        for _ in range(len(days)):
            if days[0] <= day:
                days.popleft()
                cnt += 1
            else:
                break
        answer.append(cnt)

    return answer