#Decimal Basics

print(0.1+0.1+0.1-0.3)
#printing the result to produce the user-friendly display
#format doesn’t completely help either, because the hardware related to floating-point
#math is inherently limited in terms of accuracy (a.k.a. precision)

#so
from decimal import Decimal
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))

#Explaination:
#we can make decimal objects by calling the Decimal constructor function
#in the decimal module and passing in strings that have the desired number of decimal
#digits for the resulting object (using the str function to convert floating-point values
#to strings if needed).

#When decimals of different precision are mixed in expressions,
#Python converts up to the largest number of decimal digits automatically

print(Decimal('0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30'))
