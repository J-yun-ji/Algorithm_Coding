word = list(input())
answer = []
slic = []

for i in range(1, len(word)) :
    for j in range(i + 1, len(word)) :
        one = word[:i]
        two = word[i:j]
        three = word[j:]
        one.reverse()
        two.reverse()
        three.reverse()
        slic.append(one + two + three)

for one in slic :
    answer.append(''.join(one))

print(sorted(answer)[0])