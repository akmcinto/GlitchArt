threshold = 150

def blueify(img):
    pixels = list(img.getdata())
    for x in range(0, img.width):
        for y in range(0, img.height):
            pix = img.getpixel((x,y))
            blue = pix[2]
            if blue < threshold:
                img.putpixel((x,y), (pix[0], pix[1], threshold))
    return img, "blue"

def greenify(img):
    pixels = list(img.getdata())
    for x in range(0, img.width):
        for y in range(0, img.height):
            pix = img.getpixel((x,y))
            green = pix[1]
            if green < threshold:
                img.putpixel((x,y), (pix[0], threshold, pix[2]))
    return img, "green"

def redify(img):
    pixels = list(img.getdata())
    for x in range(0, img.width):
        for y in range(0, img.height):
            pix = img.getpixel((x,y))
            red = pix[0]
            if red < threshold:
                img.putpixel((x,y), (threshold, pix[1], pix[2]))
    return img, "red"

def yellowify(img):
    pixels = list(img.getdata())
    for x in range(0, img.width):
        for y in range(0, img.height):
            pix = img.getpixel((x,y))
            yellow = max(pix[0], pix[1])
            if yellow > 0:
                img.putpixel((x,y), (yellow, yellow, pix[2] % yellow))
    return img, "yellow"

def magentify(img):
    pixels = list(img.getdata())
    for x in range(0, img.width):
        for y in range(0, img.height):
            pix = img.getpixel((x,y))
            magenta = max(pix[0], pix[2])
            if magenta > 0:
                img.putpixel((x,y), (magenta, pix[1] % magenta, magenta))
    return img, "magenta"

def cyanify(img):
    pixels = list(img.getdata())
    for x in range(0, img.width):
        for y in range(0, img.height):
            pix = img.getpixel((x,y))
            cyan = max(pix[1], pix[2])
            if cyan > 0:
                img.putpixel((x,y), (pix[0] % cyan, cyan, cyan))
    return img, "cyan"

def greyify(img):
    pixels = list(img.getdata())
    for x in range(0, img.width):
        for y in range(0, img.height):
            pix = img.getpixel((x,y))
            r, g, b = pix[0], pix[1], pix[2]
            if max(abs(r-b), abs(r-g), abs(g-b)) > 32:
                img.putpixel((x,y), (b, b, b))
    return img, "grey"
