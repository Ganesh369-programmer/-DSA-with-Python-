def remove_ch(s , ch ):

    if (len(s) == 0 or s == ' '):
        return s
    
    smallans = remove_ch(s[1:] , ch)

    if s[0] == ch:
        return smallans
    
    else:
        return s[0] + smallans


s = "abczzz"
ans = remove_ch(s , 'z')
print(ans)
