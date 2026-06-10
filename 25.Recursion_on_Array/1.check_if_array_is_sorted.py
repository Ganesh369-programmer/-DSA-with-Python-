def checksorted(l1):
    if(len(l1) == 0 or len(l1) == 1):
        return True
    
    ans = checksorted(l1[1:])

    if(l1[0] < l1[1]):
        return ans
    else:
        return False
    

def checksorted2(l1):
    if(len(l1) == 0 or len(l1) == 1):
        return True
    
    if(l1[0] >= l1[1]):
        return False
    
    return checksorted2(l1[1:])
    
arr = [4 , 5 ,6 , 9 , 23]
arr1 = [7 , 2, 9 , 69]

print(checksorted(arr))
print(checksorted(arr1))