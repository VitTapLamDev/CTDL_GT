import math

def cal(number: int):
    if number <= 1:
        return 1
    else:
        return float(math.sqrt(number + cal(number-1)))

def limit_float(num: float, num_digits: int = 10) -> str:
    return format(num, f'.10f')

def main():
    test_case = int(input())
    
    number_list = []
    for i in range(test_case):
        number = int(input())
        number_list.append(number)
   
    for number in number_list:
        print(limit_float(cal(number)))
            
if __name__ == "__main__":
    main()