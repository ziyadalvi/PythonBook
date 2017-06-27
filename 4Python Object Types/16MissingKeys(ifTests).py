#as mappings, dictionaries support accessing items by key only. With sorts of
#operations we've just seen. In addition, though, they also support type-specific
#operations with method calls that are useful in variety of ocmmon usecases

# For example, although
#we can assign to a new key to expand a dictionary, fetching a nonexistent key
#is still a mistake:

D = {'a':1,'b':2,'c':3}
print(D)

print(D['a'])

# print(D['d']) this will throw an error, as it is non existant array

D['d'] = 99
print(D['d'])

#The dictionary in membership expression allows us
#to query the existence of a key and branch on the result with a Python if statement.

#it consists of the word if, followed by an expression that
#is interpreted as a true or false result
print('f' in D)

if not 'f' in D:
    print('missing')

#Besides the in test, there are a variety of ways to avoid accessing nonexistent keys in
#the dictionaries we create
    # 1: the get method
    # 2: the try statement
    # 3: the if/else epression
value = D.get('x',0) #if x exists in D then print the value else assign 0 to value
print(value)

value = D.get('d',0)
print(value)

value = D['x'] if 'x' in D else 0
print(value)
