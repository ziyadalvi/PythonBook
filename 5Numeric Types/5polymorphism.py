#Operator overloading and polymorphism
#Although we are focused on built-in numbers right now, all Python operators may be overloaded
#(implemented) by Python classes and C extension types to work on objects you create.

#E.g:
#Objects coded with classes may be added or concatenated with x+y expressions, indexed with
#x[i] expressions.

#Python automatically overloads some operators, such that they perform different actions
#depending on the type of built-in object being processed

#E.g: the + operator adds when applied to numbers but performs concatenation when applied to
#strings

#This is called polymorphism- a term indicating that the meaning of operations depends on
#the type of objects being operated on.
