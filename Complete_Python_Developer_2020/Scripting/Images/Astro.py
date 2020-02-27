
from PIL import Image


data_folder = ".\\Scripting\\Images\\Data\\"

img = Image.open(data_folder + "astro.jpg")

print(img.size)

resized_img = img.resize((300, 300))
resized_img.save(data_folder + "Small_astro.jpg")

img.thumbnail((400, 400))
img.save(data_folder + "Thumbnail_astro.jpg")