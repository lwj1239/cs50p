def main():
    print_square(3)

def print_square(size):
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
        
main()