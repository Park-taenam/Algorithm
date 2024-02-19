import sys

N = int(sys.stdin.readline().strip())

papers = []
for _ in range(N):
    (x,y) = map(int, sys.stdin.readline().strip().split(" "))
    papers.append((x,y))

# # 풀이 1 - 틀림
''' 겹치는 경우 반영 안됨 '''
# results = 0
# for i in range(N):
#     result = 100
#     for j in range(1, N):
#         if i >= j:
#             continue
        
#         xi, yi = papers[i]
#         xj, yj = papers[j]
#         if xi <= xj:
#             x = xi+10-xj
#         elif xi > xj:
#             x = xj+10-xi
#         if (x < 0) or (x > 10):
#             x = 0
            
#         if yi <= yj:
#             y = yi+10-yj
#         elif yi > yj:
#             y = yj+10-yi
#         if (y < 0) or (y > 10):
#             y = 0
        
#         result -= x*y
#     results += result

# print(results)

# 풀이 2 - 맞음
''' 1X1 격자로 생각 '''
result = [[0]*100 for _ in range(100)]
for i in range(N):
    x, y = papers[i]
    for j in range(x, x+10):
        for k in range(y, y+10):
            result[j][k] = 1
results = 0
for i in range(100):
    results += sum(result[i])

print(results)