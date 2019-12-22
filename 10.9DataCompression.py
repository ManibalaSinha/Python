import zlib # for archiving(file) and compression
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(t)
print(len(t))
print(zlib.decompress(t))
