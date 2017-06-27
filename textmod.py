# def mod(img):
#     f = open('tmp.txt', 'w')
#     f.write(img)
#     f.close()
    # https://stackoverflow.com/questions/22351254/python-script-to-convert-image-into-byte-array

import re, random, array
from PIL import Image
import numpy as np

with open("IMAG2378_dered.jpg", "rb") as imageFile:
    f = imageFile.read()
    b = bytearray(f)
    m = re.split('a', b)
    random.shuffle(m)
    # p = np.asarray(m)
    # p = array.fromlist('B', map(ord, m)).tostring()
    p = ''
    for x in m:
        p += x
    img = Image.frombytes('RGB', (590, 640), str(p))
    img.save('tmp.jpg')


    f2 = open('tmp.jpg', 'w')
    f2.write(m)
    f2.close()