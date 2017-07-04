#Mixed types are converted up

mixtype = 40 + 3.14 #We can mix different numeric types. For instance, adding an integer
#to a floating-point number

print(mixtype)

#in mixed-type numeric expressions, Python first converts operands up to the type of the
#most complicated operand, and then performs the math on same-type operands

#This behavious is similar to type conversions in C
#Python ranks the complexity of numeric types like so: integers are simpler than floatingpoint
#numbers, which are simpler than complex numbers

#IMPORTANT
#all these mixed-type conversions apply only when mixing
#numeric types (e.g., an integer and a floating point) in an expression, including those
#using numeric and comparison operators. In general, Python does not convert across
#any other type boundaries automatically. Adding a string to an integer, for example,
#results in an error, unless you manually convert one or the other

