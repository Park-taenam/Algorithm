import sys

for i in range(3):
    x = sys.stdin.readline().strip()
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
        n = int(x)+3-i
        break

if n%3==0 and n%5==0:
    print('FizzBuzz')
elif n%3==0 and n%5!=0:
    print('Fizz')
elif n%3!=0 and n%5==0:
    print('Buzz')
else:
    print(n)