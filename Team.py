n = int(input())

count = 0

for i in range(n):
    f,v,t = map(int, input().split())
    if f+v+t>=2:
        count += 1

print(count)