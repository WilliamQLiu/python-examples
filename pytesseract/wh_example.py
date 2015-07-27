""" OCR that converts images to text """

from pytesseract import image_to_string
from PIL import Image
from wand.image import Image as WandImage
from wand.display import display


if __name__ == '__main__':
    FILE = "/Users/williamliu/Dropbox/Lifeline/WH/ViewLetterFile.pdf" + "[0]"
    with WandImage(filename=FILE) as img:
        img.save(filename="/temp.jpg")
        print "Saved Image as temp"
    with WandImage(filename="/temp.jpg") as img:
        #img.resize(200, 150)
        #img.save(filename="/thumbnail_resize.jpg")
        raw_text = image_to_string(Image.open(img))
        print "Got raw text"
    print raw_text
