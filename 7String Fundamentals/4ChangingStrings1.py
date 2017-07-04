#Changing srings (Remember: Strings are immutable)

S = 'spam'
#S[0] = 'x' Gives out an error

#you generally need to build and assign a new string using tools such as concatenation and slicing,
#and then, if desired, assign the result back to the string’s original name

S = S.replace('s','x')
print(S)

#every operation that yields a new string value, string methods generate new string
#objects. If you want to retain those objects, you can assign them to variable names.


#Despite the substitution metaphor, though, the result of formatting is a new string
#object, not a modified one
S = 'That is {0} {1} bird!'.format(1, 'dead')
print(S)
