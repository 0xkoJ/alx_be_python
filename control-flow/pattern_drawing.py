
def draw_pattern(size):
    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print() 
        row += 1

def main():
    while True:
        try:
            size = int(input("Enter the size of the pattern: "))  
            if size > 0:
                draw_pattern(size)
                break  
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
