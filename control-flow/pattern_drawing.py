
def draw_pattern(size):
    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print() 
        row += 1

def main():
    while True:
        size = input("Enter the size of the pattern: ")
        if size.isdigit() and int(size) > 0:
            size = int(size)
            draw_pattern(size)
            break
        else:
            print("Please enter a positive integer.")

if __name__ == "__main__":
    main()
