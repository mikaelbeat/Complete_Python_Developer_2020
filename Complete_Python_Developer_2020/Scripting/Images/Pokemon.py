
from PIL import Image, ImageFilter


img = Image.open(".\Scripting\Images\Pokedex\pikachu.jpg")

#blurred_img = img.filter(ImageFilter.BLUR)

print(img)

""" grey_img.save(".\Scripting\Images\Pokedex\Blur.png", "png")
grey_img = img.convert("L")
grey_img.save(".\Scripting\Images\Pokedex\Grey.png", "png")
grey_img.show() """

""" crooked_img = img.rotate(90)
crooked_img.show() """

resized_img = img.resize((300, 300))
resized_img.show()
