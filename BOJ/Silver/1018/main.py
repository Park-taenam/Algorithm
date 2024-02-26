import sys

board_1 = [[0 for _ in range(8)] for _ in range(8)]
board_2 = [[0 for _ in range(8)] for _ in range(8)]

N, M = map(int, sys.stdin.readline().strip().split(" "))
board = [[0 for _ in range(M)] for _ in range(N)]
for n in range(N):
    block = sys.stdin.readline().strip()
    for m in range(M):
        board[n][m] = block[m]

for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            board_1[i][j] = 'B'
        else:
            board_1[i][j] = 'W'

for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            board_2[i][j] = 'W'
        else:
            board_2[i][j] = 'B'

result = 64
for i in range(N-7):
    for j in range(M-7):
        cnt_1 = 0
        cnt_2 = 0
        for n in range(8):
            for m in range(8):
                if board[i+n][j+m] != board_1[n][m]:
                    cnt_1 += 1
                if board[i+n][j+m] != board_2[n][m]:
                    cnt_2 += 1
        if result > cnt_1:
            result = cnt_1
        if result > cnt_2:
            result = cnt_2   
                
print(result)