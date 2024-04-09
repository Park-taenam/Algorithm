'''
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42577
풀이: sort를 하면 직전 번호가 직후 번호의 접두사가 됨 -> 모든 케이스 안보고, 뒤만 확인하면 됨
'''
def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    
    return answer