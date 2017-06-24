#Bounds Checking
#Lists have no fixed size, but it still doesnt allows us to reference items that are not
#present. Unlike C which doesnt check and silently grows in response
#methos like append can only grow a list

L = [123,'spam','NI']

print(L[99]) #throws error

L[99] = 1

print(L[99]) #out of range error
