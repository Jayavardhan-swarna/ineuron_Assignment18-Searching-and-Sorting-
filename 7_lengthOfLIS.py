def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))  # Output: 4

nums = [0, 1, 0, 3, 2, 3]
print(lengthOfLIS(nums))  # Output: 4

nums = [7, 7, 7, 7, 7, 7, 7]
print(lengthOfLIS(nums))  # Output: 1
