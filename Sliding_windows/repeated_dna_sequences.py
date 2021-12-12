"""
Problem statement: The DNA sequence is composed of a series of nucleotides abbreviated
as 'A', 'C', 'G', and 'T'. Given a string s that represents a DNA sequence, return all
the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
You may return the answer in any order.

Strategy: Sliding windows
"""

def findRepeatedDNASequences(str1: str):
    my_strings = {}
    my_list = []

    for window_start in range(len(str1)):
        if window_start+10 > len(str1):
            break
        current_string = s[window_start:window_start+10]
        if current_string not in my_strings:
            my_strings[current_string] = 0
        my_strings[current_string] += 1
        if my_strings[current_string]>1 and current_string not in my_list:
            my_list.append(current_string)
    return my_list
