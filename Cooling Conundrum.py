import math

t = int(input())

for i in range(t):
    x,y = map(int, input().split())

    ans = 0

    for i in range(x, y, -1):
        ans = ans + math.ceil(i / 10)

    print(ans)