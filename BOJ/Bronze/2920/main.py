import sys

test = sys.stdin.readline().strip()

if test == "1 2 3 4 5 6 7 8":
    print("ascending")
elif test == "8 7 6 5 4 3 2 1":
    print("descending")
else:
    print("mixed")