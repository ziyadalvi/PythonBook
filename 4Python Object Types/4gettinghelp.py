#Getting Help
#PyDoc
S = 'ziyad'
T = 24
print(dir(S))
print(dir(T))



#dir gives the method names associated with the object passed to it
#double underscores in list are operator overloading classes.
#they represent the implementation of the string object and are available to support customization.
print(S + 'alvi')
print(S.__add__('alvi')) #we shouldnt use this form of concatination as it is slower

#The dir function simply gives the methods names. To ask what they do, #you can pass them to the help function:

print(help(S.replace))

#You can also ask for help on an entire string (e.g., help(S))

#For more details, you can also consult Python’s standard library #reference manual or
#commercially published reference books, but dir and help are the first #level of documentation in Python.
