unicode1 = "\U0001F60E"

utf8code = "😎"
smbytes = utf8code.encode("utf-8")  # smbytes = bytearray.fromhex("f09f988e")

unicode2 = ('U+{:X}'.format(ord(utf8code)))
print("string utf8", unicode1, "ord utf8", unicode2)

utf8code = smbytes.decode('utf-8')
unicode =utf8code.encode('unicode_escape')
unistr = unicode. decode("ascii")
print("string utf8", utf8code, "binair unicode", unicode, "string unicode", unistr, "binair utf8", smbytes)

eind = unistr[-3:]
x = int(eind, 16)
print("table index", eind, str(x))

key = input("Wait")