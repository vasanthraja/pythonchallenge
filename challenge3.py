import urllib.request
import re

def equality():
    request = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
    page_content = request.read().decode('utf-8')

    expected_regular_expression = '[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
    matched_strings = re.findall(expected_regular_expression, page_content)
    print("".join(matched_strings))


if __name__ == '__main__':
    equality()

# linkedlist
