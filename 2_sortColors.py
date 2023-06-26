def sortColors(nums):
    left = 0
    right = len(nums) - 1
    curr = 0
    
    while curr <= right:
        if nums[curr] == 0:
            nums[curr], nums[left] = nums[left], nums[curr]
            curr += 1
            left += 1
        elif nums[curr] == 1:
            curr += 1
        else:  # nums[curr] == 2
            nums[curr], nums[right] = nums[right], nums[curr]
            right -= 1



nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]

nums = [2, 0, 1]
sortColors(nums)
print(nums)  # Output: [0, 1, 2]
