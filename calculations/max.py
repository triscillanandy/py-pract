# write a function called maxSubArraySum which accepts an array of integers and a number called n.
# The n should calculate the maximum sum of n consecutive elements in the array
# using the sliding window technique

def max_subarray_sum(arr, window_size):
    if window_size > len(arr):
        return None

    max_sum = 0
    temp_sum = 0

    # Calculate the initial sum of the first 'window_size' elements
    for i in range(window_size):
        max_sum += arr[i]

    temp_sum = max_sum

    # Slide the window and update max_sum as needed
    for i in range(window_size, len(arr)):
        temp_sum = temp_sum - arr[i - window_size] + arr[i]
        max_sum = max(max_sum, temp_sum)

    return max_sum



print(max_subarray_sum([],4))
