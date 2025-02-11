from PIL import Image

def grayscale(image):
    width, height = image.size
    for y in range(height):
        for x in range(width):
            red = image.getpixel((x, y))[0]
            green = image.getpixel((x, y))[1]
            blue = image.getpixel((x, y))[2]
            gray_value = int(0.299 * red + 0.587 * green + 0.114 * blue)
            image.putpixel((x, y), (gray_value, gray_value, gray_value))
    return image