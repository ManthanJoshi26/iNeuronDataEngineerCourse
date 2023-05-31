nums = list(map(int,input().split()))
ans = []
target = int(input())
for i in range(len(nums) - 1):
    diff = target - nums[i]

    if diff in nums:
        ans.append(nums[i])
        ans.append(diff)
        break

print(ans)       