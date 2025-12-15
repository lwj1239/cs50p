from PIL import Image, ImageOps
import sys

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line argument")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line argument")

    input_file_name = sys.argv[1].lower()
    output_file_name = sys.argv[2].lower()

    if not is_valid_file_name(sys.argv[1]) or not is_valid_file_name(sys.argv[2]):
        sys.exit("Invalid input")

    if not is_extension_file_name_same(sys.argv[1], sys.argv[2]):
        sys.exit("Input and output have different extionsions")

    shirt_image_file_name = "shirt.png"

    try:
        with Image.open(input_file_name) as image, Image.open(shirt_image_file_name) as shirt_image:
            size = min(image.size, shirt_image.size)
            image = ImageOps.fit(image, size)
            shirt_image = ImageOps.fit(shirt_image, size)
            shirt_image = shirt_image.convert("RGBA")
            image.paste(shirt_image, (0, 0), shirt_image)
            image.save(output_file_name)
    except FileNotFoundError:
        sys.exit("File not exist")

def is_extension_file_name_same(file_name1, file_name2):
    extension1 = file_name1.rsplit(".", maxsplit=1)[-1]
    extension2 = file_name2.rsplit(".", maxsplit=1)[-1]

    return extension1 == extension2


def is_valid_file_name(file_name):
    return file_name.endswith((".jpeg", ".png", ".jpg"))

if __name__ == "__main__":
    main()
