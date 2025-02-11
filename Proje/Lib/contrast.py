from PIL import Image

def clamp(value):
    return max(0, min(value, 255))

def adjust_contrast(image, contrast_value):
    if contrast_value < -100 or contrast_value > 100:
        return None

    contrast = (100.0 + contrast_value) / 100.0
    contrast *= contrast

    width, height = image.size

    for i in range(width):
        for j in range(height):
            r = image.getpixel((i, j))[0]
            g = image.getpixel((i, j))[1]
            b = image.getpixel((i, j))[2]
            r = int(((r / 255.0 - 0.5) * contrast + 0.5) * 255.0)
            g = int(((g / 255.0 - 0.5) * contrast + 0.5) * 255.0)
            b = int(((b / 255.0 - 0.5) * contrast + 0.5) * 255.0)

            image.putpixel((i, j), (clamp(r), clamp(g), clamp(b)))

    return image
