"""
Problem statement: Given an array of positive integers (nums) and a positive integer
(target), return the minimal length of a contiguous subarray of which the sum is
greater than or equal to target.

Strategy: Sliding window.
"""

def min_subarray_length(target: int, arr: list):
    min_length = float(inf)
    current_sum = 0
    window_start = 0
    for window_end in range(len(arr)):
        current_sum += arr[window_end]
        if current_sum >= target:
            min_length = min(min_length, current_sum)
            current_sum -= arr[window_start]
            window_start += 1
    if min_length == float(inf):
        return 0
    else:
        return min_length
