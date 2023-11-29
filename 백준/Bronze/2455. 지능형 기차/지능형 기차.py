on = []
person = 0

for _ in range(4):
    a, b = map(int, input().split())
    person += b
    person -= a
    on.append(person)

print(max(on))