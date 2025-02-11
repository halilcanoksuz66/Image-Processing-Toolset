from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import io, sys
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QBuffer

from Lib import grayscale, negative, gaussian, agf, sobel, thresholding, increaseContrast, smooth, dilation, erosion, prewitt, laplacian, medyan_ortalaması, sliderEffects, rotate, mirror, histogram, average, zoom, offset, resize, perspektif

class Ui(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('app.ui', self)
        
        self.load_button.clicked.connect(self.load_image)
        self.save_button.clicked.connect(self.save_image)
        self.clean_button.clicked.connect(self.clean_image)
        self.grayscale_button.clicked.connect(self.grayscale)
        self.negative_button.clicked.connect(self.negative)
        self.gaussian_button.clicked.connect(self.gaussian)
        self.lpf_button.clicked.connect(self.lowPassFilter)
        self.sobel_button.clicked.connect(self.sobel)
        self.thresholding_button.clicked.connect(self.threshold)
        self.hs_threshold.valueChanged.connect(self.thresholdValueChanged)
        self.salt_pepper.clicked.connect(self.salt)
        self.hs_sap.valueChanged.connect(self.saltValueChanged)
        self.contrast_button.clicked.connect(self.increaseContrast)
        self.dilation_button.clicked.connect(self.dilation)
        self.erosion_button.clicked.connect(self.erosion)
        self.prewitt_button.clicked.connect(self.prewitt)
        self.laplacian_button.clicked.connect(self.laplacian)
        self.median_button.clicked.connect(self.meanAverage)
        self.smooth_button.clicked.connect(self.smooth)
        self.mirrorX_button.clicked.connect(self.mirrorX)
        self.mirrorY_button.clicked.connect(self.mirrorY)
        self.histogram_button.clicked.connect(self.histogram)
        self.average_button.clicked.connect(self.average)
        self.zoom_button.clicked.connect(self.zoom)
        self.resize_button.clicked.connect(self.resized)
        self.offset_button.clicked.connect(self.offset)
        self.pers_button.clicked.connect(self.perspective)
        
        self.hs_brightness.valueChanged.connect(self.brightnessValueChanged)
        self.hs_brightness.sliderReleased.connect(self.sliderEffects)
        
        self.hs_contrast.valueChanged.connect(self.contrastValueChanged)
        self.hs_contrast.sliderReleased.connect(self.sliderEffects)
        
        self.hs_red.valueChanged.connect(self.redValueChanged)
        self.hs_red.sliderReleased.connect(self.sliderEffects)
        
        self.hs_green.valueChanged.connect(self.greenValueChanged)
        self.hs_green.sliderReleased.connect(self.sliderEffects)
        
        self.hs_blue.valueChanged.connect(self.blueValueChanged)
        self.hs_blue.sliderReleased.connect(self.sliderEffects)
        
        self.hs_rotate.valueChanged.connect(self.rotateValueChanged)
        self.rotate_button.clicked.connect(self.rotate)
        
        
        self.show()
        
    def load_image(self):
        filename = filedialog.askopenfilename()
        if filename:
            img = QtGui.QPixmap(filename)
            self.display.setPixmap(img)
            self.display2.setPixmap(img)
            img2 = Image.open(filename)
            img2.save("temp/temp.png")
            img2.save("temp/tempOrg.png")
            img2.save("temp/photo.png")
  
    def save_image(self):
        if self.display2.pixmap() != None:
            filename = filedialog.asksaveasfilename(defaultextension='.png')
            if filename:
                img = Image.open("temp/temp.png")
                img.save(filename)
    
    def clean_image(self):
        if self.display2.pixmap() != None:
            img = Image.open("temp/photo.png")
            img.save("temp/temp.png")
            img.save("temp/tempOrg.png")
            pix = QtGui.QPixmap("temp/photo.png")
            self.display.setPixmap(pix)
            self.display2.setPixmap(pix)
            self.hs_brightness.setValue(0)
            self.hs_contrast.setValue(0)
            self.hs_red.setValue(0)
            self.hs_green.setValue(0)
            self.hs_blue.setValue(0)
    
    
    def pillowToQPixmap(self,img,saveOnOrg): 
        img.save("temp/temp.png")
        if(saveOnOrg):
            img.save("temp/tempOrg.png")
        pix = QtGui.QPixmap("temp/temp.png")
        self.display2.setPixmap(pix)
        
    def grayscale(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        img = grayscale.grayscale(img)
        self.pillowToQPixmap(img,1)
        
    def negative(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        img = negative.negative(img)
        self.pillowToQPixmap(img,1)
        
    def gaussian(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        img = gaussian.Conv3x3(img)
        self.pillowToQPixmap(img,1)
        
    def lowPassFilter(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        img = agf.Conv3x3(img)
        self.pillowToQPixmap(img,1)
        
    def sobel(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        img = sobel.Conv3x3(img)
        self.pillowToQPixmap(img,1)
        
    def threshold(self):
        img = Image.open("temp/tempOrg.png")
        data = self.hs_threshold.value()
        img = thresholding.setThresholding(img, data)
        self.pillowToQPixmap(img,0)
        
    def thresholdValueChanged(self):
        data = self.hs_threshold.value()
        self.lbl_threshold.setText(str(data))
        
    def salt(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        data = self.hs_sap.value()
        img = medyan_ortalaması.SaltAndPepper(img, data)
        self.pillowToQPixmap(img,1)
        
    def saltValueChanged(self):
        data = self.hs_sap.value()
        self.lbl_saltpepper.setText(str(data))
        
    def increaseContrast(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        img = increaseContrast.contrastStretching(img)
        self.pillowToQPixmap(img,1)
        
    def smooth(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        img = smooth.Conv3x3(img)
        self.pillowToQPixmap(img,1)
        
    def dilation(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        img = dilation.dilation(img)
        self.pillowToQPixmap(img,1)
        
    def erosion(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        img = erosion.erosion(img)
        self.pillowToQPixmap(img,1)
        
    def prewitt(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        img = prewitt.Conv3x3(img)
        self.pillowToQPixmap(img,1)
        
    def laplacian(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        img = laplacian.Conv3x3(img)
        self.pillowToQPixmap(img,1)
        
    def meanAverage(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        img = medyan_ortalaması.setMedian(img)
        self.pillowToQPixmap(img,1)
        
    def mirrorX(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        img = mirror.mirror(img, 1, -1)
        self.pillowToQPixmap(img,1)
        
    def mirrorY(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        img = mirror.mirror(img, -1, 1)
        self.pillowToQPixmap(img,1)
        
    def histogram(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        img = histogram.histogram(img)
        self.pillowToQPixmap(img,1)
        
    def average(self):
        self.display.setPixmap(self.display2.pixmap())
        img = Image.open("temp/temp.png")
        img = average.Conv3x3(img)
        self.pillowToQPixmap(img,1)
        
    def sliderEffects(self):
        img = Image.open("temp/tempOrg.png")
        pix = QtGui.QPixmap("temp/tempOrg.png")
        self.display.setPixmap(pix)
        dataBrightness = self.hs_brightness.value()
        dataContrast = self.hs_contrast.value()
        dataRed = self.hs_red.value()
        dataGreen = self.hs_green.value()
        dataBlue = self.hs_blue.value()
        
        img = sliderEffects.sliderEffects(img, dataBrightness, dataContrast, dataRed, dataGreen, dataBlue)
        
        self.pillowToQPixmap(img,0)
        
    def rotate(self):
        img = Image.open("temp/tempOrg.png")
        pix = QtGui.QPixmap("temp/tempOrg.png")
        self.display.setPixmap(pix)
        data = self.hs_rotate.value()
        img = rotate.rotate_image(img, data)
        self.pillowToQPixmap(img,0)
        
        
    def brightnessValueChanged(self):
        data = self.hs_brightness.value()
        self.lbl_brightness.setText(str(data))
        
    def contrastValueChanged(self):
        data = self.hs_contrast.value()
        self.lbl_contrast.setText(str(data))
        
    def redValueChanged(self):
        data = self.hs_red.value()
        self.lbl_red.setText(str(data))
        
    def greenValueChanged(self):
        data = self.hs_green.value()
        self.lbl_green.setText(str(data))
        
    def blueValueChanged(self):
        data = self.hs_blue.value()
        self.lbl_blue.setText(str(data))
        
    def rotateValueChanged(self):
        data = self.hs_rotate.value()
        self.lbl_rotate.setText(str(data))
        
    def zoom(self):
        img = Image.open("temp/tempOrg.png")
        data = int(self.sb_zoom.text())
        img = zoom.zoom(img, data)
        self.pillowToQPixmap(img,0)
        
    def resized(self):
        if(self.sb_resize.value()!=0):
            img = Image.open("temp/tempOrg.png")
            data = self.sb_resize.value()
            img = resize.Resize(img, data)
            self.pillowToQPixmap(img,0)
        
    def offset(self):
        img = Image.open("temp/tempOrg.png")
        dataX = int(self.sb_offset_x.value())
        dataY = int(self.sb_offset_y.value())
        img = offset.offset(img, dataX, dataY)
        self.pillowToQPixmap(img,0)
        
    def perspective(self):
        img = Image.open("temp/tempOrg.png")
        x1 = self.sb_x1.value()
        y1 = self.sb_y1.value()
        x2 = self.sb_x2.value()
        y2 = self.sb_y2.value()
        x3 = self.sb_x3.value()
        y3 = self.sb_y3.value()
        x4 = self.sb_x4.value()
        y4 = self.sb_y4.value()
        X1 = self.sb_X1.value()
        Y1 = self.sb_Y1.value()
        X2 = self.sb_X2.value()
        Y2 = self.sb_Y2.value()
        X3 = self.sb_X3.value()
        Y3 = self.sb_Y3.value()
        X4 = self.sb_X4.value()
        Y4 = self.sb_Y4.value()
        img = perspektif.Perspective(x1, y1, x2, y2, x3, y3, x4, y4, X1, Y1, X2, Y2, X3, Y3, X4, Y4, img)
        self.pillowToQPixmap(img,0)
                    
        
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()