# Implement Greedy search algorithm for Selection Sort

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume current index has minimum
        min_index = i

        # Find the actual minimum in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum with current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Show step (useful for viva)
        print(f"Step {i+1}: {arr}")

    return arr


# ---------------- Main ----------------
arr = [64, 25, 12, 22, 11]

print("Original Array:", arr)
sorted_arr = selection_sort(arr)

print("Sorted Array:", sorted_arr)