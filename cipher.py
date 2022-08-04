list(map(chr, range(97, 123)))
uin = input("Hello! Do you want to encode or decode? Enter e or d: ")
decodeflag = 0
if (uin == 'd'):
    decodeflag = 1
if (uin == 'e'):
    decodeflag = 0

if (decodeflag == 1):
    msg = input("Please enter your message: " )
    key = int (input("Please enter your key: "))
    newmsg = "";
    for element in msg:
        if (element == ' '):
            newmsg += ' '
        else :
            temp = ord(element) - key
            newmsg += chr(temp)
    print(newmsg)
else :
    msg = input("Please enter your message: " )
    key = int (input("Please enter your key: "))
    newmsg = "";
    for element in msg:
        if (element == ' '):
            newmsg += ' '
        else :
            temp = ord(element) + key
            newmsg += chr(temp)
    print(newmsg)
