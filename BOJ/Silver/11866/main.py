'''
거의 정답이나 틀림
-> k를 더해주는게 아니라 k-1을 더해줘야함
-> list 길이로 나눈 나머지 사용
'''
import sys

n, k = map(int, sys.stdin.readline().strip().split(" "))

# # 풀이 1 - 못품
# people = list(range(1, n+1))
# t = -1
# results = []
# for _ in range(n):
#     t += 3
#     if t >= len(people):
#         t -= len(people)
#     print(people[t])
#     results.append(people.pop(t))
# print(results)

# 풀이 2 - 블로그
idx = 0
queue = [i for i in range(1, n+1)]
res = []
while queue:
    idx += k - 1  # k-1번째 인덱스까지 건너뛰기
    if idx >= len(queue):  # 인덱스가 범위를 넘어갈 경우
        idx %= len(queue)  # 나머지 연산을 통해 인덱스 계산
    res.append(str(queue.pop(idx)))  # k번째 수 제거 후 결과 배열에 추가

# 결과 출력
print("<", ", ".join(res), ">", sep="")