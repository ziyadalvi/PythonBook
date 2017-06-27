#Numeric Ttypes
print(1/3)
print((2/3)+(1/2))

#n, Python recently grew a few new numeric types: decimal numbers, which
#are fixed-precision floating-point numbers, and fraction numbers, which are rational
#numbers with both a numerator and a denominator. Both can be used to work around
#the limitations and inherent inaccuracies of floating-point math

from decimal import Decimal, getcontext
d = Decimal('3.141') # Decimals: fixed precision
print(d+1)
d = d + Decimal('3.87878787878')
print(d)


getcontext().prec = 2
d = Decimal('1.00')/Decimal('3.00')
print(d)

from fractions import Fraction #Fractions: numerator + denominator

f = Fraction(2,3)
f = f + 1
print(f)

