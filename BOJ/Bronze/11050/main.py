import sys
from math import comb

N, K = map(int, sys.stdin.readline().split())
print(comb(N,K))