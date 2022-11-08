#함수 정의
#0 제거
def removeZero(a):
    cnt = 0
    if set(a) == {0}: return [0]
    for i in a:
        if i == 0: cnt += 1
        else     : break
    return a[cnt:]

#다항식의 나눗셈
def divide_Poly(p, q):
    result = []

    for idx in range(len(p) - len(q) + 1):
        if p[idx] == 0: result.append(0)
        else :
            x = p[idx] // q[0]
            result.append(x)
            for i in range(len(q)):
                p[idx+i] -= q[i] * x

    return removeZero(result), removeZero(p)

#입력
u = list(map(int, input().split()))
g = list(map(int, input().split()))

#연산
f, r = divide_Poly(u[:], g[:])

#출력
for i in f: print(i, end=" ")
print()
for i in r: print(i, end=" ")