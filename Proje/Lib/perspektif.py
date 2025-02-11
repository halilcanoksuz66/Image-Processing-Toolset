import numpy as np
from PIL import Image

def Perspective(x1,y1,x2,y2,x3,y3,x4,y4,X1,Y1,X2,Y2,X3,Y3,X4,Y4,img):
    girisMatris = ((x1,y1,1,0,0,0,-x1*X1,-y1*X1),
                   (0,0,0,x1,y1,1,-x1*Y1,-y1*Y1),
                   (x2,y2,1,0,0,0,-x2*X2,-y2*X2),
                   (0,0,0,x2,y2,1,-x2*Y2,-y2*Y2),
                   (x3,y3,1,0,0,0,-x3*X3,-y3*X3),
                   (0,0,0,x3,y3,1,-x3*Y3,-y3*Y3),
                   (x4,y4,1,0,0,0,-x4*X4,-y4*X4),
                   (0,0,0,x4,y4,1,-x4*Y4,-y4*Y4),)
    matrisTers = np.linalg.inv(girisMatris)
    
    a00 = matrisTers[0][0] * X1 + matrisTers[0][1] * Y1 + matrisTers[0][2] * X2 + matrisTers[0][3] * Y2 
    + matrisTers[0][4] * X3 + matrisTers[0][5] * Y3 + matrisTers[0][6] * X4 + matrisTers[0][7] * Y4
    
    a01 = matrisTers[1][0] * X1 + matrisTers[1][1] * Y1 + matrisTers[1][2] * X2 + matrisTers[1][3] * Y2 
    + matrisTers[1][4] * X3 + matrisTers[1][5] * Y3 + matrisTers[1][6] * X4 + matrisTers[1][7] * Y4
    
    a02 = matrisTers[2][0] * X1 + matrisTers[2][1] * Y1 + matrisTers[2][2] * X2 + matrisTers[2][3] * Y2 
    + matrisTers[2][4] * X3 + matrisTers[2][5] * Y3 + matrisTers[2][6] * X4 + matrisTers[2][7] * Y4
    
    a10 = matrisTers[3][0] * X1 + matrisTers[3][1] * Y1 + matrisTers[3][2] * X2 + matrisTers[3][3] * Y2 
    + matrisTers[3][4] * X3 + matrisTers[3][5] * Y3 + matrisTers[3][6] * X4 + matrisTers[3][7] * Y4
    
    a11 = matrisTers[4][0] * X1 + matrisTers[4][1] * Y1 + matrisTers[4][2] * X2 + matrisTers[4][3] * Y2 
    + matrisTers[4][4] * X3 + matrisTers[4][5] * Y3 + matrisTers[4][6] * X4 + matrisTers[4][7] * Y4
    
    a12 = matrisTers[5][0] * X1 + matrisTers[5][1] * Y1 + matrisTers[5][2] * X2 + matrisTers[5][3] * Y2 
    + matrisTers[5][4] * X3 + matrisTers[5][5] * Y3 + matrisTers[5][6] * X4 + matrisTers[5][7] * Y4
    
    a20 = matrisTers[6][0] * X1 + matrisTers[6][1] * Y1 + matrisTers[6][2] * X2 + matrisTers[6][3] * Y2 
    + matrisTers[6][4] * X3 + matrisTers[6][5] * Y3 + matrisTers[6][6] * X4 + matrisTers[6][7] * Y4
    
    a21 = matrisTers[7][0] * X1 + matrisTers[7][1] * Y1 + matrisTers[7][2] * X2 + matrisTers[7][3] * Y2 
    + matrisTers[7][4] * X3 + matrisTers[7][5] * Y3 + matrisTers[7][6] * X4 + matrisTers[7][7] * Y4
    
    a22 = 1
    
    return Perspective2(a00, a01, a02, a10, a11, a12, a20, a21, a22, img)
    

def Perspective2(a00, a01, a02, a10, a11, a12, a20, a21, a22, image):
    width, height = image.size
    new_image = Image.new("RGB", (width, height))
    
    for x in range(0, width):
        for y in range(0, height):
            r = image.getpixel((x, y))[0]
            g = image.getpixel((x, y))[1]
            b = image.getpixel((x, y))[2]
            
            z = a20 * x + a21 * y + 1
            
            X = (a00 * x + a01 * y + a02) / z
            Y = (a10 * x + a11 * y + a12) / z
            if(X > 0 and X < height and Y > 0 and Y < width):
                new_image.putpixel((int(X), int(Y)), (int(r), int(g), int(b)))
    return new_image
