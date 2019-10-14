import urllib.request
import re
import pickle
import os
import zipfile
from PIL import Image
def channel():
  image = Image.open(urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png'))
  #print(f'width : {image.width}, height : {image.height}')
  strip_content = [image.getpixel((x, image.height / 2)) for x in range(image.width)]
  strip_content = strip_content[::7]

  strip_content = [r for r, g, b, h in strip_content if r == g == b]

  # Below commented conversion makes 'smart guy, you made it...' move on to the next level
  # strip_content = "".join(map(chr, strip_content))
  # next level

  next_level = re.findall("[0-9]+", "".join(map(chr, strip_content)))
  # print(next_level)
  print("".join(map(chr, map(int, next_level))))

if __name__ == '__main__':
    channel()

# Answer: integrity
