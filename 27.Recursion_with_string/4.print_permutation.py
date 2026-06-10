
def print_permutation(s1 , takenfor):
    
    if (len(s1) == 0):
        print(takenfor)
        return 
    
    c = s1[0]
    small = s1[1:]

    for i in range(0 , len(takenfor) + 1):
        print_permutation(small , takenfor[0:i] + c + takenfor[i:])

    return

print_permutation('abc' , '')