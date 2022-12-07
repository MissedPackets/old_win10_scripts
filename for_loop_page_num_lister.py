from  PIL import  Image
import pytesseract
import glob

#lets me pick which page i want to read
#pg_num=15

import os
#print(glob.glob(r"C:\Users\jellycat\.spyder-py3\*"))#this prints entire directory's files



     
#print(text)
#this works btw, it's not returning an error; look into screenshot.png
#print(glob.glob(r'C:\Users\jellycat\.spyder-py3\image_frames\*'))[4]


#for name in glob.glob(r'C:\Users\jellycat\.spyder-py3\image_frames\*'):
#    print ('\t', name)

list = os.listdir(('C:\\Users\\jellycat\\.spyder-py3\\image_frames'))
#print(list[pg_num])#this makes the process longer; however, it does allow me to get the pathfile's name

for pg_num in range(255):
    tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img_path=(glob.glob(r'C:\Users\jellycat\.spyder-py3\image_frames\*'))[pg_num]
    text=pytesseract.image_to_string(Image.open(img_path), config=tessdata_dir_config)
    print(text)
    print(pg_num)
    print(list[pg_num])
    f = open("LATESTout_tesseract.txt", "a")
    f.write(f'\n{text}\n{pg_num}\n{list[pg_num]}')
f.close()