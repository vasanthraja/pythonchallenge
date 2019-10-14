import urllib.request
import re
import pickle
import os
import zipfile
from PIL import Image, ImageDraw
import bz2

def nextseq(seq):
    res = ""
    count = 1
    for i in range(len(seq)):
        if (i < len(seq) - 1):
            if seq[i] == seq[i + 1] :
                count = count + 1
            else:
                res = res + str(count) + seq[i]
                count = 1

    res = res + str(count) + seq[i]

    return res

def bull():
    seq = '1'
    a = []
    for i in range(31):
        a.append(seq)
        seq = nextseq(seq)

    print(len(a[30]))

if __name__ == '__main__':
    bull()


#Answer: 5808