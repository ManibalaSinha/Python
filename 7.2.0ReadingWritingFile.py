#open() returns file object and used with two arguments: open(filename, mode) 
#'a' opens the file for appending, 'r+' opens the file for both reading and writing.
# with keyword when dealing with file objects. adv is that file is properly closed after finishes 
f = open('workfile', 'w')
with open('workfile') as f:
     read_data = f.read()
# We can check that the file has been automatically closed.
print(f.closed)
# if you are not using with keyword, you should call f.close() to close the file.
#f.close()