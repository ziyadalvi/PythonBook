#Indexing and Slicing

#In Python, characters in a string are fetched by indexing—
#providing the numeric offset of the desired component in square brackets after the
#string.

S = 'spam'
print(S[0], S[-2])

z = 'ziziyadziziyad'
print(z[0:7])

print(z[2:13:2]) #S[i:j:k] accepts k as a step

S = 'hello'
print(S[::−1]) #reverse
