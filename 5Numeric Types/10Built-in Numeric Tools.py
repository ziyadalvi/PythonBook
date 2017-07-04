#Built-in Numeric Tools

import math
print(math.pi, math.e) # Common constants

print(math.sqrt(144), math.sqrt(2)) # Square root

print(pow(2, 4), 2 ** 4, 2.0 ** 4.0) # Exponentiation (power)

print(abs(-42.0), sum((1, 2, 3, 4))) # Absolute value, summation

print(min(3, 1, 2, 4), max(3, 1, 2, 4)) # Minimum, maximum

#There are a variety of ways to drop the
#decimal digits of floating-point numbers. We met truncation and floor earlier; we can
#also round, both numerically and for display purposes

print(math.floor(2.567), math.floor(-2.567)) # Floor (next-lower integer)

print(math.trunc(2.567), math.trunc(-2.567)) # Truncate (drop decimal digits)

print(int(2.567), int(-2.567)) # Truncate (integer conversion)

print(round(2.567), round(2.467), round(2.567, 2)) #Round
