def count_to_n(n):

    # Your code here
    if (n <= 1):
        return [1]
        
        
    return count_to_n(n - 1) + [n]
    
count_to_n(10)
count_to_n(5)