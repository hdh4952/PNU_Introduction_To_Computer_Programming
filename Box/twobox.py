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
    result = [["NULL", "NULL", "NULL"], ["NULL", "POINT", "LINE"], ["NULL", "LINE", "FACE"]]
    s = list(map(int, input().split()))
    x = cmp([s[0], s[2]], [s[4], s[6]])
    y = cmp([s[1], s[3]], [s[5], s[7]])
    return result[x][y]

for _ in range(4):
    print(solve())