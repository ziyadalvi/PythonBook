#Type-Specific Operations on Lists
#Lists are like arrays but more powerful (no type constrains, no fixed size). So they can grow and shrink on demand


L = [123,'spam',1.23]
print(L)
L.append('NI') #string mutation
print(L)

L.pop(2)
print(L)

