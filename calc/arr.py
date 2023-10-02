

# This implementation has a time complexity of O(n)
def maxSubarraySum(arr, windowSize):
    # Check if the windowSize is larger than the array length
    if windowSize > len(arr):
        return None

    # Initialize max_sum and temp with 0
    max_sum = 0
    temp = max_sum

    # Calculate the initial sum of the first window of size windowSize
    for i in range(windowSize):
        max_sum += arr[i]

    # Assign the initial max_sum value to temp
    temp = max_sum

    # Iterate through the array starting from the windowSize position
    for i in range(windowSize, len(arr)):
        # Update temp by subtracting the leftmost element of the previous window
        # and adding the rightmost element of the current window
        temp = temp - arr[i - windowSize] + arr[i]

        # Update max_sum with the maximum of max_sum and temp
        max_sum = max(max_sum, temp)

    # Return the maximum sum found
    return max_sum

# Test the maxSubarraySum function with an example
print(maxSubarraySum([3, 4, 5, 1, 6, 1, 6, 2, 8, 1, 90, 0, 2, 3, 6, 34], 3))
