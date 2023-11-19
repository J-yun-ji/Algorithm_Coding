N = int(input())

for _ in range(N) :
    a, b = map(int, input().split())
    A = a % 10

    if A == 0 : 
        print(10)
    elif A in [1, 5, 6] :
        print(A)
    elif A in [4, 9] :
        B = b % 2
        if B == 0 :
            print(A * A % 10)
        else :
            print(A)
    else :
        B = b % 4
        if B == 0 :
            print(A ** 4 % 10)
        else :
            print(A ** B % 10)