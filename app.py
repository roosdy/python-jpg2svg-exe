import sys
import os
import argparse
from PIL import Image
import svgwrite
import tkinter as tk
from tkinter import filedialog


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


def browse_input_file():
    input_file = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    input_file_var.set(input_file)


def browse_output_file():
    output_file = filedialog.asksaveasfilename(
        defaultextension=".svg", filetypes=[("SVG files", "*.svg")])
    output_file_var.set(output_file)


def start_conversion():
    input_file = input_file_var.get()
    output_file = output_file_var.get()

    if not os.path.isfile(input_file):
        error_var.set(f"Input file '{input_file}' does not exist")
        return

    if not is_valid_image_file(input_file):
        error_var.set(f"Input file '{input_file}' is not a valid image file")
        return

    convert_image_to_svg(input_file, output_file)
    error_var.set(f"Converted '{input_file}' to '{output_file}'")


# Create the main window
root = tk.Tk()
root.title("Image to SVG Converter")

input_file_var = tk.StringVar()
output_file_var = tk.StringVar()
error_var = tk.StringVar()

# Create and place the input file entry
input_file_label = tk.Label(root, text="Input file:")
input_file_label.grid(row=0, column=0, padx=(10, 5), pady=(10, 0), sticky="W")
input_file_entry = tk.Entry(root, textvariable=input_file_var)
input_file_entry.grid(row=0, column=1, padx=(5, 5), pady=(10, 0), sticky="WE")
input_file_button = tk.Button(root, text="Browse", command=browse_input_file)
input_file_button.grid(row=0, column=2, padx=(5, 10), pady=(10, 0), sticky="E")

# Create and place the output file entry
output_file_label = tk.Label(root, text="Output file:")
output_file_label.grid(row=1, column=0, padx=(10, 5), pady=(5, 0), sticky="W")
output_file_entry = tk.Entry(root, textvariable=output_file_var)
output_file_entry.grid(row=1, column=1, padx=(5, 5), pady=(5, 0), sticky="WE")
output_file_button = tk.Button(root, text="Browse", command=browse_output_file)
output_file_button.grid(row=1, column=2, padx=(5, 10), pady=(5, 0), sticky="E")

# Create and place the convert button
convert_button = tk.Button(root, text="Convert", command=start_conversion)
convert_button.grid(row=2, column=0, columnspan=3,
                    padx=(10, 10), pady=(10, 5), sticky="WE")

# Create and place the error message label
error_label = tk.Label(root, textvariable=error_var, fg="red")
error_label.grid(row=3, column=0, columnspan=3,
                 padx=(10, 10), pady=(5, 10), sticky="W")

root.columnconfigure(1, weight=1)

root.mainloop()

# run the app via the ImageToSVGConverter.exe file

# Recompile after changes by running the following command in the terminal:
# pyinstaller - -onefile - -windowed - -icon = app.ico - -name ImageToSVGConverter app.py
