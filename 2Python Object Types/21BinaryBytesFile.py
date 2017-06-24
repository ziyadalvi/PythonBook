#Binary byte file
import struct
packed = struct.pack('>i4sh',7,b'spam',8) #create packed binary data
print(packed) #10bytes, not objects or text

file = open('data.bin', 'wb') #Open binary output file ('wb' is for write binary)
file.write(packed) #Write packed binary data
file.close()

#reading bin file and unpacking
data = open('data.bin', 'rb').read()
print(data)
slice = data[4:8] #slice bytes
print(slice)
unpacked = struct.unpack('>i4sh',data) #a sequence of 8bit bytes
print(unpacked) #unpack into objects
