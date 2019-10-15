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
  with open('evil2.gfx', "rb") as f:
      data = f.read()
      print(len(data))
      for i in range(5):
          open(f'{i}.jpg', 'wb').write(data[i::5])

if __name__ == '__main__':
    solution()


#Answer: evil