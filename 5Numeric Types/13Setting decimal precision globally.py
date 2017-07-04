#Global precision
import decimal
print(decimal.Decimal(1) / decimal.Decimal(7))

decimal.getcontext().prec = 4 #Setting global precision

print(decimal.Decimal(1) / decimal.Decimal(7))
