import sys

x = sys.stdin.readline().strip()

alphabet_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for alphabet in alphabet_list:
    temp = len(x)
    x = x.replace(alphabet, ",")

print(len(x))