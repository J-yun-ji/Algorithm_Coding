firstCol = input()
secondCol = input()
thirdCol = input()
Color = {'black' : 0, 'brown' : 1, 'red' : 2, 'orange' : 3,
'yellow' : 4, 'green' : 5, 'blue' : 6, 'violet' : 7, 'grey' : 8, 'white' : 9}
j = 1
num3 = 1
num2 = 0
num1 = 0

print((10 * Color[firstCol] +  Color[secondCol]) * (10 ** Color[thirdCol]))