#Division: Classic, Floor, and True

#X/Y Classic and true division. Performs true division, always keeping the remainders in floating-point
#results, regardless of types

#X//Y Floor division. This truncates fractional remainders down to their floor. It's result
#type depends on the types of operands

X = 2.5
Y = 3.2
print(X/Y)
print(X // Y) #the data type of the result for // is still dependent on the operand types

X = 2
Y = 4
print(X/Y)
print(X // Y)

#the // operator is informally called truncating division, but it’s more
#accurate to refer to it as floor division—it truncates the result down to its floor, which
#means the closest whole number below the true result. The net effect is to round down,
#not strictly truncate, and this matters for negatives.

import math
print(math.floor(2.5)) #Closest number below value
#2
print(math.floor(-2.5))
#-3
print(math.trunc(2.5))
#2
print(math.trunc(-2.5))
#-2

#now lets see / and //
print((5 / 2, 5 / -2))
#(2.5, -2.5)

print((5 // 2, 5 // -2))
#(2, -3) #floor results
