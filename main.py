from PIL import Image
import sys, os, re
from colourify import *

def main(argv):
    fpath, ext = os.path.splitext(argv[0])
    fname = re.search('([\\/]\w+$)', fpath).group(0)
    img = Image.open(argv[0])
    currdir = os.path.dirname(os.path.realpath(__file__))

    suffix = ""
    for arg in argv[1:]:
        s = ""
        if arg == "greyify":
            img, s = greyify(img)
        if arg == "blueify":
            img, s = blueify(img)
        if arg == "redify":
            img, s = redify(img)
        if arg == "greenify":
            img, s = greenify(img)
        if arg == "yellowify":
            img, s = yellowify(img)
        if arg == "magentify":
            img, s = magentify(img)
        if arg == "cyanify":
            img, s = cyanify(img)
        suffix += "_" + s

    img.save(currdir + fname + suffix + ext)

if __name__ == "__main__":
    # http://www.diveintopython.net/scripts_and_streams/command_line_arguments.html, 2016-05-26
    main(sys.argv[1:])
