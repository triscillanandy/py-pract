def minSubarrayLen(s, nums):
    if not nums:
        return 0

    min_len = float('inf')  # Initialize with positive infinity
    left = 0
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= s:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0


target_sum = 7
array = [2, 3, 1, 2, 4, 3]
result = minSubarrayLen(target_sum, array)
print(result)  # Output: 2 (the subarray [4, 3] has a sum of 7)
