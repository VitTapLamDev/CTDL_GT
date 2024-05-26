def sum_even(arr, n):
  if n == 0:
    return 0
  else:
    if arr[0] % 2 == 0:
      return arr[0] + sum_even(arr[1:], n - 1)
    else:
      return sum_even(arr[1:], n - 1)

n = int(input())
arr = [int(x) for x in input().split()]
even_sum = sum_even(arr, n)
print(even_sum)

def sum_even_iterative(arr):
  even_sum = 0
  for num in arr:
    if num % 2 == 0:
      even_sum += num
  return even_sum

n = int(input())
arr = [int(x) for x in input().split()]
even_sum = sum_even_iterative(arr)
print(even_sum)