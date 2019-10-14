import urllib
import requests
import re
import pickle
import os
import zipfile
import bz2
from PIL import Image, ImageDraw
from io import BytesIO

def solution():
    un = 'huge'
    ps = 'file'
    values = { 'username': un,'password': ps }
    image = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/return/cave.jpg', auth=(un, ps)).content))
    w, h = (image.size)

    even_image = Image.new('RGB', (w // 2, h // 2));
    odd_image = Image.new('RGB', (w // 2, h // 2));

    for i in range(w):
        for j in range(h):
            if (i + j) % 2 == 0:
                odd_image.putpixel((i // 2, j // 2), image.getpixel((i ,j)))
            else:
                even_image.putpixel((i // 2, j // 2), image.getpixel((i ,j)))

    even_image.show()
    odd_image.show()

if __name__ == '__main__':
    solution()


#Answer: evil