import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().strip().split())

    a = str(N%H) if N%H!=0 else str(H)
    b = str(N//H+1) if N%H!=0 else str(N//H)

    if len(b)==1:
        b = '0'+b
    
    print(a+b)