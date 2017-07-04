#Booleans
#Some may argue that the Python Boolean type, bool, is numeric in nature because its
#two values, True and False, are just customized versions of the integers 1 and 0 that
#print themselves differently.

print(type(True))
#<class 'bool'>

print(isinstance(True, int))
#True

print(True == 1) # Same value
#True

print(True is 1) # But a different object: see the next chapter
#False

print(True is not 0)

print(True or False) # Same as: 1 or 0
#True

print(True + 4) # (Hmmm)
#5
