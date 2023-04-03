# Image to SVG Converter

Image to SVG Converter is a simple GUI application that converts JPG, JPEG, and PNG images to SVG format.

## Features

- Easy-to-use graphical user interface
- Support for JPG, JPEG, and PNG image formats
- White pixels are treated as transparent in the output SVG

## Usage

1. Download the `ImageToSVGConverter.exe` file.
2. Run the `ImageToSVGConverter.exe` file to start the application.
3. Click the "Browse" button next to "Input file" to select an image (JPG, JPEG, or PNG) to be converted.
4. Click the "Browse" button next to "Output file" to select the output SVG file's location.
5. Click the "Convert" button to start the conversion process.
6. The output SVG file will be saved in the specified location.

## Recompiling the Application

If you make changes to the source code and want to recompile the application, run the following command in the terminal:

```bash
pyinstaller --onefile --windowed --icon=app.ico --name ImageToSVGConverter app.py
```

This command will generate a new ImageToSVGConverter.exe file in the dist folder.

## Dependencies

The application uses the following Python libraries:

- Pillow (PIL fork) for image processing
- svgwrite for creating SVG files
- Tkinter for the graphical user interface

## License

This project is open-source and available under the MIT License.
