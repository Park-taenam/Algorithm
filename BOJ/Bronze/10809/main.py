# # 풀이 2
# import sys

# S = sys.stdin.readline().strip()
# check = [-1]*26

# for i, s in enumerate(S):
#     if check[ord(s)-97] != -1:
#         continue
#     else:
#         check[ord(s)-97] = i

# for i in check:
#     print(i, end = " ")

# 풀이 2
S = input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(x), end = ' ')