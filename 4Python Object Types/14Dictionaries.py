#Dictionaries
#Python dictionaries are not sequences but are mappings
#Mappings are also collections of other objects, but they store objects by
#key instead of by relative position.
#They are also mutable.

#When written as literals, dictionaries are coded in curly braces and consists of
#series of "key:value".

D = {'food':'Spam',
     'quantity':4,
     'color':'pink'}

#accessing values
print(D['food'])

#we can make dictionaries by passing to the dict type name either 'keyword arguments'
#or the result of 'zipping' together sequences of keys and values at runtime (e.g from files)

bob1 = dict(name='Bob', job='dev', age=40)
print(bob1)

#zipping
bob2 = dict(zip(['name','job','age'],['Bob','dev',40]))
print(bob2) #Mappings are not
#positionally ordered, so unless you’re lucky, they’ll come back in a different order than
#you typed them

