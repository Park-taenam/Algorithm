import sys

N = int(sys.stdin.readline().strip())

for _ in range(N):
    value = sys.stdin.readline().strip()
    while True:
        if '()' in value:
            value = value.replace('()', '')
        else:
            break
    if value=='':
        print('YES')
    else:
        print('NO')