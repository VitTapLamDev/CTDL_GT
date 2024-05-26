from math import factorial

def S(x, n):
  if n == 0:
    return 0
  else:
    return x ** n / factorial(int(n)) + S(x, n - 1)

t = int(input())
result_list = []
for i in range(t):
  x, n = map(float, input().split())
  result_list.append(S(x,n))
for i in range(t):
    print("%.8f" % result_list[i])