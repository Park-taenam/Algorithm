import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())

    results = [[0 for _ in range(n)] for _ in range(k+1)]

    for a in range(0,k+1):
        for b in range(0,n):
            if a==0:
                results[a][b] = b+1
            else:
                results[a][b] = sum([x for x in results[a-1][:b+1]])

    print(results[k][n-1])