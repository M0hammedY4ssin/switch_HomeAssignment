'''
Find the median char (half of the letters are smaller than it, and half are bigger) in a string. 
'''

def median_char(string):
    sorted_chars = sorted(string)       # Sort the characters in the string
    mid_index = len(sorted_chars) // 2  # take the middle index
    return sorted_chars[mid_index]