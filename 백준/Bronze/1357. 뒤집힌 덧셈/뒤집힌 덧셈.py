def Rev(X) :
    X = X[::-1]
    return X

X, Y = map(str, input().split())
sum = str(int(Rev(X)) + int(Rev(Y)))
print(int(Rev(sum)))