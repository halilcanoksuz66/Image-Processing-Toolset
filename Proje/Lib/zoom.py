from PIL import Image

def zoom(image, zoom):
    width, height = image.size
    wz = int(zoom / 400 * width)
    hz = int(zoom / 400 * height)
    zoomed_image = Image.new("RGB", (width-2*wz,height-2*hz))
    for x in range(wz,width-wz):
        for y in range(hz,height-hz):
            pixel = image.getpixel((x, y))
            zoomed_image.putpixel((x-wz, y-hz), pixel)
    return zoomed_image