def bubble_sort_ascending(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1
        
        pos = low + ((high - low) * (x - arr[low]) // (arr[high] - arr[low]))

        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1

d = int(input().strip())
arr = list(map(int, input().strip().split()))

n = int(input().strip())
search_elements = [int(input().strip()) for _ in range(n)]

bubble_sort_ascending(arr)
print(' '.join(map(str, arr)))
for x in search_elements:
    result = interpolation_search(arr, x)
    print(result)
