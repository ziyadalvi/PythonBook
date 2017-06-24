#Lists
#Lists are positionally ordered collections of arbitrarily typed objects with no fixed size
#They are mutable

#Sequence Operations

L = [123, 'spam', 1.23]
print(len(L))

#Because they are sequences, lists support all the sequence operations we discussed for
#strings; the only difference is that the results are usually lists instead of strings.

print(L[0])
print(L[1:-1])
L + [4,5,6]
print(L)

print(L*2)








#Wtong example of immutability since the object's value is being replaced not mutated
L = L + [4,5,6]
print(L)

#same example can be implemented in string however the strings are immutable objects 
S = '123abc'
S = S + '123'
print(S)
