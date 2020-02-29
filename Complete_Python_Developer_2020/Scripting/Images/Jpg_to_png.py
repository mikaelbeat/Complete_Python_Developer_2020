
from PIL import Image
import sys, os

#value1 = int(sys.argv[1])
#value2 = int(sys.argv[2])
#grey_img.save(".\Scripting\Images\Pokedex\Grey.png", "png")

source = sys.argv[1]
destination = sys.argv[2]

print(f"Source is {source} and destination {destination}")

try:
    if os.path.isdir(destination):
        print(f"\nDestination folder {destination} already exists!\n")
    else:
        os.mkdir(destination)
        print(f"\nDestination directory {destination} created!\n")
except OSError:
    print(f"\nError creating directory {destination}!\n")


for file in os.listdir(source):
    print(file)
    img = Image.open(source + "\\" +file)
    print(img)




""" print(os.system("dir"))

img = Image.open(".\Scripting\Images\Pokedex\pikachu.jpg")

grey_img.save(".\Scripting\Images\Pokedex\Grey.png", "png")

print(os.system("dir")) """

""" data_folder = ".\\Scripting\\Images\\Pokedex\\"

img = Image.open(data_folder + "astro.jpg")

print(img.size)

resized_img = img.resize((300, 300))
resized_img.save(data_folder + "Small_astro.jpg")

img.thumbnail((400, 400))
img.save(data_folder + "Thumbnail_astro.jpg") """