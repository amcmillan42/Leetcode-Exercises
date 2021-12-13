"""
Problem statement: Given n non-negative integers a1, a2, ..., an , where each
represents a point at coordinate (i, ai). n vertical lines are drawn such that
 the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which,
 together with the x-axis forms a container, such that the container contains the most water.

 Strategy: Two pointer technique. The key idea is that the area will only increase
 in the direction of a height increase. Therefore, slide the left or right endpoint
 pointers according to which direction yields this height increase.
"""

def max_water_area(height):
    start_index, end_index = 0, len(height)-1
    max_area = 0
    while start_index < end_index:
        current_height = min(height[start_index], height[end_index])
        current_area = current_height*(end_index-start_index)
        max_area = max(max_area, current_area)
        if height[start_index] < height[end_index]:
            start_index += 1
        elif height[start_index] >= height[end_index]:
            end_index += 1
    return max_area
