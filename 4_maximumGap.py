def maximumGap(nums):
    if len(nums) < 2:
        return 0

    max_num = max(nums)
    exp = 1
    buckets = [0] * len(nums)

    while exp <= max_num:
        count = [0] * 10

        for num in nums:
            count[num // exp % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            digit = num // exp % 10
            buckets[count[digit] - 1] = num
            count[digit] -= 1

        nums[:] = buckets[:]

        exp *= 10

    max_gap = 0
    for i in range(1, len(nums)):
        max_gap = max(max_gap, nums[i] - nums[i - 1])

    return max_gap



nums = [3, 6, 9, 1]
print(maximumGap(nums))  # Output: 3

nums = [10]
print(maximumGap(nums))  # Output: 0
