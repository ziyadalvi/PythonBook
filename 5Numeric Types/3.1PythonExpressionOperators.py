#Python Expression Operators

#Parentheses group subexpressions
#We can forget about operator precedence completely if we group parts of
#expressions with parantheis

X = 1
Y = 2
Z = 3

ZZ = X + Y * Z
print(ZZ)

ZZ = (X + Y) * Z
print(ZZ)

ZZ = X + (Y * Z)
print(ZZ)


                            
#Mixe types are converted up

ZZ = 40 + 3.14
print(ZZ)
