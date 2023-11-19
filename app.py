import os
from PIL import Image

def convert_to_1bit_black_and_white(image_path, output_path, threshold=100):
    
    try:
        image = Image.open(image_path)

        grayscale_image = image.convert("L")

        black_and_white = grayscale_image.point(lambda x: 255 if x > threshold else 0, '1')

        black_and_white.save(output_path)
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def process_directory(input_directory, output_directory):
    
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.tif', '.bmp', '.gif')):
                file_path = os.path.join(root, file)

                relative_path = os.path.relpath(root, input_directory)
                output_root = os.path.join(output_directory, relative_path)
                if not os.path.exists(output_root):
                    os.makedirs(output_root)

                output_path = os.path.join(output_root, file)

                convert_to_1bit_black_and_white(file_path, output_path)
                print(f"Processed and saved: {output_path}")

scans_directory = './Images'
processed_directory = './Processed'

process_directory(scans_directory, processed_directory)