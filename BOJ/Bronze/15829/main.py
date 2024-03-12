import sys
from string import ascii_lowercase

l = int(sys.stdin.readline().strip())
text = sys.stdin.readline().strip()

r, m = 31, 1234567891
result = 0

# 풀이 1 - 50점
alpha_dict = {}
for i, alpha in enumerate(ascii_lowercase):
    alpha_dict[alpha] = i+1

for i in range(l):
    a = alpha_dict[text[i]]
    result += a*(r**i)%m

print(result)

# 풀이 2 - 100점
for i in range(l):
    a = ord(text[i])-96
    result += a*(r**i)

print(result)