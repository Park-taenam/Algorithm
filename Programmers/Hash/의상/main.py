'''
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42578
'''

def solution(clothes):
    cate_list = [x[1] for x in clothes]
    print(cate_list)
    
    answer = 1
    for cate in set(cate_list):
        answer *= cate_list.count(cate)+1
    
    return answer -1