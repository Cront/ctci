def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while(left <= right):
        mid = (right + left) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == '__main__':
    array = [8,3,5,11,1,99,33,40]
    binary_search(array, 11)