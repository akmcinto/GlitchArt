from PIL import Image
import sys, os

def main(argv):
    fname, ext = os.path.splitext(argv[0])
    img = Image.open(argv[0])
    currdir = os.path.dirname(os.path.realpath(__file__))
    img.save(currdir + "\\testimg" + ext)

if __name__ == "__main__":
    # http://www.diveintopython.net/scripts_and_streams/command_line_arguments.html, 2016-05-26
    main(sys.argv[1:])
