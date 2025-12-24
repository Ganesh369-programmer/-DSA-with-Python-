
def binary_search(arr , t):
    size = len(arr)
    start = 0
    end = size -1  

    while(start <= end):

        mid = (start + end) // 2

        if (t == arr[mid]):
            return mid
        elif (arr[mid] > t):
            end = mid - 1
        elif (arr[mid] < t):
            start = mid + 1

    return -1


sorted_list = [10,23 ,35,45,50,70,85]
target = 35

result = binary_search(sorted_list , target)
print(result)