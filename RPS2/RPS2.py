isR = False
isP = False
isS = False
li = input().split()

for i in li:
    if i == 'R':
        isR = True
    elif i == 'P':
        isP = True
    elif i == 'S':
        isS = True

if isR and isP and not isS:
    print("P")
elif isR and not isP and isS:
    print("R")
elif not isR and isP and isS:
    print("S")
else:
    print("D")