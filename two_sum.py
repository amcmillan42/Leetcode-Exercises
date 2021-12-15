"""
Problem statement: Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Strategy: Pivot on one element in the array to reduce complexity to O(N),
and do a space time trade off to increase speed.
"""

def two_sum(nums, target):
    my_dict = {nums[i]: i for i in range(len(nums))}
    for i in range(len(nums)):
        current_num = target-nums[i]
        if current_num in my_dict and my_dict[current_num]!=i:
            return (i, my_dict[current_num])
