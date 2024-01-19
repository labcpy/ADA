def sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i  # Changed the variable name from 'min' to 'min_index'
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp


n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)
print("Original array:", arr)
sort(arr)
print("Elements After sorting:", arr)
