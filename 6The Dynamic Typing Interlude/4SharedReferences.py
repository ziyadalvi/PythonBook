a = 3
b = a

print(a,b)
#Names and objects after next running the assignment b = a. Variable b becomes a reference
#to the object 3. Internally, the variable is really a pointer to the object’s memory space created by
#running the literal expression 3.

#a pointing to 3
#b pointing to 3

#This scenario in Python—with multiple names referencing the same object—is usually
#called a shared reference (and sometimes just a shared object). Note that the names a
#and b are not linked to each other directly when this happens; in fact, there is no way
#to ever link a variable to another variable in Python

a = 3
b = a #change the value of b; b still references the original object, the integer 3.
a = 'spam'

print(a,b)
