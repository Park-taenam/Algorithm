'''
int형으로 바꿔야 sort 제대로 됨!
'''
import sys

N = int(sys.stdin.readline().strip())

points = []
for i in range(N):
    [x,y] = map(int, sys.stdin.readline().strip().split(" "))
    points.append([x,y])
points.sort()
for point in points:
    print(point[0], point[1])

'''
만약 문제가 두 번째 값이 먼저 기준이 된다면 이렇게 해야함
key에 function으로 넣으면 됨
'''
# 두 번째 값을 기준으로 오름차순으로 정렬을 하는데 두 번째 값이 같을 때에는 첫 번째 값을 기준으로 오름차순
points.sort(key = lambda x: (x[1], x[0]))

# 두 번째 값을 기준으로 내림차순으로 정렬을 하는데, 두 번째 값이 같을 때에는 첫 번째 값을 기준으로 오름차순
points.sort(key = lambda x: (-x[1], x[0]))

# 오로지 두 번째 값을 기준으로만 오름차순 정렬을 하고 첫 번째 값은 그냥 입력받은 순서대로 두고 싶다면
points.sort(key = lambda x: x[1])