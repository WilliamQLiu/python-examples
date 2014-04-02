from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os,sys

def get_soup(url):
   return BeautifulSoup(requests.get(url).text)

image_type = sys.argv[1]
query = image_type
url = "http://www.bing.com/images/search?q=" + query + "&qft=+filterui:color2-bw+filterui:imagesize-large&FORM=R5IR3"
soup = get_soup(url)
bimg = re.compile("mm.bing.net")
img_links = soup.find_all("img", {"src2": bimg})
images = [a['src2'] for a in img_links]


for img in images:
    raw_img = urllib2.urlopen(img).read()
    cntr = len([i for i in os.listdir("images") if image_type in i]) + 1
    f = open("images/" + image_type + "_"+ str(cntr), 'wb')
    f.write(raw_img)
    f.close()
