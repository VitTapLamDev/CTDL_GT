def binary_number(number: int) -> int:
    if number > 1:
        binary_number(number // 2)
    print(number % 2, end='')

def main():
    test_case = int(input())
    
    number_list = []
    for i in range(test_case):
        number = int(input())
        number_list.append(number)
   
    for number in number_list:
        binary_number(number)
        print()
            
if __name__ == "__main__":
    main()