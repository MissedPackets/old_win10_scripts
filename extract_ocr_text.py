from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import os
import cv2
#import shutil
tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_frames='image_frames'

def files():
    try:
        os.remove(image_frames)
    except OSError:
        pass
    if not os.path.exists(image_frames):
        os.makedirs(image_frames)
        
    src_vid=cv2.VideoCapture('my_vid.mp4')
    return(src_vid)

def process(src_vid):
    index=0
    while src_vid.isOpened():
        ret, frame =src_vid.read()
        if not ret:
            break
            
        name = './image_frames/frame' +str(index)+'.png'
        
        if index % 90==0:
            print('extracting frames...'+name)
            cv2.imwrite(name, frame)
        index=index+1
        if cv2.waitKey(5) & 0xFF ==ord('q'):
            break
    src_vid.release()
    cv2.destroyAllWindows()
    
    
def get_text():
    for i in os.listdir(image_frames):
        print(str(i))
        my_example=Image.open(image_frames+"/"+i)
        text=pytesseract.image_to_string(my_example, lang='eng')
        print(text)
if __name__=='__main__':
    vid=files()
    process(vid)
    get_text()

