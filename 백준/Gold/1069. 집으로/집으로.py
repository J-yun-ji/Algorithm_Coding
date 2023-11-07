import sys
input = sys.stdin.readline

X, Y, D, T = map(int, input().split())

distance = (X*X + Y*Y) ** 0.5

if T > D :
    print(distance)

else :
    num = distance // D
    print(min(T*num+distance-D*num, T*(num+1) if D < distance else min(distance, T+D-distance, 2*T)))