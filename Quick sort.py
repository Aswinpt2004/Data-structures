k = int(input("Enter the total number of elements to be sorted: "))
arr = []
for i in range(1, k + 1):
    elements = int(input(f"Enter the number {i} to be sorted: "))
    arr.append(elements)

print("Elements before sorting:", arr)


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        # print(f"After partitioning with pivot {arr[pi]}: {arr}")

        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


quicksort(arr, 0, len(arr) - 1)

print("Elements after sorting:", arr)
