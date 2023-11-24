N, m, M, T, R = map(int, input().split())
count = t = 0
now = m

while count < N:
    if m+T > M:
        break
    if now + T <= M:
        now += T
        count += 1
    else:
        now = max(now-R, m)
    t += 1
print(t if count == N else -1)