def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            right = mid - 1
        else:
            left = mid + 1
    return -1

d = int(input())
arr = list(map(int, input().split()))
n = int(input())
search_elements = [int(input()) for _ in range(n)]

bubble_sort_descending(arr)

print(' '.join(map(str, arr)))

for x in search_elements:
    result = binary_search(arr, x)
    print(result)
