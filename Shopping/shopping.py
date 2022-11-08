customer_name = []
shopping_list = []
similarity_list = []
ans = []
while True:
    try:
        data = input().split()
        if data[0] in customer_name:
            idx = customer_name.index(data[0])
            for i in data[1:]: shopping_list[idx].append(i)
        else:
            customer_name.append(data[0])
            shopping_list.append(data[1:])
    except:
        break

for i in range(len(shopping_list) - 1):
    for j in range(i+1, len(shopping_list)):
        similarity = len(set(shopping_list[i]) & set(shopping_list[j])) / (len(set(shopping_list[i]) | set(shopping_list[j])) + 1)
        similarity_list.append((similarity, customer_name[i], customer_name[j]))

similarity_list.sort(key = lambda x : -x[0])
value = similarity_list[0][0]

for i in range(len(similarity_list)):
    if similarity_list[i][0] >= value:
        ans.append(sorted(similarity_list[i][1:]))

ans.sort()
for x in ans: print(x[0], x[1])