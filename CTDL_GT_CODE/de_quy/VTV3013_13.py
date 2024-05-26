def S(n):
  if n == 1:
    return 0.5
  else:
    return S(n - 1) + n / (n + 1)

t = int(input())
result_list = []
for _ in range(t):
  n = int(input())
  result_list.append(S(n))
  
for result in result_list:
    print("{:.10f}".format(result))