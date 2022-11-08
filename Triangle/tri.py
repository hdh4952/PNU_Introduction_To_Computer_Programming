a = list(map(int, input().split()))
a.sort()

if(a[0] + a[1] <= a[2]):
    ans = 0
else:
    if a[2]**2 == a[0]**2 + a[1]**2:
        ans = 1
    elif a[2]**2 > a[0]**2 + a[1]**2:
        ans = 2
    else:
        ans = 3

print(ans)