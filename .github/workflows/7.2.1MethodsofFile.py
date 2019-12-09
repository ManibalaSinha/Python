#to read a file, call f.read(size), which reads some quantity of data and returns it as string
#if the end of file has been reached, f.read() will return empty string('').
#f.write(string) writes the contents of string to the file, return the number of characters
#f.tell() returns integer giving the current position in the file as number of bytes from beginning
#f.seek(offset, whence) to change the file object's position.position is computed from adding
#offset to a reference point, reference point is selected by whence argument.
f = open('workfile', 'rb+')
print(f.write(b'0123456789abcdef'))
#print(f.tell())
print(f.read())
#print(f.seek(5)) #go to 6th byte in the file
print(f.read(1))

