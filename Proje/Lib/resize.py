from PIL import Image

def Resize(image, value):
    width, height = image.size
    newH = int(height/value)
    newW = int(width/value)
    new_image = Image.new("RGB", (newW, newH))
    pixels = new_image.load()

    for y in range(newW):
        for x in range(newH):
            p = image.getpixel((x*value,y*value))
            pixels[x, y] = p
    return new_image