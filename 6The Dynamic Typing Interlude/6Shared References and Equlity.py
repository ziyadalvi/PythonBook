#Python caches and reuses small integers and small strings, as mentioned earlier,
#the object 42 here is probably not literally reclaimed; instead, it will likely remain in a
#system table to be reused the next time you generate a 42 in your code

x = [1,2,3]
y = x


#the == operator, tests whether the two referenced objects have
#the same values; this is the method almost always used for equality checks in Python.
#The second method, the is operator, instead tests for object identity—it returns True
#only if both names point to the exact same object

print(x == y)
print(x is y)

L = [1,2,3]
M = [1,2,3]

print(L == M)
print(L is M)
