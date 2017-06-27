f = open('data.txt','w') #make a new file in output mode ('w' is for write)
f.write('Hello\n')
f.write('World\n')
f.close()

f = open('data.txt', 'r')
text = f.read()
print(text)

#best way to read a file today is to not read it at all—files provide an iterator that automatically
#reads line by line in for loops and other contexts
for line in open('data.txt'): print(line)

