# Image Format Converter
This script converts images from one format to another. It takes a source folder, a new folder, and the desired image format as command line arguments.	 
## Requirements
- Python 3.x
- Pillow library (`pip install Pillow`)
## Usage
1. Save the script to a file (e.g. `convert.py`).
2. Open a command prompt or terminal and navigate to the directory where you saved the script.
3. Run the script using the following command: `python convert.py <source_folder> <new_folder> <image_format>`
- `<source_folder>`: The path to the folder containing the images you want to convert.
- `<new_folder>`: The path to the folder where you want to save the converted images. If this folder doesn’t exist, it will be created automatically.
- `<image_format>`: The desired image format (e.g. `png`, `jpg`, etc.)

Example:
`python convert.py C:\Users\John\Pictures C:\Users\John\Converted png`
This command will convert all images in the `C:\Users\John\Pictures` folder to PNG format and save them in the `C:\Users\John\Converted` folder.
