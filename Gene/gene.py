import sys

f = open("genome.txt", 'r')
data = f.read().replace('\n', '')
f.close()

Si = sys.stdin.readline().split()
Ei = sys.stdin.readline().split()
SiIndex = []
EiIndex = []
ans = "None"

for i in range(len(Si)):
    for j in range(len(data)):
        if len(data)-len(Si[i]) < j: break
        isExist = True
        for k in range(len(Si[i])):
            if data[j+k] != Si[i][k]:
                isExist = False
                break

        if isExist:
            SiIndex.append((j, j+len(Si[i])))

for i in range(len(Ei)):
    for j in range(len(data)):
        if len(data)-len(Ei[i]) <= j: break
        isExist = True
        for k in range(len(Ei[i])):
            if data[j+k] != Ei[i][k]:
                isExist = False
                break

        if isExist:
            EiIndex.append((j, j+len(Ei[i])))

for i in range(len(SiIndex)):
    for j in range(len(EiIndex)):
        if SiIndex[i][1] > EiIndex[j][0]: continue
        isExist = True
        left  = SiIndex[i][0] + 1
        right = EiIndex[j][1] - 1

        for k in range(len(SiIndex)):
            if i == k: continue
            if left <= SiIndex[k][0] and SiIndex[k][1] <= right:
                isExist = False
                break

        for k in range(len(EiIndex)):
            if j == k: continue
            if left <= EiIndex[k][0] and EiIndex[k][1] <= right:
                isExist = False
                break

        if isExist:
            check = data[left-1:right+1]
            if ans == "None": ans = check[:]
            elif len(ans) >  len(check): ans = check[:]
            elif len(ans) == len(check):
                if ans > check: ans = check
print(ans)