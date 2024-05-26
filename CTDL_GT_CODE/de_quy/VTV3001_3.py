def max_digit(n: int) -> int:
    if n < 10:
        return n
    else:
        last_digit = n % 10
        max_of_rest = max_digit(n // 10)
        return max(last_digit, max_of_rest)

def count_max_digit(number: int, max_digit: int=10) -> int:
    count = 0
    for i in str(number):
        if i == str(max_digit):
            count += 1
    return count

def main():
    test_case = int(input())
    
    number_list = []
    for i in range(test_case):
        number = int(input())
        number_list.append(number)
    for number in number_list:
        print(f"{number}: {count_max_digit(number=number, max_digit=max_digit(number))}")
            
if __name__ == "__main__":
    main()