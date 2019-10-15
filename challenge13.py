import urllib
import requests
import re
import pickle
import os
import zipfile
import bz2
from PIL import Image, ImageDraw
from io import BytesIO
import xmlrpc.client
#https://docs.python.org/3/library/xmlrpc.html

def solution():
    connection = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    #print(connection.system.listMethods())
    print(connection.system.methodHelp("phone"))

    # Bert is evil from the previous challenge
    print(connection.phone("Bert"))

if __name__ == '__main__':
    solution()


#Answer: ITALY