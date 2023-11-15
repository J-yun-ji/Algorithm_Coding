while 1:
    li = list(map(int, input().split()))
    if li[0] == 0:
        break
    n = 1
    for i in range(li[0]):
        sss = li[2*i + 1]
        ppp = li[2*i + 2]
        n = n * sss - ppp
    print(n)