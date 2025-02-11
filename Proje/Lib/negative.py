from PIL import Image

def negative(image):
    width, height = image.size
    for y in range(height):
        for x in range(width):            
            red = image.getpixel((x, y))[0]
            green = image.getpixel((x, y))[1]
            blue = image.getpixel((x, y))[2]
            red = 255 - red
            green = 255 - green
            blue = 255 - blue
            image.putpixel((x, y), (red, green, blue))
    return image