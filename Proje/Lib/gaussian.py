from PIL import Image

def pixelsSum(image, matrix, sayi, x, y):
    pixelSum = 0
    for i in range(-2, 3):
        for j in range(-2, 3):
            pixelSum += image.getpixel((x + j, y + i))[sayi] * matrix[i+1][j+1]
    return pixelSum

def Conv3x3(image):
    matrix = ((1,4,6,4,1),
              (4,16,24,16,4),
              (6,24,36,24,6),
              (4,16,24,16,4),
              (1,4,6,4,1))
    factor = 256
    width, height = image.size
    new_image = Image.new("RGB", (width, height))
    pixels = new_image.load()

    for y in range(2, height - 3):
        for x in range(2, width - 3):
            r = image.getpixel((x, y))[0]
            g = image.getpixel((x, y))[1]
            b = image.getpixel((x, y))[2]

            r = (pixelsSum(image, matrix, 0, x, y) / factor) 

            g = (pixelsSum(image, matrix, 1, x, y) / factor) 

            b = (pixelsSum(image, matrix, 2, x, y) / factor) 

            pixels[x, y] = (int(r), int(g), int(b))

    return new_image