threshold = 128

def deblueify(img):
    pixels = list(img.getdata())
    for x in range(0, img.width):
        for y in range(0, img.height):
            pix = img.getpixel((x,y))
            blue = pix[2]
            if blue > threshold:
                img.putpixel((x,y), (pix[0], pix[1], threshold))
    return img, "deblue"

def degreenify(img):
    pixels = list(img.getdata())
    for x in range(0, img.width):
        for y in range(0, img.height):
            pix = img.getpixel((x,y))
            green = pix[1]
            if green > threshold:
                img.putpixel((x,y), (pix[0], threshold, pix[2]))
    return img, "degreen"

def deredify(img):
    pixels = list(img.getdata())
    for x in range(0, img.width):
        for y in range(0, img.height):
            pix = img.getpixel((x,y))
            red = pix[0]
            if red > threshold:
                img.putpixel((x,y), (threshold, pix[1], pix[2]))
    return img, "dered"

def deyellowify(img):
    pixels = list(img.getdata())
    for x in range(0, img.width):
        for y in range(0, img.height):
            pix = img.getpixel((x,y))
            yellow = max(pix[0], pix[1])
            if yellow > threshold:
                img.putpixel((x,y), (threshold, threshold, pix[2]))
    return img, "deyellow"

def demagentify(img):
    pixels = list(img.getdata())
    for x in range(0, img.width):
        for y in range(0, img.height):
            pix = img.getpixel((x,y))
            magenta = max(pix[0], pix[2])
            if magenta > threshold:
                img.putpixel((x,y), (threshold, pix[1], threshold))
    return img, "demagenta"

def decyanify(img):
    pixels = list(img.getdata())
    for x in range(0, img.width):
        for y in range(0, img.height):
            pix = img.getpixel((x,y))
            cyan = max(pix[1], pix[2])
            if cyan > threshold:
                img.putpixel((x,y), (pix[0], threshold, threshold))
    return img, "decyan"

def degreyify(img):
    pixels = list(img.getdata())
    for x in range(0, img.width):
        for y in range(0, img.height):
            pix = img.getpixel((x,y))
            r, g, b = pix[0], pix[1], pix[2]
            if max(abs(r-b), abs(r-g), abs(g-b)) < 32:
                img.putpixel(r + g, g + b, b + r)
    return img, "degrey"
