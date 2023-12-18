cnt = input()
nums = [int(i) - 100 for i in input().split()]
nums.sort(key=lambda x: abs(x))
print(nums[0] + 100, end=' ')
for i in nums:
    if i >= 0:
        print(i + 100)
        exit()
print(-1)