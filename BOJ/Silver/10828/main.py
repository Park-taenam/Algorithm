import sys

class stack():
    def __init__(self):
        self.stack = []
    
    def push(self, X):
        return self.stack.append(X)
    
    def pop(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
    def empty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0

    def top(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack[len(self.stack)-1]

N = int(sys.stdin.readline().strip())
s = stack()
for _ in range(N):
    func = sys.stdin.readline().strip()
    
    if "push" in func:
        func, X = func.split(" ")
        s.push(X)
    elif "pop" in func:
        print(s.pop())
    elif "size" in func:
        print(s.size())
    elif "empty" in func:
        print(s.empty())
    elif "top" in func:
        print(s.top())