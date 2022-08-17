
from PIL import Image, ImageFilter
image1 = Image.open('jamesharden.jpg')
image2 = image1.convert("L")
image2.save("jamesharden_BLACK.jpg")