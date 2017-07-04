#when we reassign a variable, what happens to the value it was
#previously referencing? For example, after the following statements, what happens to
#the object 3?

"""The answer is that in Python, whenever a name is assigned to a new object, the space
held by the prior object is reclaimed if it is not referenced by any other name or object.
This automatic reclamation of objects’ space is known as garbage collection"""

x = 42
x = 'shrubbery' # Reclaim 42 now (unless referenced elsewhere)
x = 3.1415 # Reclaim 'shrubbery' now
x = [1, 2, 3] # Reclaim 3.1415 now


#notice that x is set to a different type of object each time. Again, though this is
#not really the case, the effect looks like that the type of x is changing over time.

#Each time x is
#assigned to a new object, Python reclaims the prior object’s space. For instance, when
#it is assigned the string 'shrubbery', the object 42 is immediately reclaimed (assuming
#it is not referenced anywhere else)

#Internally, Python accomplishes this feat by keeping a counter in every object that keeps
#track of the number of references currently pointing to that object. As soon as (and
#exactly when) this counter drops to zero, the object’s memory space is automatically
#reclaimed
