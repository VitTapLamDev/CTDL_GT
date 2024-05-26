def X(n):
  if n == 0:
    return 1
  else:
    return X(n - 1) + Y(n - 1)

def Y(n):
  if n == 0:
    return 0
  else:
    return 3 * X(n - 1) + Y(n - 1)

t = int(input())
for _ in range(t):
  n = int(input())
  x_value = X(n)
  y_value = Y(n)
  print(x_value, y_value)