from PIL import Image

def offset(image, oX, oY):
    width, height = image.size
    offset_image = Image.new("RGB", image.size)
    x = 0
    while(x<width and x+oX<width):
        y=0
        while(y<height and y+oY<height):
            pixel = image.getpixel((x, y))
            offset_image.putpixel((x+oX, y+oY), pixel)
            y+=1
        x+=1
    return offset_image