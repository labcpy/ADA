import time
import random

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1



n = int(input("Enter the number of elements in the array (n>5000): "))
arr = []
if n<5000:
    print("Invalid")
else:
    for i in range(n):
        element = random.randint(0,n)
        arr.append(element)



print("Original array:", arr)
start_time = time.time()
merge_sort(arr)
end_time = time.time()
execution_time = end_time - start_time

print("Elements After sorting:", arr)
print(f"Sorted elements in: {execution_time:.2f} seconds")