from PIL import Image

def sliderEffects(image, brightness, contrast_value, red, green, blue):
    
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    contrast = (100.0 + contrast_value) / 100.0
    contrast *= contrast
    
    width, height = image.size
    new_image = Image.new("RGB", image.size)

    for y in range(height):
        for x in range(width):
            r = image.getpixel((x, y))[0]
            g = image.getpixel((x, y))[1]
            b = image.getpixel((x, y))[2]
            
            r = max(0, min(r + brightness, 255))
            g = max(0, min(g + brightness, 255))
            b = max(0, min(b + brightness, 255))
            
            r = int(((r / 255.0 - 0.5) * contrast + 0.5) * 255.0)
            g = int(((g / 255.0 - 0.5) * contrast + 0.5) * 255.0)
            b = int(((b / 255.0 - 0.5) * contrast + 0.5) * 255.0)
            
            r = min(255, max(0, r + red))
            g = min(255, max(0, g + green))
            b = min(255, max(0, b + blue))
            
            new_image.putpixel((x, y), (r, g, b))
    return new_image