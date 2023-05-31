l = list(map(int,input().split()))


d = {}


for i in l:
    if i in d:
        d[i] += 1
    
    else:
        d[i] = 1

for k,v in d.items():
    if v == 2:
        print("True")
        break
    else:
        print("False")        