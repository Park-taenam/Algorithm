'''
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42862
comment
- 함수 내에서 동일 변수명으로 받으니 반영 안됨
'''

def solution(n, lost, reserve):
    lost_2 = list(set(lost) - set(reserve))
    reserve_2 = list(set(reserve) - set(lost))
    
    lost_cnt = len(lost_2)
    
    for num in lost_2:
        if num-1 in reserve_2:
            lost_cnt -= 1
            reserve_2.remove(num-1)
        elif num+1 in reserve_2:
            lost_cnt -= 1
            reserve_2.remove(num+1)

    return n - lost_cnt