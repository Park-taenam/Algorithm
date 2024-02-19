import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    R, S = sys.stdin.readline().strip().split(" ")
    for i in range(len(S)):
        print(S[i]*int(R), end="")
    print()