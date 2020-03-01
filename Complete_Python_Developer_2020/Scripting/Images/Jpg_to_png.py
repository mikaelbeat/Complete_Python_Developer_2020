
from PIL import Image
import sys, os


source = sys.argv[1]
destination = sys.argv[2]


try:
    if os.path.isdir(destination):
        print(f"\nDestination folder {destination} already exists!")
    else:
        os.mkdir(destination)
        print(f"\nDestination directory {destination} created!")
except OSError:
    print(f"\nError creating directory {destination}!")


try:
    for file in os.listdir(source):
        img = Image.open(source + "\\" + file)
        without_extension = os.path.splitext(file)[0]
        with_png_extension = without_extension + ".png"
        img.save(destination + "\\" + with_png_extension)
        print(f"\nConverted {file} to {with_png_extension}")
except FileNotFoundError:
    print(f"\nSource folder {source} not found!")
