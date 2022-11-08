rps = {'R': 0, 'P': 0, 'S': 0}
a, b = input().split()
rps[a] = rps[b] = 1
if rps['R'] == 1 and rps['P'] == 1:
    print('P')
elif rps['R'] == 1 and rps['S'] == 1:
    print('R')
elif rps['P'] == 1 and rps['S'] == 1:
    print('S')
else:
    print('D')
