while True:
    N = input()
    stack = []
    rest = ''
    if N == '0':
        break
    else:
        for i in N:
            stack.append(i)
        for i in range(len(stack)):
            rest += stack.pop()
        if rest == N:
            print('yes')
        else:
            print('no')