#although you can’t mix strings and number types around operators such as +,
#you can manually convert operands before that operation if needed:

S = "42"
I = 1
S + I

#TypeError: Can't convert 'int' object to str implicitly

int(S) + I # Force addition
#43

S + str(I) # Force concatenation
#'421'


