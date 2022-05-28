nums = list(map(int, input().split()))

sort_nums = sorted(nums)

if sort_nums[1] == nums[1]:
    print("Yes")
else:
    print("No")