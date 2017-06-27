#Type Checking
#How to Break Your Code’s Flexibility

#We can see the type of an object by passing it in type built-in function that gives
#the type of the object


L = str
print(type(L))

L = [1,2,3,'123',None]
print(type(L))


#there are at least three ways to do so in a Python script

if type(L) == type([]): #checking by direct declaration
    print('yes')

if type(L) == list: #checkign by list type object
    print('yes')

if isinstance(L, list):
    print('yes')


#this is almost always the wrong thing to do in a Python program
#(and often a sign of an ex-C programmer first starting to use Python!)
#The reason why  is that by checking for specific types in your code, you effectively break its flexibility—you limit it to
#working on just one type. Without such tests, your code may be able to work on a
#whole range of types.
#This is related to the idea of polymorphism, and it stems from
#Python’s lack of type declarations. As you’ll learn, in Python, we code to object interfaces
#(operations supported), not to types. That is, we care what an object does, not
#what it is. 


    
