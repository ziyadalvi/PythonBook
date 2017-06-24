#Tuple
#roughly like a list that cannot be changed—tuples are sequences, like lists, but they are
#immutable, like strings

T = (11,22,33,44)
print(len(T))

print(T + (5,6)) #concatination

print(T[2]) #indexing slicing and more

print(T.count(2))

T = (2,) + T[1:] #makes new tuple for new value
print(T)

#Like lists and dictionaries, tuples support mixed types and nesting, but they don’t grow
#and shrink because they are immutable

T = 'spa', 3.0, [11,22,12]
print(T[1])
T[2][1]

T.append(4) #gives an error 
