def custom_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

short_list = [5, 2, 9, 1, 5]
long_list = [64, 34, 25, 12, 22, 11, 90]

sorted_short_list = custom_sort(short_list.copy())
sorted_long_list = custom_sort(long_list.copy())

print(f"Sorted Short List: {sorted_short_list}")
print(f"Sorted Long List: {sorted_long_list}")

def comparisons_count(n):
    return n * (n - 1) // 2

print(f"Comparisons for list of 5 items: {comparisons_count(5)}")
print(f"Comparisons for list of 10 items: {comparisons_count(10)}")