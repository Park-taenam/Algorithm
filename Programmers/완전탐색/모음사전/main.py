'''
문제: https://school.programmers.co.kr/learn/courses/30/lessons/84512
'''

# 풀이 1 - 중복순열
from itertools import product

def solution(word):
    words = []
    for i in range(1,6):
        for c in product(['A','E','I','O','U'], repeat=i):
            words.append(''.join(list(c)))
    words.sort()
    return words.index(word)+1

# 풀이 2 - DFS
'''https://only-wanna.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AA%A8%EC%9D%8C%EC%82%AC%EC%A0%84-%ED%92%80%EC%9D%B4'''
order = 0     
def solution(word):    
    dic = {}    
    lst =["A","E","I","O","U"]    

    def dfs (s):        
        global order        
        if len(s) > 5:            
            return        
        dic[s] = order;        
        order += 1        
        for i in lst:            
            if(len(s+i) > 5):                
                return            
            dfs(s + i)    
    dfs("")    
    return dic[word]