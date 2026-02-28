
def find_indices(arr, element):

    # Your code here

    def helper(index):

        if len(arr) == index:
            return []

        if arr[index] == element:
            return [index] + helper(index + 1) 
        else:
            return helper(index + 1)    
    
    return helper(0)

arr = [1, 2, 3, 2, 4, 2]
element = 2

print(find_indices(arr , element))