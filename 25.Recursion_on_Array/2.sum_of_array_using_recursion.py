def sumarray(l1):
    if(len(l1) == 0):
        return 0
    
    sumarr = sumarray(l1[1:])
    
    ans = sumarr + l1[0]
    print(ans)
    return ans

arr = [1,2,3,4,5]
# print(sumarray(arr))
sumarray(arr)


def sumarray_tail(l1 , accumulator= 0):
    if(len(l1) == 0):
        return accumulator
    
    accumulator += l1[0] 

    return sumarray_tail(l1[1:] , accumulator)

print(f"Tail Recursion : {sumarray_tail(arr )}")