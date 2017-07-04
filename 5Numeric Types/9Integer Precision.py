#Integer Precision

print(999999999999999999999999999999+1)
print(2 ** 200)

#Because Python must do extra work to support their extended precision, integer math
#is usually substantially slower than normal when numbers grow large. However, if you
#need the precision, the fact that it’s built in for you to use will likely outweigh its
#performance penalty.
