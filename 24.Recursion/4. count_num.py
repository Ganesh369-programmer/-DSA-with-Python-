def count_num(n):

    if (n>=1 and n <= 9):
        return 1
    elif(n == 0):
        return 1
    
    smallnum = int(n/10)
    # print("smallnum",smallnum)

    smallans = count_num(smallnum)
    # print("smallans", smallans)
    ans = 1 + smallans
    return ans

print(count_num(5))
print(count_num(123))
print(count_num(857489))