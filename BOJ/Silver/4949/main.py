import sys

# 풀이 1 - stack
while True:
    text = sys.stdin.readline().replace('\n','')
    if text == ".":
        break
    stack = []
    answer = 'yes'

    for i in text:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                answer = 'no'
                break 
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                answer = 'no'
                break
        else:
            continue
    
    if len(stack):
        answer = 'no'
    print(answer)

# 풀이 2 - string
while True:
    text = sys.stdin.readline().replace('\n','')
    if text == ".":
        break
    check = ''

    for s in text:
        if s not in '()[]':
            continue
        else:
            check += s
    
    for _ in range(len(check)//2+1):
        check = check.replace('()', '')
        check = check.replace('[]', '')
    
    if len(check):
        print('no')
    else:
        print('yes')
