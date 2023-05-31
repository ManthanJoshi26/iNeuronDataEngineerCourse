l = list(map(int,input().split()))

l.sort()
ans = []

for i in range(len(l)-1):
    if l[i] == l[i+1]:
        ans.append(l[i])
        ans.append(i+2)

print(ans)