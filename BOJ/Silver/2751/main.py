'''
- input 받을 때 부터 int 형으로 안받으니 틀렸었음
'''
import sys

N = int(sys.stdin.readline().strip())

x = []
for _ in range(N):
    x.append(int(sys.stdin.readline().strip()))
    
for v in sorted(x):
    print(v, end="\n")