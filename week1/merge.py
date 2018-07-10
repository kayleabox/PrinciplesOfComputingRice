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
    for index in range(len(line_without_zeros)):
        if index < len(line_without_zeros) - 1 and line_without_zeros[index] == line_without_zeros[index + 1]:
            if merged_with_previous == False:
                merged_line.append(line_without_zeros[index] + line_without_zeros[index + 1])
                merged_with_previous = True
            else:
                merged_with_previous = False
        else: 
            if merged_with_previous != True:
                merged_line.append(line_without_zeros[index])
            merged_with_previous = False
    while len(line) - len(merged_line) > 0:
        merged_line.append(0)
    return merged_line;