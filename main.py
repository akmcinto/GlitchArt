from PIL import Image
import sys, os, re
from colourify import *
from decolourify import *

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
        elif arg == "blueify":
            img, s = blueify(img)
        elif arg == "redify":
            img, s = redify(img)
        elif arg == "greenify":
            img, s = greenify(img)
        elif arg == "yellowify":
            img, s = yellowify(img)
        elif arg == "magentify":
            img, s = magentify(img)
        elif arg == "cyanify":
            img, s = cyanify(img)

        elif arg == "degreyify":
            img, s = degreyify(img)
        elif arg == "deblueify":
            img, s = deblueify(img)
        elif arg == "deredify":
            img, s = deredify(img)
        elif arg == "degreenify":
            img, s = degreenify(img)
        elif arg == "deyellowify":
            img, s = deyellowify(img)
        elif arg == "demagentify":
            img, s = demagentify(img)
        elif arg == "decyanify":
            img, s = decyanify(img)
        suffix += "_" + s

    img.save(currdir + fname + suffix + ext)

if __name__ == "__main__":
    # http://www.diveintopython.net/scripts_and_streams/command_line_arguments.html, 2016-05-26
    main(sys.argv[1:])
