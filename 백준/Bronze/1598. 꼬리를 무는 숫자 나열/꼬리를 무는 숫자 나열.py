num1, num2 = map(int, input().split())

num1 -= 1
num2 -= 1
one = abs((num1 // 4) - (num2 // 4))
two = abs((num1 % 4) - (num2 % 4))
print(one + two)
