num = [int(input()) for _ in range(10)]
div = []

for i in range(10) :
    div.append(num[i] % 42)

div = set(div)
div = list(div)

print(len(div))