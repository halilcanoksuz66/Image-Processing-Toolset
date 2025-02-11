from PIL import Image

                        # HİSTOGRAM EŞİKLEME
def contrastStretching(image):
    new_image = Image.new('RGB', image.size)
    
    width, height = image.size
    
    minR = 255
    maxR = 0
    minG = 255
    maxG = 0
    minB = 255
    maxB = 0
    
    for x in range(width):
        for y in range(height):
            r = image.getpixel((x, y))[0]
            g = image.getpixel((x, y))[1]
            b = image.getpixel((x, y))[2]
            
            minR = min(minR,r)
            maxR = max(maxR,r)
            minG = min(minG,g)
            maxG = max(maxG,g)
            minB = min(minB,b)
            maxB = max(maxB,b)
            
    for x in range(width):
        for y in range(height):
            r = image.getpixel((x, y))[0]
            g = image.getpixel((x, y))[1]
            b = image.getpixel((x, y))[2]
            
            r = 255 * ((r - minR) / (maxR - minR))
            g = 255 * ((g - minG) / (maxG - minG))
            b = 255 * ((b - minB) / (maxB - minB))
            
            new_image.putpixel((x, y), (int(r), int(g), int(b)))
            
    return new_image