f = list(map(int, input().split()))
g = list(map(int, input().split()))

def mul(p, q):
    reversed(p); reversed(q)
    w = [0 for _ in range(len(p)+len(q)-1)]

    for degP, valP in enumerate(p):
        for degQ, valQ in enumerate(q):
            w[degP+degQ] += valP * valQ

    reversed(w)
    return w

for i in mul(f, g): print(i, end=" ")