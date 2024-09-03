utf8code = "😎"
smbytes = utf8code.encode("utf-8")
unipoint = ('U+{:X}'.format(ord(utf8code)))

utf8code = smbytes.decode('utf-8')
unicode =utf8code.encode('unicode_escape')

print("string utf8", utf8code, "string unicode",  unipoint,  "binair unicode", unicode, "binair utf8",  smbytes)

key = input("Wait")