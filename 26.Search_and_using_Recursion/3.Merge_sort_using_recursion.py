# Sorting Using Recursion
# Merge Sort


def Merge(l1, s, m, e):
    i = s
    j = m + 1
    ans = []

    # Merge two sorted halves
    while i <= m and j <= e:
        if l1[i] < l1[j]:
            ans.append(l1[i])
            i += 1
        elif l1[i] > l1[j]:
            ans.append(l1[j])
            j += 1
        else:
            ans.append(l1[i])
            ans.append(l1[j])
            i += 1
            j += 1

    # Remaining elements from first half
    while i <= m:
        ans.append(l1[i])
        i += 1

    # Remaining elements from second half
    while j <= e:
        ans.append(l1[j])
        j += 1

    # Copy sorted elements back to original list
    startOfMyAns = 0
    startOfMyList = s

    while startOfMyList <= e:
        l1[startOfMyList] = ans[startOfMyAns]
        startOfMyAns += 1
        startOfMyList += 1


def MergeSortHelper(l1, s, e):
    if s >= e:
        return

    m = s + (e - s) // 2

    # Sort left half
    MergeSortHelper(l1, s, m)

    # Sort right half
    MergeSortHelper(l1, m + 1, e)

    # Merge both halves
    Merge(l1, s, m, e)


def MergeSort(l1):
    MergeSortHelper(l1, 0, len(l1) - 1)


# Test Merge function
l2 = [5, 6, 12, 1, 9, 10]
Merge(l2, 0, 2, 5)
print("After Merge:", l2)

# Test Merge Sort
l1 = [6, 5, 12, 10, 9, 1]
MergeSort(l1)
print("After Merge Sort:", l1)