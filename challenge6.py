import urllib.request
import re
import pickle
import os
import zipfile

def channel():
  f = zipfile.ZipFile('channel.zip')
  comments = []
  file_name = '90052'

  regex = re.compile('Next nothing is ([0-9]+)')

  while True:
    file = file_name + '.txt';
    file_content = f.read(file).decode('utf-8')
    comments.append(f.getinfo(file).comment.decode('utf-8'))
    file_name = re.findall(regex, file_content)

    if (len(file_name) == 0):
      print("".join(comments))
      break
    else:
      file_name = file_name[0]

if __name__ == '__main__':
    channel()

# Answer: Hockey
