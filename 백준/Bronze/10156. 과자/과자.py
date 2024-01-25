K, N, M = map(int, input().split())

if (M < K * N) :
  print((M - (K*N)) * -1)
else :
  print("0")