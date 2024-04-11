'''
문제: https://school.programmers.co.kr/learn/courses/30/lessons/87946
'''
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    pers = list(permutations(list(range(len(dungeons))), len(dungeons)))
    
    for per in pers:
        k_2 = k
        cnt = 0
        for i in per:
            if dungeons[i][0] <= k_2:
                k_2 -= dungeons[i][1]
                cnt += 1
        if answer <= cnt:
            answer = cnt
    return answer
