#dynamic typing, implies polymorphism
#In Python, types are determined automatically at runtime, not
#in response to declarations in your code. This means that you never declare variables
#ahead of time

a = 3 # Assign a name to an object

#at least conceptually, Python will perform three distinct steps to carry out the request.
#These steps reflect the operation of all assignments in the Python language:
#1. Create an object to represent the value 3.
#2. Create the variable a, if it does not yet exist.
#3. Link the variable a to the new object 3.

#These links from variables to objects are called references in Python

#In concrete terms:
#• Variables are entries in a system table, with spaces for links to objects.
#• Objects are pieces of allocated memory, with enough space to represent the values
#for which they stand.
#• References are automatically followed pointers from variables to objects.

#Python internally caches and reuses certain kinds of unchangeable
#objects, such as small integers and strings as an optimization

#IMP:
"""Technically speaking, objects have more structure than just enough space to represent
their values. Each object also has two standard header fields: a type designator used to
mark the type of the object, and a reference counter used to determine when it’s OK to
reclaim the object."""

