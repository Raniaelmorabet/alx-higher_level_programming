#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    
    Args:
    list_of_integers (list): The list of unsorted integers.
    
    Returns:
    int or None: The peak element if found, otherwise None.
    """
    if not list_of_integers:
        return None
    
    def binary_search_peak(arr, low, high):
        if low == high:
            return arr[low]
        
        mid = (low + high) // 2
        if arr[mid] > arr[mid + 1]:
            return binary_search_peak(arr, low, mid)
        else:
            return binary_search_peak(arr, mid + 1, high)
    
    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)
