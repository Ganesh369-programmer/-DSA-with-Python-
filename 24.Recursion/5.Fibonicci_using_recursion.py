def fibonicci(n):
    if (n == 0):
        return 1
    if ( n == 1):
        return 1
    
    last = fibonicci(n - 1)
    secondlast = fibonicci(n - 2)

    ans = last + secondlast

    return ans


print(fibonicci(4))
print(fibonicci(10))