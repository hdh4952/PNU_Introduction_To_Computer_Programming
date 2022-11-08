import string

s = input().split("0")
ans = 0

for now in s:
    cmp = 0

    for w in now:
        if 'a' <= w and w <= 'z':
            cmp += ord(w) - ord('a') + 10
        else:
            cmp += ord(w) - ord('0')

    if ans < cmp:
        ans = cmp

print(ans)