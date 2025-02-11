import math
from PIL import Image

def rotate_image(image, degree):
    rads = math.radians(degree)
    rot_img = Image.new("RGB", image.size)
    width, height = image.size

    midx,midy = (width//2, height//2)

    for i in range(0,width):
        for j in range(0,height):
            x= (i-midx)*math.cos(rads)+(j-midy)*math.sin(rads)
            y= -(i-midx)*math.sin(rads)+(j-midy)*math.cos(rads)

            x=round(x)+midx 
            y=round(y)+midy 

            if (x>=0 and y>=0 and x<width and  y<height):
                r = image.getpixel((x, y))[0]
                g = image.getpixel((x, y))[1]
                b = image.getpixel((x, y))[2]
                rot_img.putpixel((i, j), (r,g,b))

    return rot_img