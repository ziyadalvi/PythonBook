#Comparisions:Normal and Chained

print(1<2)
print(2.0 >= 1) #mixed types are allowed in numeric expressions (only)
print(2.0 == 2.0)
print(2.0 != 2.0)


#Python also allows us to chain multiple comparisons together to perform
#range tests. Chained comparisons are a sort of shorthand for larger Boolean expressions.

X = 2
Y = 4
Z = 6
print(X < Y < Z)
print(X < Y and Y < Z)

print(X < Y > Z)
print(X < Y and Y > Z)

print(1 < 2 < 3.0 < 4)
print(1 > 2 > 3.0 > 4)

print(1 == 2 < 3) #Same as: 1 == 2 and 2 < 3
# Not same as: False < 3 (which means 0 < 3, which is true!)

#numeric comparisons are based
#on magnitudes, which are generally simple—though floating-point numbers may not
#always work as you’d expect

print(1.1 + 2.2 == 3.3)
#Prints out false due to the fact that floating-point numbers cannot represent some values
#exactly due to their limited number of bits—

print(1.1 + 2.2)
#3.3000000000000003 not 3.3
