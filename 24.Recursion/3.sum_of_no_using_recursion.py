def sum_of_natural_numbers(n):
    """
    Function to calculate the sum of the first n natural numbers using recursion.
    
    Parameters:
    n (int): The non-negative integer for which the sum is to be calculated.
    
    Returns:
    int: The sum of the first n natural numbers.
    """
    # Your code here
    if n == 1:
        return 1
    # print(n) 
    # n = n + 1
    return n + sum_of_natural_numbers(n - 1)
    
result = sum_of_natural_numbers(5)
print(result)
# print(sum_of_natural_numbers(5))