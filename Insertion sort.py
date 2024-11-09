k = int(input("Enter the total number of elements to be sorted: "))
arr = []
for i in range(1, k + 1):
    elements = int(input(f"Enter the number {i} to be sorted: "))
    arr.append(elements)
print("elements before sorting:", arr)

# main code from here
n = len(arr)
for a in range(1, n):
    b = a
    while b > 0 and arr[b] < arr[b - 1]:
        arr[b - 1], arr[b] = arr[b],arr[b - 1]
        b -= 1

# to here
        print(f"after every iteration: ", arr)

print("elements after sorting:", arr)
