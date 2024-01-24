import sys

N = int(sys.stdin.readline().strip())
cnt = N

for _ in range(N):
    text = sys.stdin.readline().strip()
    
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            pass
        elif text[i] in text[i+1:]:
            cnt -= 1
            break

print(cnt)