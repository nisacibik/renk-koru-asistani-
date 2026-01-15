from PIL import Image

img=Image.open("images/redGrenn.jpg")

print(img.mode)
print(img.size)
pixel=img.getpixel((0,0))
print(pixel)
img.show()