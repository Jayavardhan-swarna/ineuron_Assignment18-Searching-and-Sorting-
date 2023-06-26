def containsDuplicate(nums):
    unique = set()

    for num in nums:
        if num in unique:
            return True
        else:
            unique.add(num)

    return False


nums = [1, 2, 3, 1]
print(containsDuplicate(nums))  # Output: True

nums = [1, 2, 3, 4]
print(containsDuplicate(nums))  # Output: False

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicate(nums))  # Output: True
