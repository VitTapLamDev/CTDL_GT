def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def main():
    test_case = int(input())
    
    number_list = []
    for i in range(test_case):
        number = input().split(" ")
        number_list.append((number[0], number[1]))
   
    for number in number_list:
        print(f"{gcd(int(number[0]), int(number[1]))}")
            
if __name__ == "__main__":
    main()