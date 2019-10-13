def isChar(c):
    if (c >= 'a' and c <= 'z') or (c >='A' and c <= 'Z') :
        return True
    return False

def map():
    s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    res = ''
    for c in s:
        if (isChar(c)):
            res = res + (chr( ((ord(c) - 95) % 26)  + ord('a')))
        else:
            res = res + c
    print(res)

if __name__ == '__main__':
    map()
