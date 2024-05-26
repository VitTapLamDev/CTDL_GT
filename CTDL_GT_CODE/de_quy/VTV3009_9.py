def count_positives_iterative(arr):
  positive_count = 0
  for num in arr:
    if num > 0:
      positive_count += 1
  return positive_count

n = int(input())
arr = [float(x) for x in input().split()]
positive_count = count_positives_iterative(arr)
print(positive_count)