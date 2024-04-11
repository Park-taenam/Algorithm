'''
문제: https://school.programmers.co.kr/learn/courses/30/lessons/60058
풀이: 하라는 대로 따라하면 된다.
'''
from collections import deque

def seperate_u_v(p):
    # u : 균형잡힌 괄호 문자열, v : 나머지
    open_p, close_p = 0,0
    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i+1], p[i+1:] # u,v

def check_balance(p):
    stack = deque()
    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True if not stack else False

def solution(p):
    if not p:   # 과정 1
        return p
    
    u,v = seperate_u_v(p)   # 과정 2
    
    if check_balance(u):    # 과정 3
        return u + solution(v)  # 과정 3-1
    else:
        answer = '('    # 과정 4-1
        answer += solution(v)   # 과정 4-2
        answer += ')'   # 과정 4-3
        
        for pp in u[1:len(u)-1]:    # 과정 4-4
            if pp == '(':
                answer += ')'
            else:
                answer += '('
    return answer   # 과정 4-5