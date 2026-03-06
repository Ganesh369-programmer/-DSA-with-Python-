def linear_search(arr, target):
    """
    Function to perform linear search on an array using recursion.
    
    Parameters:
    arr (list of int): The array of integers.
    target (int): The element to search for.
    
    Returns:
    bool: True if target is found, False otherwise.
    """
    # Your code here
    def helper(index):
        if len(arr) == index:
            return False
            
        if arr[index] == target:
            return True
        else:
            return helper(index + 1)
    
    return helper(0)


arr = [10, 20, 30, 40]
target = 20
print(linear_search(arr , target))