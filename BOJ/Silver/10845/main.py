import sys
from collections import deque

N = int(sys.stdin.readline().strip())

deq = deque()
for _ in range(N):
    func = sys.stdin.readline().strip()
    
    if "push" in func:
        func, X = func.split(" ")
        deq.append(X)
    elif "pop" in func:
        if len(deq) == 0:
            print("-1")
        else:
            print(deq.popleft())
    elif "size" in func:
        print(len(deq))
    elif "empty" in func:
        if len(deq) == 0:
            print("1")
        else:
            print("0")
    elif "front" in func:
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[0])
    elif "back" in func:
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[len(deq)-1])
