# def mod(img):
#     f = open('tmp.txt', 'w')
#     f.write(img)
#     f.close()
    # https://stackoverflow.com/questions/22351254/python-script-to-convert-image-into-byte-array

import re, random, array, io
from PIL import Image
from PIL import ImageDraw
import numpy as np
import binascii, io

with open("IMAG2378_dered.jpg", "rb") as imageFile:
    f = imageFile.read()
    b = bytearray(f)
    m = re.split('\b', b)
    random.shuffle(m[-5:])
    p = ''
    for x in m:
        p += x
    stream = io.BytesIO(p)
    img = Image.open(stream)
    draw = ImageDraw.Draw(img)
    img.save("a_test.jpg")
    img.close()
