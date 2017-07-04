#Types Live with Objects, Not Variables

a = 3 # It's an integer
a = 'spam' # Now it's a string
a = 1.23 # Now it's a floating point

"""Names have no types so we are not changing the type here, but we simply have made variable
refer to another object.

Objects, on the other hand, know what type they are—each object contains a header
field that tags the object with its type"""

#The integer object 3, for example, will contain
#the value 3, plus a designator that tells Python that the object is an integer (strictly
#speaking, a pointer to an object called int, the name of the integer type).

