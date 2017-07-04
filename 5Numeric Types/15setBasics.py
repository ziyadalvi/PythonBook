#Sets
#set- an unordered collection of unique and immutable objects that supports operations of set theory

x = set('abcde')
y = set('bdxyz')

x = {'a','b','c','d','e'} #new syntax

print(x-y)
print(x|y) #unoion
print(x&y) #intersection
print(x>y, x<y) #superset,subset
print(x^y) #Symmetric difference (XOR) (inverrse of or)

print('e' in x) #is same as

print('e' in 'Elephant', 22 in [11,22,33])

z = x.intersection(y) #same as x&y
print(z)

z.add('SPAM') #insert one item
print(z)

z.update({'X','Y'}) #Merge: inplace union
print(z)

z.remove('b')
print(z)

#iterable containers:

for item in {'a','b','c'}: print(item * 3)

#Set expression generally require two sets, their method-based counterparts can work with
#any iterable type as well

S = set([1,2,3])
print(S)

print(S | set([3,4]))
