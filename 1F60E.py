smbytes =bytearray.fromhex("f09f988e")
smunicode = "\U0001F60E"

utf8code = "😎"
smbytes = utf8code.encode("utf-8")

print('U+{:X}'.format(ord(utf8code)))
print(smbytes)

utf8code = smbytes.decode('utf-8')
unicode =utf8code.encode('unicode_escape')
unistr = unicode. decode("ascii")
print("utf8", utf8code, "unicode", unicode, "ascii", unistr, "utf8", smunicode)

eind = unistr[-3:]
x = int(eind, 16)
print(str(x))

key = input("Wait")