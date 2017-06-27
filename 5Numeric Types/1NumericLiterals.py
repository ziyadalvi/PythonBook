#Numeric Literals/187
x = 1234, -24, 0, 99999999999999 #Integers (unlimited size)
print(x)

x = 1.23, 1., 3.14e-10, 4E210, 4.0e+210 #Floating-point numbers
print(x)

x = 0o177, 0x9ff, 0b101010 #Octal, hex, and binary literals in 3.X
print(x)

x = 0o177, 0x9ff, 0b101010 #Octal, octal, hex, and binary literals in 2.X
print(x)

x = 3+4j, 3.0+4.0j, 3J #Complex number literals
print(x)

x = set('spam') # {1, 2, 3, 4} Sets: 2.X and 3.X construction forms
print(x)

x = Decimal('1.0') # Fraction(1, 3) Decimal and fraction extension types
print(x)

x = bool(x) #, True, False Boolean type and constants
print(x)



