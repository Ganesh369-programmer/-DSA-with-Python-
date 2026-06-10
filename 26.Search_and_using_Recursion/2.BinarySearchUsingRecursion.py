def binarysearchhelper(l1 , x , s , e):
    if(s > e):
        return False
    
    m = s + (e - s) // 2

    if(l1[m] == x):
        return True
    
    if(x > l1[m]):
        return binarysearchhelper(l1 , x , m + 1 , e)
    
    return binarysearchhelper(l1 , x , s , m - 1)

def binarysearchusingrecursion(l1 , x):
    return binarysearchhelper(l1 , x , 0 , len(l1) - 1)

l1 = [i for i in range(1000)]
print(binarysearchusingrecursion(l1  , 999))