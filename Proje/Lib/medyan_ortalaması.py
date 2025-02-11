from PIL import Image
import random

def Medyan(image, sayi, x, y):
    liste = list()
    for i in range(-1, 2):
        for j in range(-1, 2):
            liste.append(image.getpixel((x + j, y + i))[sayi])
    liste.sort()
    return liste[4]

def setMedian(image):
    width, height = image.size
    new_image = Image.new("RGB", (width, height))
    pixels = new_image.load()

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            color = Medyan(image, 0, x, y)

            pixels[x, y] = (int(color), int(color), int(color))

    return new_image

def SaltAndPepper(image, howMuch):
    width, height = image.size
    new_image = image.copy()

    amount = int(width * height / 100 * howMuch)
    for i in range(0, amount):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        
        color = random.randint(0, 1)
        if color == 1:
            color = 255
        new_image.putpixel((x, y), (color, color, color))
    return new_image