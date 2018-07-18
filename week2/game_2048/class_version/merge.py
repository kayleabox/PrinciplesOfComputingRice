def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    non_zeros = try_merge([value for value in line if value != 0])
    zeros = [0 for dummy_num in range(len(line) - len(non_zeros))]
    return (non_zeros + zeros)

def try_merge(line_wo_zeros):
    """
    Attempts to merge each number in an array with the one after it.
    If the number was already merged with the one before it, 
    no merge will occur.
    """
    return [ get_new_value(line_wo_zeros, index, value) for index, value in enumerate(line_wo_zeros)]

def get_new_value(line_wo_zeros, index, value):
    """
    Return the value multiplied by 2 if it can be merged with the next one 
    and remove the element at the next index
    Return the value if it cannot be merged with the next one
    """
    if index < len(line_wo_zeros) - 1 and value == line_wo_zeros[index + 1]:
        line_wo_zeros.pop(index + 1)
        return value * 2 
    return value