"""
Problem statement: Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.

Strategy: Two pointers
"""

def remove_duplicates_two(arr):
    N = len(arr)
    left = 1
    right = 1
    freq = 1

    while left < N:
        if arr[right-1] == arr[left]:
            freq +=1
        if freq > 2:
            left +=1
            freq = 1
        else:
            arr[right] = arr[left]
            right += 1
            left += 1
    return right

print(remove_duplicates_two([1,1,1,2,2,3]))
