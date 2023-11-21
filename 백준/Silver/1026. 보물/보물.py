N = int(input())
 
Array = list(map(int, input().split()))
Brray = list(map(int, input().split()))

sorted_a = sorted(Array, reverse=True)
sorted_b = sorted(Brray)

sum = 0
for i in range(N) :
    sum += sorted_a[i] * sorted_b[i]

print(sum)