from PIL import Image

def dilation(image):
    width, height = image.size
    new_image = Image.new("RGB", (width, height))
    pixels = new_image.load()

    for y in range(1, height - 2):
        for x in range(1, width - 2):
            r = max(image.getpixel((x+j,y+i))[0] for i in range(-1,2) for j in range(-1,2))
            pixels[x, y] = (int(r), int(r), int(r))

    return new_image