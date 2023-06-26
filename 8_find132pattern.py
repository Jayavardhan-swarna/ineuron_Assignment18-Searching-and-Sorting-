def find132pattern(nums):
    stack = []
    s3 = float('-inf')

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < s3:
            return True

        while stack and stack[-1] < nums[i]:
            s3 = stack.pop()

        stack.append(nums[i])

    return False


nums = [1, 2, 3, 4]
print(find132pattern(nums))  # Output: False

nums = [3, 1, 4, 2]
print(find132pattern(nums))  # Output: True

nums = [-1, 3, 2, 0]
print(find132pattern(nums))  # Output: True
