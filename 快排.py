def quick_sort(a, low, high):
    if low >= high:
        return a
    i, j = low, high
    pivot = a[low]
    while i < j:
        while i < j and a[j] > pivot:
            j -= 1
        a[i] = a[j]
        while i < j and a[i] < pivot:
            i += 1
        a[j] = a[i]
    a[j] = pivot

    quick_sort(a, low, j -1)
    quick_sort(a, j + 1, high)

    return a

lists = [5,4,3,2,1]
print(quick_sort(lists, 0, len(lists) - 1))