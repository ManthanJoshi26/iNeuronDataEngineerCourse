l = list(map(int,input().split()))

k = int(input())
cnt = 0

for i in range(len(l)):
    if l[i] == k:
        l[i] = '*'
    else :
        cnt += 1
print(cnt)