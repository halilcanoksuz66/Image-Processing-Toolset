from PIL import Image

def mirror(image, dX, dY):
    width, height = image.size
    mirrored_image = Image.new("RGB", image.size)
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            mirrored_image.putpixel((dX*x, dY*y), pixel)
    return mirrored_image