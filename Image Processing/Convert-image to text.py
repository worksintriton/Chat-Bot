from pytesseract import pytesseract
from PIL import Image
import  cv2
import glob
import os
import io
import re
import numpy
from wand.image import Image
pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
config=('-1 eng --oem 1 --psm 6 preserve_inrterword_spaces 0')
#[cv2.imread(file) for file in glob.glob('path/to/files/*png')]
#img=[cv2.imread(file) for file in glob.glob('C:/Users/Triton/Desktop/image/Gowthampdfimage-*.jpg')]
path = glob.glob('C:/Users/Triton/Desktop/image/img/Gowthampdfimag.jpg')
cv_img = []
for img in path:
    n = cv2.imread(img)
    cv_img.append(n)
    Result=pytesseract.image_to_string(img,config=config)   
    res=Result.encode('utf-8')
    ult=res.decode('utf-8')
#Result.save(filename='C:/Users/Triton/Desktop/image/Gowthampdftext'+'.txt')
print('ok')
work_dir = 'C:/Users/Triton/Desktop/image/img'
for path in glob.glob(os.path.join(work_dir, "Gowthampdfimagetext-.txt",'w')):
    path.save(filename='C:/Users/Triton/Desktop/image/img/gowthampdftext.txt')
    
    with io.open(path, mode="w", encoding="utf-8") as fd:
        content = fd.write()   
print('converted')    
