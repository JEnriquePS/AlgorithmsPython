def max_value_of_integer_sequences(arr):
    """
    Find the maximum value in the given array using a partial bubble sort approach.

    This function partially sorts the input array using a bubble sort-like algorithm,
    moving the largest element to the end of the array. It then returns this largest element.

    Parameters:
    arr (list): A list of comparable elements (typically numbers).

    Returns:
    The maximum value in the input array.

    Note:
    - This function modifies the input array.
    - The time complexity of this function is O(n^2), where n is the length of the array.
    - For large arrays, this method is not efficient. Consider using Python's built-in max()
      function or a linear scan for better performance.

    Example:
    >>> max_value_of_integer_sequences([60, 90, 100, 80, 70])
    100
    """
    length = len(arr)
    for i in range(length - 1):
        if arr[i] > arr[i + 1]:
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
    maximum_value = arr[length - 1]
    return maximum_value


def max_value_linear_scan(arr):
    """
    Find the maximum value in an array using a linear scan approach.

    This function performs a single pass through the input array, comparing each
    element with the current maximum value. It efficiently finds the maximum
    value without modifying the original array.

    Parameters:
    arr (list): An array (list) of comparable elements, typically numbers.
                Can be empty.

    Returns:
    The maximum value in the array. If the array is empty, returns None.

    Time Complexity: O(n), where n is the number of elements in the array.
    Space Complexity: O(1), as it uses only a constant amount of extra space.

    Examples:
    >>> max_value_linear_scan([1, 5, 3, 9, 2])
    9
    >>> max_value_linear_scan([])
    None
    >>> max_value_linear_scan([-1, -5, -3])
    -1

    Note:
    - This function does not modify the input array.
    - It handles empty arrays by returning None.
    - For very large arrays, consider using Python's built-in max() function,
      which is implemented in C and may be more efficient.
    """
    if not arr:  # Check if the array is empty
        return None

    max_val = arr[0]  # Start with the first element as the maximum
    for element in arr[1:]:  # Iterate through the rest of the array
        if element > max_val:
            max_val = element

    return max_val


if __name__ == "__main__":
    # Example usage of the max_value function
    print(max_value_of_integer_sequences([60, 90, 100, 80, 70, 85, 75, 50, 40, 30]))
    print(max_value_linear_scan([1, 5, 3, 9, 2]))
