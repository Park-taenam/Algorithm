'''
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42885
'''

from collections import deque

def solution(people, limit):
    answer = 0
    people_sort = deque(sorted(people))
    
    while people_sort:
        if len(people_sort) == 1:
            answer += 1
            break

        if people_sort[0] + people_sort[-1] <= limit:
            people_sort.pop()
            people_sort.popleft()
            answer += 1
        else:
            people_sort.pop()
            answer += 1

    return answer