from PIL import Image

def pixelsSum(image, matrix, sayi, x, y):
    pixelSum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            pixelSum += image.getpixel((x + j, y + i))[sayi] * matrix[i+1][j+1]
    return pixelSum

def Conv3x3(image):
    matrix = ((1,2,1),
              (0,0,0),
              (-1,-2,-1))
    width, height = image.size
    new_image = image.copy()
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            r = pixelsSum(image, matrix, 0, x, y)
            g = pixelsSum(image, matrix, 1, x, y)
            b = pixelsSum(image, matrix, 2, x, y)

            new_image.putpixel((x, y), (int(r), int(g), int(b)))

    return new_image