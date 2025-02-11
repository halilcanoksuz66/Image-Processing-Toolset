from PIL import Image

def pixelsSum(img, matrix, sayi, x, y):
    pixelSum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            pixelSum += img.getpixel((x + j, y + i))[sayi] * matrix[i+1][j+1]
    return pixelSum

def minMax(value):
    return max(0, min(value, 255))

def Conv3x3(img):
    matrix = ((0,-2,0),
              (-2,11,-2),
              (0,-2,0))
    factor = 3
    offset = 0
    width, height = img.size
    image = Image.new("RGB", img.size)
    for y in range(1, height-1):
        for x in range(1, width-1):
            r = img.getpixel((x, y))[0]
            g = img.getpixel((x, y))[1]
            b = img.getpixel((x, y))[2]

            r = (pixelsSum(img, matrix, 0, x, y) / factor) + offset
            g = (pixelsSum(img, matrix, 1, x, y) / factor) + offset
            b = (pixelsSum(img, matrix, 2, x, y) / factor) + offset
            
            r = minMax(r)
            g = minMax(g)
            b = minMax(b)
            
            image.putpixel((x, y), (int(r), int(g), int(b)))

    return image