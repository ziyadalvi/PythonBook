#Built-in Numeric Tools

#Expression operators
     #+, -, *, /, >>, **, &, etc.
#Built-in mathematical functions
     #pow, abs, round, int, hex, bin, etc.
#Utility modules
     #random, math, etc

x = 2 ** 4
print(x)

x = pow(2,4)
print(x)

import math
print(math.ceil(2.4))

#Although numbers are primarily processed with expressions, built-ins, and modules,
#they also have a handful of type-specific methods today, which we’ll meet in this chapter
#as well. Floating-point numbers, for example, have an as_integer_ratio method that
#is useful for the fraction number type, and an is_integer method to test if the number
#is an integer. 

