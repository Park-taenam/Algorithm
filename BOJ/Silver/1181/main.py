'''
처음에 유니코드 값 사용해서 풀려고 했음 (ord)
'''
import sys

N = int(sys.stdin.readline())

words = []
for _ in range(N):
    words.append(sys.stdin.readline().strip())

## 풀이 1 - 블로그 참조
words = list(set(words))

# 1순위: 길이 순 정렬 / 2순위: 사전 순 정렬
words = sorted(words, key = lambda x: [len(x), x])

for word in words:
    print(word)