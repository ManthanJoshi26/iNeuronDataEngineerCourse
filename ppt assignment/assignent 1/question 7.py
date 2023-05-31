def moveZeroes(nums):
    left = 0   
    right = 0   
    

    while right < len(nums):

        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        
        right += 1
    
    print(nums)

l = list(map(int,input().split()))

moveZeroes(l)