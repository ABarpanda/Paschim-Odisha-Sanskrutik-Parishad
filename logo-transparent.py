from PIL import Image
import numpy as np

opacity_level = 150 # Opaque is 255, input between 0-255

# img = Image.open('logo.png')
# img.putalpha(opacity_level)
# img.save("logo_transp.png", "PNG")

with Image.open("logo.png") as im:
    im2 = im.copy()
    im2.putalpha(opacity_level)
    im.paste(im2, im)
    im.save("logo_transp.png", "PNG")