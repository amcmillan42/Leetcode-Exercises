"""
Problem statement: Given an array of sorted numbers, remove all duplicates from it.
You should not use any extra space; after removing the duplicates in-place return
the length of the subarray that has no duplicate in it.

Strategy: Two pointers
"""

def remove_duplicates(arr):
    N = len(arr)
    right = 1
    left = 1
    while left < N:
        if arr[right-1] != arr[left]:
            arr[right] = arr[left]
            right += 1
        left += 1
    return right

print(remove_duplicates([2,3,3,3,6,9,9]))
print(remove_duplicates([2,2,2,11]))
