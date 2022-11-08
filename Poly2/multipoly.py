f = list(map(int, input().split()))

def mul(p, q):
    reversed(p); reversed(q)
    w = [0 for _ in range(len(p)+len(q)-1)]

    for degP, valP in enumerate(p):
        for degQ, valQ in enumerate(q):
            w[degP+degQ] += valP * valQ

    reversed(w)
    return w

while True:
    try:
        g = list(map(int, input().split()))
        f = mul(f, g)
    except:
        break

if f[0] == 0:
    print("0")
else :
    for i in f: print(i, end=" ")