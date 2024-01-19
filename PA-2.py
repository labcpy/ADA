def min_max(arr):
    if len(arr) == 1:
        return arr[0], arr[0]

    mid = len(arr) // 2
    left_min, left_max = min_max(arr[:mid])
    right_min, right_max = min_max(arr[mid:])

    return min(left_min, right_min), max(left_max, right_max)


n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

if len(arr) == 0:
    print("Array is empty, no minimum and maximum.")
else:
    min_val, max_val = min_max(arr)
    print("Minimum value: ", min_val)
    print("Maximum value: ", max_val)