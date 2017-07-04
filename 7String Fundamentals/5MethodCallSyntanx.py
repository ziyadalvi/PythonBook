#Method Call Syntax

#Attribute fetches:
#An expression of the form object.attribute means “fetch the value of attribute
#in object.”

#Call expressions:
#An expression of the form function(arguments) means “invoke the code of func
#tion, passing zero or more comma-separated argument objects to it, and return
#function’s result value.”


#Putting these two together allows us to call a method of an object. The method call
#expression:
#object.method(arguments)
#Call method to process object with arguments.

S = 'spam'
result = S.find('pa')

print(result)
