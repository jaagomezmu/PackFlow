def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x >= pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    input_list = [7, 2, 1, 6, 8, 5, 3, 4]
    sorted_list = quicksort(input_list)
    print("Original list:", input_list)
    print("Sorted list:", sorted_list)