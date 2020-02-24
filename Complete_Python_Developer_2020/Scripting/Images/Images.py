
from PIL import Image, ImageFilter


img = Image.open(".\Scripting\Images\Pokedex\pikachu.jpg")


filtered_img = img.filter(ImageFilter.BLUR)

print(img)

#filtered_img.save(".\Scripting\Images\Pokedex\Blur.png", "png")
filtered_img = img.convert("L")
filtered_img.save(".\Scripting\Images\Pokedex\Grey.png", "png")
