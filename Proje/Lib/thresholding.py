from PIL import Image

def setThresholding(image,esikDeger):
    width, height = image.size
    for y in range(height):
        for x in range(width):
            color = image.getpixel((x, y))[0]
            if(color > esikDeger):
                color = 255
            else:
                color = 0
            image.putpixel((x, y), (color, color, color))
    return image