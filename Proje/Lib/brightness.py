from PIL import Image
def setBrightness(image, brightness):
    
    if image.mode != 'RGB':
        image = image.convert('RGB')

    width, height = image.size

    for y in range(height):
        for x in range(width):
            r = image.getpixel((x, y))[0]
            g = image.getpixel((x, y))[1]
            b = image.getpixel((x, y))[2]
            r = max(0, min(r + brightness, 255))
            g = max(0, min(g + brightness, 255))
            b = max(0, min(b + brightness, 255))
            image.putpixel((x, y), (r, g, b))
    return image