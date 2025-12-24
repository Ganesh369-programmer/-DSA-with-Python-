def bubble_sort(arr):
    n = len(arr)

    for passs in range(0 , n):
        for i in range(0 , n-1-passs):
            if (arr[i] > arr[i+1]):
                arr[i],arr[i+1] = arr[i+1],arr[i]


    return arr
            

ar1 = [12 , 11  , 23 , 90 , 78 ]
arr2 = [9, 8 , 7, 6 , 5, 4 , 3 , 2 ,1]
result = bubble_sort(arr2)
print(result)
