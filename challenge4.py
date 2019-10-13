import urllib.request
import re

def linkedlist():
    initial_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    url_ending = '12345'
    while True:
        url = initial_url + url_ending
        print(url)
        request_conent = urllib.request.urlopen(url).read().decode('utf-8')
        match_expr = 'and the next nothing is ([0-9]+)'
        matched_content = re.findall(match_expr, request_conent)
        if (len(matched_content) == 0):
            if (request_conent == 'Yes. Divide by two and keep going.'):
                url_ending = str(int(url_ending) / 2)
                continue

            else:
                print(request_conent)
            break;
        else:
            url_ending = matched_content[0]


if __name__ == '__main__':
    linkedlist()

# peak.html
