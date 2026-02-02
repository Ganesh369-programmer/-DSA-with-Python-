def power2(n):
    if(n == 1):
        return 2
    
    smallanswer = power2(n - 1)
    ans = 2 * smallanswer
    print(ans)
    return ans

print(power2(5))