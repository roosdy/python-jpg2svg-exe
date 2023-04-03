import sys
import os
import argparse
from PIL import Image
import svgwrite


def is_valid_image_file(input_file):
    return input_file.lower().endswith(('.jpg', '.jpeg', '.png'))


def convert_image_to_svg(input_file, output_file):
    with Image.open(input_file).convert('RGBA') as image:
        width, height = image.size
        dwg = svgwrite.Drawing(output_file, size=(width, height))

        for y in range(height):
            for x in range(width):
                r, g, b, a = image.getpixel((x, y))
                if a > 0 and (r, g, b) != (255, 255, 255):
                    color = f'rgb({r},{g},{b})'
                    dwg.add(dwg.rect(insert=(x, y), size=(1, 1),
                            fill=svgwrite.rgb(r, g, b, '%')))

        dwg.save()


def main():
    parser = argparse.ArgumentParser(
        description="Convert an image to an SVG file.")
    parser.add_argument("input_file", help="Input image file.")
    parser.add_argument("output_file", help="Output SVG file.")
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    if not os.path.isfile(input_file):
        print(f"Input file '{input_file}' does not exist")
        sys.exit(1)

    if not is_valid_image_file(input_file):
        print(f"Input file '{input_file}' is not a valid image file")
        sys.exit(1)

    convert_image_to_svg(input_file, output_file)
    print(f"Converted '{input_file}' to '{output_file}'")


if __name__ == '__main__':
    main()
