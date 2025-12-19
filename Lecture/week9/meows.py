import argparse

parse = argparse.ArgumentParser(description="向喵一样叫")
parse.add_argument("-n", default=1, help="喵的次数", type=int)
args = parse.parse_args()

for _ in range(args.n):
    print("meow")