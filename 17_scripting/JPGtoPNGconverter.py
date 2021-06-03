
import sys
import os
from PIL import Image

# Great the first and seconds arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check is new/exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}/{filename}')
    clean_name = os.path.splitext(filename)[0]

    # convert images & save to new folder
    img.save(f'{output_folder}/{clean_name}.png', 'png')
