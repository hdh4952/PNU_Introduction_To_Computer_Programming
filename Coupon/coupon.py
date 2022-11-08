k, c = map(int, input().split())
menuPrice = []
vis = [False for _ in range(k)]
ans = []
selected_Menu = []

def solve(coupon, start):
    minValue = 50001
    for i in range(k):
        if vis[i] == True or menuPrice[i] > coupon: continue
        minValue = menuPrice[i]
        if i < start: continue
        vis[i] = True
        selected_Menu.append(i+1)
        solve(coupon - menuPrice[i], i+1)
        vis[i] = False
        selected_Menu.pop()
    
    if minValue > coupon: ans.append(selected_Menu[:])

for _ in range(k): menuPrice.append(int(input()))
solve(c, 0)
for line in ans: print(*line)