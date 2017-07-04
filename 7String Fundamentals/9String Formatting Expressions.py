#String Formatting Expressions

#string formatting allows us to perform multiple type-specific substitutions on a
#string in a single step. It’s never strictly required, but it can be convenient, especially
#when formatting text to be displayed to a program’s users

#String formatting expressions: '...%s...' % (values):
#The original technique available since Python’s inception, this form is based upon
#the C language’s “printf” model, and sees widespread use in much existing code.

#String formatting method calls: '...{}...'.format(values):
#A newer technique added in Python 2.6 and 3.0, this form is derived in part from
#a same-named tool in C#/.NET, and overlaps with string formatting expression
#functionality.

