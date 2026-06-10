def firstindexofanelement(l1 , x):
    if(len(l1) == 0):
        return -1
   
    if(l1[0] == x):
        
        return 0
    
    ans = firstindexofanelement(l1[1:] , x)

    if(ans == -1):
        return ans
    else:
        return ans +1
    

print(firstindexofanelement([3 , 2 , 5 , 2 , 8 , 2 ,1] , 2))