def snail(array):
    """
    Given an n x n array, returns the elements of the array in a clockwise spiral order.

    Args:
    - array: list of list of integers, representing the n x n array.

    Returns:
    - list of integers, representing the elements of the array in a clockwise spiral order.
    """
    result = []
    while array:
        # Extract the first row (from left to right)
        result.extend(array.pop(0))

        if array and array[0]:
            # Extract the rightmost column (from top to bottom)
            for row in array:
                result.append(row.pop())

        if array and array[-1]:
            # Extract the bottom row (from right to left)
            result.extend(array.pop()[::-1])

        if array and array[0]:
            # Extract the leftmost column (from bottom to top)
            for row in array[::-1]:
                result.append(row.pop(0))

    return result
