#Set comprehensions

print({x ** 2 for x in [1,2,3,4]})

#the loop is coded on the right, and the collection expression is coded on the left (x ** 2).
#“Give me a new set containing X squared, for every X in a list.”
S = {c * 4 for c in 'spam'}

print(S|{'xxxx','aaaa'})
