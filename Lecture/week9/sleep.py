from typing import Iterator

def main():
    n = int(input("Number: "))
    print(sleep(n))

def sleep(n: int) -> Iterator[str]:
    for _ in range(n):
        yield "yang" * n

if __name__ == "__main__":
    main()