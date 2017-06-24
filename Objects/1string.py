#core types, numbers, strings, tuples are immutable while #lists,dictionaries and sets are not.
#Among other things, immutability can be used to guarantee that
#an object remains constant throughout your program

#we can expand strings into lists so it can be mutated

S = 'ziyad'
L = list(S)
print(L)
L[1] = 'X'
L = ''.join(L) #join with empty delimeter
print(L)

#The bytearray supports in-place changes for text, but only for text #whose characters are all most 8bits wide (ASCII). 
#All other strings are still immubatble - bytearray is a distict hybrid 
#of immutable bytes strings


B = bytearray(b'ziyad') #A byte/list hybrid (ahead)
print(B)
B.extend(b'alvi') #'b'needed in 3.X
print(B) #B[i] = ord(c) 
B.decode() #translate into normal string
print(B)
