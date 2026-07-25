n = int(input())

if n%5 == 0:
    ans = n//5
    print(ans)
else:
    ans = (n//5)+1
    print(ans)