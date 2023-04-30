import os
import glob
from PIL import Image

def resize_images(input_folder, output_folder_suffix="_resized", size=(500, 500)):
    """
    Resizes all images in the input_folder to the specified size and saves them in a new folder with a suffix.
    
    :param input_folder: str, the path to the folder containing the images to be resized
    :param output_folder_suffix: str, the suffix to add to the input folder name to create the output folder
    :param size: tuple, the target size for the resized images (width, height)
    """
    # Create the output folder if it doesn't exist
    output_folder = os.path.join(os.path.dirname(input_folder), os.path.basename(input_folder) + output_folder_suffix)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all image files in the input folder
    input_folder = os.path.join(input_folder, "*")
    image_files = glob.glob(input_folder)

    # Iterate through the image files
    for image_file in image_files:
        # Open the image using Pillow
        with Image.open(image_file) as img:
            # Resize the image
            resized_img = img.resize(size)

            # Create the output file path
            file_name = os.path.basename(image_file)
            output_file = os.path.join(output_folder, file_name)

            # Save the resized image
            resized_img.save(output_file)

if __name__ == "__main__":
    input_folder = "images-different-sizes"
    target_size = (500, 500)

    resize_images(input_folder, size=target_size)
