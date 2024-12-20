k = int(input("Enter the total number of elements to be sorted: "))
arr = []
for i in range(1, k + 1):
    elements = int(input(f"Enter the number {i} to be sorted: "))
    arr.append(elements)
print("elements before sorting: ", arr)

# main code from here
n = len(arr)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

    print("after every iteration", arr)

print("elements after sorting: ", arr)
