import urllib.request
import re
import pickle

def peak():
    banner_url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    banner_content = urllib.request.urlopen(banner_url).read()

    deserialized_content = (pickle.loads(banner_content))

    res = []
    for row in deserialized_content:
        line = ''
        for col in row:
            line = line + (col[1] * col[0])
        res.append(line)
    print("\n".join(res))


if __name__ == '__main__':
    peak()


# Answer:
              #####                                                                      #####
               ####                                                                       ####
               ####                                                                       ####
               ####                                                                       ####
               ####                                                                       ####
               ####                                                                       ####
               ####                                                                       ####
               ####                                                                       ####
      ###      ####   ###         ###       #####   ###    #####   ###          ###       ####
   ###   ##    #### #######     ##  ###      #### #######   #### #######     ###  ###     ####
  ###     ###  #####    ####   ###   ####    #####    ####  #####    ####   ###     ###   ####
 ###           ####     ####   ###    ###    ####     ####  ####     ####  ###      ####  ####
 ###           ####     ####          ###    ####     ####  ####     ####  ###       ###  ####
####           ####     ####     ##   ###    ####     ####  ####     #### ####       ###  ####
####           ####     ####   ##########    ####     ####  ####     #### ##############  ####
####           ####     ####  ###    ####    ####     ####  ####     #### ####            ####
####           ####     #### ####     ###    ####     ####  ####     #### ####            ####
 ###           ####     #### ####     ###    ####     ####  ####     ####  ###            ####
  ###      ##  ####     ####  ###    ####    ####     ####  ####     ####   ###      ##   ####
   ###    ##   ####     ####   ###########   ####     ####  ####     ####    ###    ##    ####
      ###     ######    #####    ##    #### ######    ###########    #####      ###      ######
