#Sets, are neither mappings nor sequences; they are unordered collections of
#unique and immutable objects.
#we create sts by calling the built-in set funciton or using new set literals and expressions
#they support mathematial set operations

X = set('spam') #makes a set out of a sequence
Y = {'h','a','m'} #makes a set with set literals

print(X,'\n',Y)

Z = X,Y #A tuple of two sets

Z = X & Y #Intersection
print(Z)

Z = X | Y #Union
print(Z)

Z = X - Y #Difference
print(Z)

Z = X > Y #Superset
print(Z)

Z = {n**2 for n in [1,2,3,4]} #Set comprehension
print(Z)

#filtering out duplicates in list using sets
list1 = set('eqweqweqweqweqweqweqweqweqweqweqweqweqwleqweqweqwelqweqweq')
list2 = set('qweqweqdasdsdqwelqweqjweqwjeqweqwekqweqlweqwpeqweqweqkweqe')

print((set(list1)))
print(list2 - list1)



#cannot happen in list
list1 = list('eqweqweqweqweqweqweqweqweqweqweqweqweqwleqweqweqwelqweqweq')
list2 = list('qweqweqdasdsdqwelqweqjweqwjeqweqwekqweqlweqwpeqweqweqkweqe')


print(set(list2) - set(list1))

