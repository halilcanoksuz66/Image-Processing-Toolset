from PIL import Image
import matplotlib.pyplot as plt
import io
from PyQt5.QtCore import QBuffer

def histogram(image):
    width, height = image.size
    arr = [0] * 256

    for y in range(height):
        for x in range(width):
            color = image.getpixel((x, y))[0]
            arr[color] += 1


    plt.figure(figsize=(10, 6))
    plt.bar(range(256), arr, color='b', alpha=0.7)
    plt.xlabel('Renk Değerleri')
    plt.ylabel('Piksel Sayısı')
    
    buffer = QBuffer()
    buffer.open(QBuffer.ReadWrite)
    plt.savefig(buffer, format='png')
    img = Image.open(io.BytesIO(buffer.data()))
    buffer.close()
    
    return img