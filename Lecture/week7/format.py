import re

def main():
    name = input("What's your name? ").strip()

    if matches := re.search(r"^(.+), *(.+)$", name):
        name = " ".join(reversed(matches.groups()))

    print(f"Hello, {name}")

if __name__ == "__main__":
    main()