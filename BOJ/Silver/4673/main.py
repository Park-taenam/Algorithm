import sys

# # 풀이 1 - 시간초과
# def self_num(n):
#     temp_list = [int(x) for x in str(n)]
#     return int(n)+sum(temp_list)

# n = 1
# while n<=10000: 
#     tf = True
#     for i in range(1,n):
#         if n == int(self_num(i)):
#             tf = False
#             break
#     if tf:
#         print(n)
#     n += 1 

# 풀이 2 - 블로그
natural_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

self_num = sorted(natural_num - generated_num)
for i in self_num:
    print(i)