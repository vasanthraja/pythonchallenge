import os

def isChar(c):
    if (c >= 'a' and c <= 'z') or (c >='A' and c <= 'Z') :
        return True
    return False

def ocr():
    file_name = 'ocr.txt'
    if not os.path.exists(file_name):
        print('file does not exists')
        return
    else:
        with open(file_name) as f:
            file_content = f.read()
            readable_content = ''
            for c in file_content:
                if (isChar(c)):
                    readable_content = readable_content + c;
    print(readable_content)

if __name__ == '__main__':
    ocr()

# answer: equality
