## 풀이 1 - 정답
# import sys

# read = sys.stdin.readline
# x = int(read().split()[0])

# cnt = 0
# temp_list = [64]

# for _ in range(7):
#     if sum(temp_list) == x:
#         break

#     a = temp_list.pop()
#     temp_list.append(a/2)
#     if sum(temp_list) < x:
#         temp_list.append(a/2)

#     cnt += 1

# print(len(temp_list))

## 사람들 정답
# 이진수로 나타냈을 때의 1의 개수를 출력(비트마스킹)
print(bin(int(input())).count('1'))