import sys
from collections import deque

N = int(sys.stdin.readline().strip())

deq = deque()
for _ in range(N):
    func = sys.stdin.readline().split()
    
    if "push_front" in func[0]:
        deq.appendleft(func[1])
        
    elif "push_back" in func[0]:
        deq.append(func[1])
        
    elif "pop_front" in func[0]:
        if len(deq) == 0:
            print("-1")
        else:
            print(deq.popleft())
            
    elif "pop_back" in func[0]:
        if len(deq) == 0:
            print("-1")
        else:
            print(deq.pop())
            
    elif "size" in func[0]:
        print(len(deq))
        
    elif "empty" in func[0]:
        if len(deq) == 0:
            print("1")
        else:
            print("0")
            
    elif "front" in func[0]:
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[0])
            
    elif "back" in func[0]:
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[len(deq)-1])