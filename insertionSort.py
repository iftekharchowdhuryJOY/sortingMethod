def insertionSort(arr):
    n = len (arr) # get the length of the array
    if n <= 1:
        return # If the array has 0 or 1 element, it is already sorted, so return

    for j in range(1, n): # Iterate over the array starting from the second element

        key = arr[j]  # Store the current element as the key to be inserted in the right position

        i = j - 1

        while i >= 0 and arr[i] > key: # Move elements greater than key one position ahead
            arr[i + 1] = arr[i] # Shift elements to the right
            i -= 1
        arr[i + 1] = key # Insert the key in the correct position

# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [5, 2, 4, 6, 1, 3]
insertionSort(arr)
print(arr)
