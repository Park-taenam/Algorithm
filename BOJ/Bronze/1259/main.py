import sys

while True:
    test = sys.stdin.readline().strip()
    if test == "0":
        break
    print('yes' if test == test[::-1] else 'no')