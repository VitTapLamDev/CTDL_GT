from math import sqrt

def cal(n: int):
    if n == 1:
        return 2
    else:
        inner_result = 1  
        for i in range(2, n + 1):
            inner_result = sqrt(inner_result + 1)
        return sqrt(1 + inner_result)

t = int(input())
result_list = []
for i in range(t):
    n = int(input())
    result_list.append(cal(n))
for i in range(t):
    print("%.10f" % result_list[i])