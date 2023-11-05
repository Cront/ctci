def partition(arr, l, r):
    pivot = arr[r]
    i = l

    for j in range(l, r):
        if arr[j] <= pivot: 
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i

def quick_select(arr, l, r, k):
    pivot = partition(arr, l, r)

    if (pivot == (k-1)):
        return arr[pivot]
    if (pivot > (k-1)):
        return quick_select(arr, l, pivot - 1, k)
    else:
        return quick_select(arr, pivot + 1, r, k)
        

array = [15, 10, 4, 3, 20, 7]
print(quick_select(array, 0, len(array) - 1, 5))