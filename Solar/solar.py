n, m = map(int, input().split())
arr = [[0]*(m+1) for _ in range(n+1)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x = 1
y = 1
direction = 0
ans = list()

for num in range (1, n*m+1):
    arr[x][y] = num
    nx = x + dx[direction]
    ny = y + dy[direction]

    if not(0 < nx and nx <= n and 0 < ny and ny <= m) or arr[nx][ny] != 0:
        direction += 1
        direction %= 4
        nx = x + dx[direction]
        ny = y + dy[direction]

    x = nx
    y = ny

for _ in range(4):
    q = list(map(int, input().split()))
    isCheck = False
    if len(q) == 1:
        if q[0] > n*m:
            ans.append([0, 0])
            continue

        for i in range(1, n+1):
            for j in range(1, m+1):
                if arr[i][j] == q[0]:
                    ans.append([i, j])
                    isCheck = True
                    break
            if isCheck:
                break

    elif len(q) == 2:
        cx = q[0]
        cy = q[1]
        if not(0 < cx and cx <= n and 0 < cy and cy <= m):
            ans.append([0, 0])
            continue

        ans.append([arr[cx][cy]])

for idx in range(4):
    for i in ans[idx]:
        print(i, end=' ')
    print("")