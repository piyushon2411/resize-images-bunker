# Image Resizer

This Python script resizes all images in a given folder to a specified size (default: 500x500 pixels) and saves them in a new folder with a `_resized` suffix.

## Prerequisites

- Python 3.x
- Pillow library (Python Imaging Library fork)

## Installation

1. Install Python 3.x from the [official website](https://www.python.org/downloads/).

2. Install the Pillow library by running the following command in your terminal or command prompt:

```bash
pip install pillow
```

## Usage

1. Place the `resize_images.py` script in the folder containing the images you want to resize.

2. Open a terminal or command prompt in the folder containing the script.

3. Run the following command:

```bash
python resize_images.py
```

4. The script will create a new folder with the same name as the input folder, but with a `_resized` suffix. The resized images will be saved in this new folder.

## Script Description

`resize_images.py` contains a function called `resize_images()`, which takes three arguments:

- `input_folder`: the path to the folder containing the images to be resized.
- `output_folder_suffix`: the suffix to add to the input folder name to create the output folder (default: "_resized").
- `size`: the target size for the resized images (default: (500, 500)).

The script iterates through all the image files in the input folder, resizes them using the Pillow library, and saves the resized images in the new output folder. The aspect ratio of the images is maintained during resizing.
```

Save the contents above into a file named `README.md` and include it in your project folder. This will serve as the documentation for your project.