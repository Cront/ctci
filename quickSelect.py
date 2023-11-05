def partition(arr, left, right):
    pivot = arr[right]
    i = left

    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    return i

def quick_select(arr, left, right, k):
    pivot_index = partition(arr, left, right)

    if pivot_index == (k - 1):
        return arr[pivot_index]
    elif pivot_index > (k - 1):
        return quick_select(arr, left, pivot_index - 1, k)
    else:
        return quick_select(arr, pivot_index + 1, right, k)