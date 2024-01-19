import time

def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i <= j:
        while i <= j and arr[i] < pivot:
            i += 1
        while j >= left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[right] = arr[right], arr[i]
    return i

start_time = time.time()
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

print("Original array:", arr)

quicksort(arr, 0, len(arr) - 1)

end_time = time.time()
execution_time = end_time - start_time

print("Elements After sorting:", arr)
print(f"Sorted elements in: {execution_time:.2f} seconds")