def smallest_subarray_with_sum(arr, x):
    n = len(arr)
    min_len = n + 1  # Initialize min_len to a large value
    current_sum = 0
    start = 0
    subarray_start = 0  # Initialize the start index of the smallest subarray
    subarray_end = 0  # Initialize the end index of the smallest subarray

    # Loop through the array using the 'end' pointer
    for end in range(n):
        current_sum += arr[end]  # Add the current element to the sum

        # While conddition the current sum is greater than the target 'x', move the 'start' pointer
        while current_sum > x:
            # Checking if the current subarray length is smaller than the current minimum length
            if end - start + 1 < min_len:
                min_len = end - start + 1  # Update min_len
                subarray_start = start  # Update the start index of the smallest subarray
                subarray_end = end  # Update the end index of the smallest subarray
            current_sum -= arr[start]  # Subtract the element at 'start' from the sum
            start += 1  # Move the 'start' pointer to the right

    # If min_len is still n + 1, it means no subarray was found, so return a message
    if min_len == n + 1:
        return "No subarray found"

    # elsewe are  returning  the minimum length and the subarray that satisfies the condition
    return min_len, arr[subarray_start:subarray_end + 1]


arr = [1, 4, 45, 6, 0, 19]
x = 51
result_length, result_subarray = smallest_subarray_with_sum(arr, x)
print("Smallest subarray length with sum > x:", result_length)
print("Minimum length subarray:", result_subarray)
