""" OCR that converts images to text """

from pytesseract import image_to_string
from PIL import Image

print image_to_string(Image.open('/Users/williamliu/Desktop/Screen Shot 2014-09-27 at 11.45.34 PM.png'))

#print image_to_string(Image.open('/Users/williamliu/Desktop/Screen Shot 2014-09-27 at 11.45.34 PM.png'))
#print image_to_string(Image.open('test-european.jpg'), lang='fra')
