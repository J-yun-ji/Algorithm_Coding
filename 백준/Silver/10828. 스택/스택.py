import sys
input = sys.stdin.readline

stack = []
N = int(input())

for i in range(N) :
    num = input().strip()
    if num[:4] == "push" : 
        stack.append(int(num[5:]))
    elif num == "pop" :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1]) 
            stack.pop()
    elif num == "size" :
        print(len(stack))
    elif num == "empty" :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif num == "top" :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])