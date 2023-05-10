import sys
from PIL import Image
import os

source_folder = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for filename in os.listdir(source_folder):
    img = Image.open(f'{source_folder}/{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{new_folder}/{clean_name}.{sys.argv[3]}', sys.argv[3])
    print(f'{filename} converted to {sys.argv[3]} format!')