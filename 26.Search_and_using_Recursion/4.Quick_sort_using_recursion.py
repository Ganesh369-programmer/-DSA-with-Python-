def quick_sort(arr):
    """
    Function to perform quick sort on a list of integers using recursion.
    
    Parameters:
    arr (list of int): The list to be sorted.
    
    Returns:
    list of int: The sorted list.
    """
    
    # Base case: if the list has 1 or no elements, it's already sorted
    if len(arr) <= 1:
        return arr
 
    # Choosing the pivot (here we choose the last element as the pivot)
    pivot = arr[-1]
    less_than_pivot = []  # Elements less than the pivot
    greater_than_pivot = []  # Elements greater than the pivot
 
    # Partitioning the array into two lists
    for i in range(len(arr) - 1):  # Exclude the pivot itself
        if arr[i] < pivot:
            less_than_pivot.append(arr[i])
        else:
            greater_than_pivot.append(arr[i])
 
    # Recursively applying quick sort to the two partitions
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)