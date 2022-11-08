m = int(input())
mi = list(map(int, input().split()))
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
newYear = input()
newYearIdx = week.index(newYear)
ans = list()

for i in range(3):
    cnt = 0
    qm, qd = map(int, input().split())
    if qm > m or qd > mi[qm-1]:
        ans.append("None")
        continue
    for miIdx in range(0, qm-1):
        cnt += mi[miIdx]
    cnt += qd-1
    cnt += newYearIdx
    cnt %= 7
    ans.append(week[cnt])

for s in ans:
    print(s)