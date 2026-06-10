def return_subsequence(s1):

    if (s1 == ''):   #don't give gap here 
        ans = ['']
        return ans

    
    smallans = return_subsequence(s1[1:])
    l = s1[0]
    ans = []

    ans.extend(smallans)

    for eachpermutation in smallans:
        ans.append(l + eachpermutation)

    return ans

l1 = 'abc'
ans = return_subsequence(l1)
print(ans)