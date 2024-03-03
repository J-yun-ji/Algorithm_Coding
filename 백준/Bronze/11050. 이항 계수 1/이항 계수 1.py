N, K = map(int, input().split())
ptn = 1
ptk = 1
ptm = 1

for i in range(N, 1, -1) :
    ptn *= i 
    if i <= K :
        ptk *= i
    if i <= N - K :
        ptm *= i

print(ptn // (ptk * ptm))