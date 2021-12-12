"""
Problem Statement: Given a string str1, find the length of the longest substring
without repeating characters

Strategy: Use the sliding window approach. That is, keep a hash table of the characters
that have already appeared and their frequency. If that frequency is greater than 1,
delete characters, starting at the beginning of str1, until all frequencies are equal to 1.
Store the max length on each iteration. 
"""

def longest_nonrepeat_substring(str1: str):
    char_freq = {}
    max_length = 0
    window_start = 0
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1
        while char_freq[right_char] > 1:
            char_left = str1[window_start]
            char_freq[window_start] -= 1
            if char_freq[window_start] == 0:
                del char_freq[window_start]
            window_start += 1
        max_length = max(max_length, window_end-window_start+1)
    return max_length
