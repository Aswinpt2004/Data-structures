k = int(input("Enter the total number of elements to be sorted: "))
arr = []
for i in range(1, k + 1):
    elements = int(input(f"Enter the number {i} to be sorted: "))
    arr.append(elements)

print("Elements before sorting:", arr)


# main code from here
def mergesort(arr):
    if len(arr) < 2:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    mergesort(left)
    mergesort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    print("After merge step:", arr)


mergesort(arr)

print("Elements after sorting:", arr)
