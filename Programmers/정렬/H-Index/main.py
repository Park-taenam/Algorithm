'''
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42747
'''
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for i, num in enumerate(citations):
        if num > i:         # i or answer
            answer = i+1
        else:
            break
    
    return answer