def myfunc(nums):
    # Get the length of the input array
    n = len(nums)
    
    # Initialize a list to store the prefix sum of the elements
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]

    # Calculate the prefix sum for each element in the array
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    # Initialize variables to store the index and minimum difference
    min_index = 0
    min_diff = float('inf')

    # Iterate through each possible index
    for i in range(n - 1):
        # Calculate the sum of elements on the left and right of the index
        left_sum = prefix_sum[i]
        right_sum = prefix_sum[n - 1] - prefix_sum[i]
        
        # Calculate the average of the elements on the left and right
        left_avg = left_sum // (i + 1)
        right_avg = right_sum // (n - i - 1)
        
        # Calculate the absolute difference between the left and right averages
        diff = abs(left_avg - right_avg)

        # Update the minimum difference and index if a smaller difference is found
        if diff < min_diff or (diff == min_diff and i < min_index):
            min_diff = diff
            min_index = i

    # Return the index with the minimum average difference
    return min_index


nums1 = [2, 5, 3, 9, 5, 3]
print(myfunc(nums1))
