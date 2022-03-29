filename = "C:/Users/USER/Desktop/hermelin/python/files/test.txt"
#f = open(filename, 'r')
f = open(filename, 'r+')
print(f.read())
#f.close()

f = open(filename, 'w')
print(f.write('192.168.1.1\n192.168.1.2'))
f.close()
