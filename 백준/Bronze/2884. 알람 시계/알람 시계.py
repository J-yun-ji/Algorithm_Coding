H, M = map(int, input().split()) # 10 10

if M < 45 :
  if H == 0 :
    H = 24
  H -= 1
  M = 60 - (45 - M) # 45-10= 35
else :
  M -= 45
print(H, M)
