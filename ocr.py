# import cv2
#you have to install tesseract by its installer exe and direct its script driver to the .exe dire
import sys
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(Image.open('name.png'), lang='eng')
print(text)