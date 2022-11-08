def solve():
    a = input()
    isChar = False
    d = list()
    c = list()
    s = list()
    preChar = 'n'

    for i in a:
        if not('0' <= i and i <= '9'):
            isChar = True
        else:
            d.append(int(i))

    if isChar:
        print("-1")
        return

    for i in range(len(a)-1):
        if d[i] == d[i+1]:
            c.append("e")
        elif d[i] + 1 == d[i+1]:
            c.append("u")
        elif d[i] - 1 == d[i+1]:
            c.append("d")
        else:
            c.append("n")

    for i in range(len(a)-1):
        if c[i] == 'n':
            s.append(0)
        elif c[i] == preChar:
            s.append(s[i-1] + 1)
        else:
            s.append(1)
            preChar = c[i]

    print(sum(s))
solve()