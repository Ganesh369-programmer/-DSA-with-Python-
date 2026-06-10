def palindrome_helper(s1 , s , e):

    if (s>=e):
        return True
    
    if (s1[s] != s1[e]):
        return False
    
    return palindrome_helper(s1 , s + 1 , e - 1)

def palindrome(s1):
    return palindrome_helper(s1 , 0 , len(s1) - 1)

print(palindrome('malayalam'))