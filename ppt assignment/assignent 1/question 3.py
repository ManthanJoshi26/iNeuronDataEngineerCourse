def binarySearch(l,t):
    
    head = 0
    tail = len(l) - 1 
    
    while head<= tail:
        mid = head + (tail -head) //2

        if(l[mid] == t):
            return mid;
        
        elif l[mid] < t:
            head = mid + 1
        else:
            tail = mid - 1
    
    return head

l = list(map(int,input().split()))

t = int(input())

ans = binarySearch(l,t)

print(ans)
