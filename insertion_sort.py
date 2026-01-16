def insertion_sort(arr):
    n = len(arr)

    for current in range(1 , n):
        currentcard = arr[current]
        currentposition = current - 1

        while currentposition >= 0:
            if arr[currentposition] < currentcard:
                break

            else:
                arr[currentposition + 1] = arr[currentposition]
                currentposition -= 1
        
        arr[currentposition + 1] = currentcard
    
    return arr

    

arr1 = [12 , 11 ,23 , 43 , 56 , 2]
result = insertion_sort(arr1)
print(result)