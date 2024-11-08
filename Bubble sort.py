k = int(input("Enter the total number of elements to be sorted: "))
arr = []
for i in range(1, k + 1):
    elements = int(input(f"Enter the number {i} to be sorted: "))
    arr.append(elements)
print("elements before sorting: ", arr)

# main code from here

n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# to here
            print(f"after every iteration", arr)

print("elements after sorting: ", arr)
