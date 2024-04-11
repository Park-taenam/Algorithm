'''
문제: https://school.programmers.co.kr/learn/courses/30/lessons/43162
'''
def dfs(graph, v, visit):
    visit[v] = True
    for i, k in enumerate(graph[v]):
        if not visit[i] and k == 1:
            dfs(graph, i, visit)
    
def solution(n, computers):
    visited = [False] * n
    
    answer = 0
    for i in range(n):
        if visited[i] == False:
            answer += 1
        dfs(computers, i, visited)
    
    return answer