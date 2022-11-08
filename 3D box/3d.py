def cmp(a, b):
    l1, r1, l2, r2 = a + b
    if l2 < l1:
        l1, r1, l2, r2 = l2, r2, l1, r1

    if r1 < l2:
        return 0
    elif r1 == l2:
        return 1
    else:
        return 2

def solve():
    x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4 = map(int, input().split())
    x = cmp([x1, x2], [x3, x4])
    y = cmp([y1, y2], [y3, y4])
    z = cmp([z1, z2], [z3, z4])
    A = sorted([x, y, z])

    if A == [2, 2, 2]:
        return "VOL"
    elif A == [1, 2, 2]:
        return "FACE"
    elif A == [1, 1, 2]:
        return "LINE"
    elif A == [1, 1, 1]:
        return "POINT"
    else:
        return "NULL"

for _ in range(4):
    print(solve())