n,m,a = map(int, input().split())

'''c = n//a
d = m//a

if n%a !=0:
    c = c + 1
if m%a !=0:
    d = d +1
ans = c+d'''

x = ((n+a)-1)/a
y = ((m+a)-1)/a

ans = x+y

print(ans)