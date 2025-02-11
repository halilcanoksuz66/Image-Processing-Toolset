from PIL import Image

def color(image, red, green, blue):
    if red < -255 or red > 255 or green < -255 or green > 255 or blue < -255 or blue > 255:
        return False
    
    width, height = image.size

    for y in range(height):
        for x in range(width):
            r = image.getpixel((x, y))[0]
            g = image.getpixel((x, y))[1]
            b = image.getpixel((x, y))[2]
            
            r = min(255, max(0, r + red))
            g = min(255, max(0, g + green))
            b = min(255, max(0, b + blue))
            image.putpixel((x, y), (r, g, b))
    return image
