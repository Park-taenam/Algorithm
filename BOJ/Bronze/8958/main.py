import sys

N = int(sys.stdin.readline().strip())

for _ in range(N):
    test = sys.stdin.readline().strip()
    score = 0

    for i in range(len(test)):
        if test[i] == "O":
            k = 0
            while test[i-k] == "O":
                score += 1
                if i-k == 0:
                    break
                k += 1

    print(score)