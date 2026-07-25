x = int(input())
a = 0

if x>=1:
    for i in range(1, x+1):
        a = a+i
else:
    for i in range(x,2):
        a = a+i
print(a)
