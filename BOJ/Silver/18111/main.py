'''python3 - 시간초과 / pypy3 - 정답'''
import sys

n, m, b = map(int, sys.stdin.readline().strip().split())
block = []
for _ in range(n):
    block.append([int(x) for x in sys.stdin.readline().strip().split()])

ans = sys.maxsize
glevel = 0 

for i in range(257):
    use_block = 0
    take_block = 0
    for x in range(n):
        for y in range(m):
            if block[x][y] > i:
                take_block += block[x][y] - i
            else:
                use_block += i - block[x][y]
    
    if use_block > take_block + b:
        continue
    
    cnt = take_block*2 + use_block
    
    if cnt <= ans:
        ans = cnt
        glevel = i

print(ans, glevel)    