'''
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42860
풀이: https://aiday.tistory.com/120
'''

def solution(name):    
    answer = 0
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
        # 위아래
        answer += min(ord(char) - ord("A"), ord("Z") - ord(char) + 1)
        
        # 양 옆
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min([min_move, 2*i + len(name) - next, i + 2*(len(name)-next)])
    
    return answer + min_move