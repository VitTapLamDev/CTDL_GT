def de_quy(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    else:
        return (n * de_quy(n-1))

def main():
    running = True
    while running:
        try:
            n = int(input())
            if n > 0 :
                for i in range(0, n+1):
                    print(f"{i}! = {de_quy(i)}")
                running = False
            else:
                print("Gia tri dau vao ko hop le")
        except:
            print("Gia tri dau vao ko hop le")
            
if __name__ == "__main__":
    main()