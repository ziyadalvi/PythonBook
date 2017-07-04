#Fraction Basics

from fractions import Fraction

x = Fraction(1,3)
y = Fraction(4,6)

print(x)
print(y)

#Fractions can be used in mathematical expressions as usual

print(x+y)
print(x-y)

print(Fraction('.25'))

#Both Fraction and
#Decimal provide ways to get exact results, albeit at the cost of some speed and code
#verbosity. For instance, in the following example (repeated from the prior section),
#floating-point numbers do not accurately give the zero answer expected, but both of
#the other types do:

print(0.1 + 0.1 + 0.1 - 0.3) # This should be zero (close, but not exact)
#5.551115123125783e-17

from fractions import Fraction
print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))
#Fraction(0, 1)

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
#Decimal('0.0')
