def smallest_subarray_with_sum(arr, x):
    n = len(arr)
    min_len = n + 1  # Initialize min_len to a large value
    current_sum = 0
    start = 0
    subarray_start = 0  # Initialize the start index of the smallest subarray
    subarray_end = 0  # Initialize the end index of the smallest subarray

    for end in range(n):
        current_sum += arr[end]

        while current_sum > x:
            if end - start + 1 < min_len:
                min_len = end - start + 1
                subarray_start = start
                subarray_end = end
            current_sum -= arr[start]
            start += 1

    if min_len == n + 1:
        return "No subarray found"
    
    return min_len, arr[subarray_start:subarray_end+1]

# Example usage:
arr = [1,10,5,2,7]
x = 9
result_length, result_subarray = smallest_subarray_with_sum(arr, x)
print("Smallest subarray length with sum > x:", result_length)
print("Minimum length subarray:", result_subarray)
