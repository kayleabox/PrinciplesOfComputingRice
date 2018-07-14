"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    merged_with_previous = False
    line_without_zeros = [value for value in line if value != 0]
    merged_line = []
    
    try_merge(merged_with_previous, line_without_zeros, merged_line)
    while len(line) - len(merged_line) > 0:
        merged_line.append(0)
    return merged_line;

def try_merge(merged_w_previous, line_wo_zeros, merged_line):
    """
    Attempts to merge each number in an array with the one after it.
    If the number was already merged with the one before it, 
    no merge will occur.
    """
    for index in range(len(line_wo_zeros)):
        if index < len(line_wo_zeros) - 1 and line_wo_zeros[index] == line_wo_zeros[index + 1]:
            merged_w_previous = merge_if_not_merged_with_previous(merged_w_previous, merged_line, line_wo_zeros, index)
        else: 
            merged_w_previous = append_to_line_if_not_merged(merged_w_previous, merged_line, line_wo_zeros, index)

def merge_if_not_merged_with_previous(merged_with_previous, merged_line, line_without_zeros, index):
    """
    Merges the number at the current index with the number 
    at index + 1 if the number at index has not been merged
    already. Then appends the merged number to a placeholder.
    """
    if merged_with_previous == False:
        merged_line.append(line_without_zeros[index] + line_without_zeros[index + 1])
        return True
    else:
        return False

def append_to_line_if_not_merged(merged_with_previous, merged_line, line_without_zeros, index):
    """
    Appends numbers that are not eligible for merging with their
    neighbors to the placeholder array.
    """
    if merged_with_previous != True:
        merged_line.append(line_without_zeros[index])
    return False